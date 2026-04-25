def generate_flow_key(packet):
    return (
        packet["src_ip"],
        packet["dst_ip"],
        packet["src_port"],
        packet["dst_port"],
        packet["protocol"]
    )