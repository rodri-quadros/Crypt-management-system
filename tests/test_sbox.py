from cipher.sbox import generate_reverse_sbox, generate_sbox, print_log_sbox
import random
import os
import sys

def test_generate_sbox_length():
    key = ''.join(random.choices('0123456789ABCDEF', k=16))
    sbox = generate_sbox(key.encode())
    assert len(sbox) == 16, "a sbox deve ter obrigatoriamente 16 entradas"

def test_valid_permutation():
    key = ''.join(random.choices('0123456789ABCDEF', k=16))
    sbox = generate_sbox(key.encode())
    assert len(sbox) == 16, "a sbox deve ter obrigatoriamente 16 entradas"

def test_generate_reverse_sbox(sbox):
    key = ''.join(random.choices('0123456789ABCDEF', k=16))
    sbox_inv = generate_reverse_sbox(key.encode())
    for k, v in sbox.items():
        assert sbox_inv[v] == k, f"as sbox não são correspondentes quando invertidas"

def test_deterministic():
    key = ''.join(random.choices('0123456789ABCDEF', k=16))
    sbox_one = generate_sbox(key.encode())
    sbox_two = generate_sbox(key.encode())
    assert sbox_one == sbox_two, "as sbox devem ser identicas para a mesma key"
        