import streamlit as st
import pandas as pd
import json
import time
from kafka import KafkaConsumer
from collections import defaultdict, deque, Counter
from streamlit_autorefresh import st_autorefresh

# Graph imports
import networkx as nx
from pyvis.network import Network
import tempfile

# ---------- CONFIG ----------
st.set_page_config(page_title="AI-NIDS SOC Dashboard", layout="wide")
st.title("--AI-NIDS Security Operations Center--")

# ---------- AUTO REFRESH ----------
st_autorefresh(interval=2000, key="refresh")

# ---------- SIDEBAR ----------
st.sidebar.header(" Filters")

filter_ip = st.sidebar.text_input("Filter by Source IP")

filter_attack = st.sidebar.selectbox(
    "Attack Type",
    ["All", "DDoS", "Port Scan", "Brute Force", "Normal"]
)

filter_severity = st.sidebar.selectbox(
    "Severity",
    ["All", "CRITICAL", "HIGH", "MEDIUM", "LOW"]
)

# ---------- SESSION STATE ----------
if "traffic" not in st.session_state:
    st.session_state.traffic = deque(maxlen=50)
    st.session_state.alerts = deque(maxlen=20)
    st.session_state.timeline = deque(maxlen=30)
    st.session_state.graph_edges = deque(maxlen=100)
    st.session_state.packet_count = 0
    st.session_state.connection_tracker = defaultdict(list)

# ---------- KAFKA ----------
@st.cache_resource
def get_consumer():
    return KafkaConsumer(
        "raw-network-events",
        bootstrap_servers="localhost:9092",
        auto_offset_reset="latest",
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode("utf-8"))
    )

consumer = get_consumer()

WINDOW_SIZE = 5

# ---------- AI LOGIC ----------
def calculate_risk(connection_count, is_attack):
    score = min(100, 60 + connection_count * 4) if is_attack else min(50, connection_count * 2)
    if score > 85: return score, "CRITICAL"
    elif score > 70: return score, "HIGH"
    elif score > 40: return score, "MEDIUM"
    else: return score, "LOW"

def classify_attack(connection_count, is_attack):
    if not is_attack: return "Normal"
    if connection_count > 12: return "DDoS"
    elif connection_count > 8: return "Port Scan"
    else: return "Brute Force"

def get_model_label(attack_type):
    return {
        "DDoS": "Isolation Forest",
        "Port Scan": "LSTM",
        "Brute Force": "Random Forest"
    }.get(attack_type, "Baseline")

def calculate_confidence(score):
    return round(min(99, 50 + score * 0.5), 2)

def explain_prediction(connection_count, score):
    return f"High connection rate ({connection_count}/5s) + anomaly score {score}"

# ---------- NETWORK GRAPH ----------
def render_graph(edges):
    G = nx.Graph()

    # Build graph
    for src, dst in edges:
        G.add_edge(src, dst)

    net = Network(
        height="400px",
        width="100%",
        bgcolor="#0e1117",
        font_color="white"
    )

    # Add nodes
    for node in G.nodes():
        degree = G.degree(node)
        net.add_node(
            node,
            label=node,
            size=10 + degree * 3
        )

    # Add edges
    for edge in G.edges():
        net.add_edge(edge[0], edge[1])

    # SAVE AS FIXED HTML FILE
    file_path = "network_graph.html"
    net.save_graph(file_path)

    return file_path

# ---------- INGESTION ----------
messages = consumer.poll(timeout_ms=200)

for tp, msgs in messages.items():
    for msg in msgs:
        data = msg.value
        src_ip = data["src_ip"]
        dst_ip = data["dst_ip"]
        now = time.time()
        is_attack = data.get("attack", False)

        st.session_state.packet_count += 1

        tracker = st.session_state.connection_tracker
        tracker[src_ip].append(now)
        tracker[src_ip] = [t for t in tracker[src_ip] if now - t <= WINDOW_SIZE]

        connection_count = len(tracker[src_ip])

        score, level = calculate_risk(connection_count, is_attack)
        attack_type = classify_attack(connection_count, is_attack)
        model = get_model_label(attack_type)
        confidence = calculate_confidence(score)
        explanation = explain_prediction(connection_count, score)

        # Store traffic
        st.session_state.traffic.append({
            "Time": time.strftime("%H:%M:%S"),
            "Source": src_ip,
            "Destination": dst_ip,
            "Protocol": data["protocol"],
            "Attack Type": attack_type,
            "Risk Score": score,
            "Risk Level": level,
            "Model": model,
            "Confidence %": confidence
        })

        # Graph edges
        st.session_state.graph_edges.append((src_ip, dst_ip))

        # Alerts + timeline
        if level in ["HIGH", "CRITICAL"]:
            alert = {
                "Time": time.strftime("%H:%M:%S"),
                "IP": src_ip,
                "Attack": attack_type,
                "Risk": score,
                "Confidence": confidence,
                "Model": model,
                "Explanation": explanation,
                "Severity": level
            }
            st.session_state.alerts.append(alert)
            st.session_state.timeline.append(alert)

