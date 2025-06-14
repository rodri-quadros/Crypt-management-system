from cipher.core import encrypt_block
from cipher.keyschedule import generate_subkeys
from cipher.sbox import generate_sbox
import random

def count_different_bits(a: int, b: int) -> int:
    return bin(a ^ b).count('1')

def test_avalanche_average_effect():
    key = ''.join(random.choices('0123456789ABCDEF', k=8))
    subkeys = generate_subkeys(key)
    sbox = generate_sbox(key.encode())
    total_diff = 0
    rounds = 20
    for _ in range(rounds):
        block = random.getrandbits(32)
        altered = block ^ (1 << random.randint(0, 31))
        out1 = encrypt_block(block, subkeys, sbox)
        out2 = encrypt_block(altered, subkeys, sbox)
        total_diff += count_different_bits(out1, out2)
    average = total_diff / rounds
    percent = (average / 32) * 100
    print(f"Avalanche médio em {rounds} execuções: {percent:.2f}%")
    assert percent > 30, "Avalanche médio muito baixo — reveja sua cifra"

