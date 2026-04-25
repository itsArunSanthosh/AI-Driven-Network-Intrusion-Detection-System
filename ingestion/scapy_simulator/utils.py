import random

def generate_ip():
    return f"10.0.0.{random.randint(1, 254)}"

def generate_external_ip():
    return f"192.168.1.{random.randint(1, 254)}"

def generate_port():
    return random.randint(1024, 65535)