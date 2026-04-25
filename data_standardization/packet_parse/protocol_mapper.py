def map_protocol(protocol):
    if isinstance(protocol, str):
        return protocol
    return {6: "TCP", 17: "UDP"}.get(protocol, "UNKNOWN")