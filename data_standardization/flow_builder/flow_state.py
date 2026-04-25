import time

class FlowState:

    def __init__(self, flow_key, packet):
        self.flow_key = flow_key
        self.start_time = packet["timestamp"]
        self.last_seen = packet["timestamp"]

        self.total_packets = 1
        self.total_bytes = packet["packet_size"]

        self.bytes_sent = packet["packet_size"]
        self.bytes_received = 0

    def update(self, packet):
        self.last_seen = packet["timestamp"]
        self.total_packets += 1
        self.total_bytes += packet["packet_size"]