# ---------- KPI ----------
k1, k2, k3, k4 = st.columns(4)

k1.metric(" Packets", st.session_state.packet_count)
k2.metric(" Alerts", len(st.session_state.alerts))
k3.metric(" Active IPs", len(st.session_state.connection_tracker))
k4.metric(" Attack Traffic",
          sum(1 for t in st.session_state.traffic if t["Attack Type"] != "Normal"))

st.divider()

# ---------- LAYOUT ----------
# ================= MAIN GRID =================
row1_col1, row1_col2 = st.columns([2,1])

# ---------- TRAFFIC ----------
with row1_col1:
    st.subheader("__Live Traffic__")

    df = pd.DataFrame(list(st.session_state.traffic))

    # Filters
    if filter_ip:
        df = df[df["Source"].str.contains(filter_ip)]
    if filter_attack != "All":
        df = df[df["Attack Type"] == filter_attack]
    if filter_severity != "All":
        df = df[df["Risk Level"] == filter_severity]

    st.dataframe(df, use_container_width=True)

    selected_index = st.selectbox(
        "Select event for investigation",
        df.index.tolist()
    ) if not df.empty else None

# ---------- ALERTS ----------
with row1_col2:
    st.subheader("__Alerts__")

    html = ""
    for a in list(st.session_state.alerts)[::-1]:
        color = "#f04848" if a["Severity"]=="CRITICAL" else "#eb9c4d"
        html += f"<div style='background:{color};padding:8px;margin-bottom:6px'>{a['Attack']} | {a['IP']} | {a['Risk']}</div>"

    st.markdown(f"<div style='height:400px;overflow-y:auto'>{html}</div>", unsafe_allow_html=True)

row2_col1, row2_col2 = st.columns([2,1])

# ---------- EXPLAIN ----------
with row2_col1:
    st.subheader("__Explainable AI__")

    if st.session_state.alerts:
        latest = st.session_state.alerts[-1]

        st.markdown(f"""
        <div style="
            background-color:#111827;
            padding:15px;
            border-radius:8px;
            border-left:5px solid #3b82f6;
        ">
        <b>Attack Type:</b> {latest['Attack']} <br>
        <b>Model:</b> {latest['Model']} <br>
        <b>Risk Score:</b> {latest['Risk']} <br>
        <b>Confidence:</b> {latest['Confidence']}% <br><br>

        <b>Explanation:</b><br>
        {latest['Explanation']}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.info("No alerts available for explanation.")

# ---------- TOP ATTACKERS ----------
from collections import Counter

with row2_col2:
    st.subheader("__Top Attackers__")

    counts = Counter([a["IP"] for a in st.session_state.alerts])

    if counts:
        top_5 = counts.most_common(5)

        for ip, count in top_5:
            st.markdown(f"""
            <div style="
                background-color:#1f2937;
                padding:10px;
                margin-bottom:8px;
                border-radius:6px;
                border-left:5px solid #ff4d4d;
            ">
            <b>{ip}</b><br>
            Alerts: {count}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("No attackers detected yet.")

row3_col1, row3_col2 = st.columns([2,1])

# ---------- TIMELINE ----------
with row3_col1:
    st.subheader("__Attack Timeline__")

    if st.session_state.timeline:
        st.dataframe(
            pd.DataFrame(list(st.session_state.timeline)[::-1]),
            use_container_width=True
        )

# ---------- GRAPH ----------
with row3_col2:
    st.subheader("__Network Graph__")

    if st.session_state.graph_edges:
        graph_file = render_graph(st.session_state.graph_edges)

        with open(graph_file, "r", encoding="utf-8") as f:
            html = f.read()

        st.components.v1.html(html, height=420)

st.divider()
st.subheader("__Investigation Panel__")

if selected_index is not None:
    row = df.loc[selected_index]

    colA, colB = st.columns(2)

    with colA:
        st.write(f"**Source IP:** {row['Source']}")
        st.write(f"**Destination:** {row['Destination']}")
        st.write(f"**Attack Type:** {row['Attack Type']}")

    with colB:
        st.write(f"**Risk Score:** {row['Risk Score']}")
        st.write(f"**Model:** {row['Model']}")
        st.write(f"**Confidence:** {row['Confidence %']}%")

else:
    st.info("Select an event to investigate.")

# ---------- DRILL DOWN ----------

if selected_index is not None:
    row = df.loc[selected_index]
    st.write(row)
else:
    st.info("Select an event")

# ---------- FOOTER ----------
st.caption("SOC Dashboard | Real-time AI NIDS")