"""
Streamlit dashboard for AI-NIDS.

Displays:
- Alerts
- Risk scores
- Simple metrics
"""

import streamlit as st
import random
import time

st.title("🚨 AI-Powered NIDS Dashboard")

# Simulated data
def generate_data():
    return {
        "entity": f"10.0.0.{random.randint(1,50)}",
        "risk_score": round(random.random(), 2),
        "label": random.choice(["benign", "malicious"])
    }

# Display section
st.header("Live Alerts")

for _ in range(5):
    data = generate_data()

    if data["label"] == "malicious":
        st.error(f"{data['entity']} → Risk: {data['risk_score']}")
    else:
        st.success(f"{data['entity']} → Risk: {data['risk_score']}")

# Metrics
st.header("System Metrics")

st.metric("Requests/sec", random.randint(50, 150))
st.metric("Avg Latency (ms)", random.randint(50, 300))
st.metric("False Positive Rate", round(random.random(), 2))

st.caption("Demo dashboard — replace with real pipeline integration")