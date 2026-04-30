from .flow_state import FlowState

class FlowAggregator:
    def __init__(self):
        self.active_flows = {}

    def process_packet(self, packet: dict):
        # TODO: Update flow state or create new flow
        pass

    def emit_flow(self, flow_state: FlowState) -> dict:
        """
        Convert flow state into final flow record.
        """
        return {
            "flow_id": "generated_id",
            "packet_count": flow_state.total_packets,
            "total_bytes": flow_state.total_bytes
        }