import random

def generate_sbox(seed_bytes: bytes):
    base_sbox = list(range(16))
    random.seed(seed_bytes)
    random.shuffle(base_sbox)
    sbox = {i: base_sbox[i] for i in range(16)}
    return sbox 

def generate_reverse_sbox(sbox: dict):
    reversed_sbox = {}
    for k, v in sbox.items():
        reversed_sbox[v] = k
    return reversed_sbox

def print_log_sbox(sbox: dict) -> str:
    log = ""
    for k in sorted(sbox.keys()):
        log += (f"{k} -> {sbox[k]}\n")
    return log