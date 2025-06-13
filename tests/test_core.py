from cipher.core import decrypt_block, encrypt_block
from cipher.keyschedule import generate_subkeys
from cipher.sbox import generate_sbox, generate_reverse_sbox
import random
import sys
import os

def test_encrypt_decrypt_block():
    key = ''.join(random.choices('0123456789ABCDEF', k=8))
    block = random.getrandbits(32)
    subkeys = generate_subkeys(key)
    sbox = generate_sbox(key.encode())
    sbox_inv = generate_reverse_sbox(sbox)
    encrypted = encrypt_block(block, subkeys, sbox)
    decrypted = decrypt_block(encrypted, subkeys, sbox_inv)
    assert decrypted == block
