REQUIRED_FIELDS = [
    "flow_id", "src_ip", "dst_ip",
    "duration", "packet_count"
]

def validate(flow):
    return all(field in flow for field in REQUIRED_FIELDS)