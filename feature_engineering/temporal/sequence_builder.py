"""
Builds sequences of flows for temporal modeling (LSTM-ready).
"""

from collections import defaultdict

class SequenceBuilder:
    def __init__(self, max_length=10):
        self.max_length = max_length
        self.sequences = defaultdict(list)

    def update(self, flow: dict):
        src_ip = flow["src_ip"]
        self.sequences[src_ip].append(flow)

        if len(self.sequences[src_ip]) > self.max_length:
            self.sequences[src_ip].pop(0)

        return self.sequences[src_ip]