import time
from .flow_key import generate_flow_key
from .flow_state import FlowState

FLOW_TIMEOUT = 5  # seconds

class FlowAggregator:

    def __init__(self):
        self.flows = {}

    def process_packet(self, packet):
        key = generate_flow_key(packet)

        if key not in self.flows:
            self.flows[key] = FlowState(key, packet)
        else:
            self.flows[key].update(packet)

    def emit_expired_flows(self):
        current_time = time.time()
        expired = []

        for key, flow in list(self.flows.items()):
            if current_time - flow.last_seen > FLOW_TIMEOUT:
                expired.append(self._build_flow_record(flow))
                del self.flows[key]

        return expired

    def _build_flow_record(self, flow):
        duration = max(flow.last_seen - flow.start_time, 1e-5)

        return {
            "flow_id": str(hash(flow.flow_key)),
            "timestamp": int(flow.last_seen),

            "src_ip": flow.flow_key[0],
            "dst_ip": flow.flow_key[1],
            "src_port": flow.flow_key[2],
            "dst_port": flow.flow_key[3],
            "protocol": flow.flow_key[4],

            "duration": duration,
            "bytes_sent": flow.bytes_sent,
            "bytes_received": flow.bytes_received,
            "packet_count": flow.total_packets,

            "bytes_per_second": flow.total_bytes / duration,
            "packets_per_second": flow.total_packets / duration,

            "is_internal_src": flow.flow_key[0].startswith("10."),
            "is_internal_dst": flow.flow_key[1].startswith("192.")
        }