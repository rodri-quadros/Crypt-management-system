from cipher.keyschedule import generate_subkeys
import random
import os 
import sys

def test_generate_subkeys_lenght():
    key = ''.join(random.choices('0123456789ABCDEF', k=8))
    subkeys = generate_subkeys(key)
    assert len(subkeys) == 3, "é obrigatório gerar exatas 3 subchaves"

def test_generate_subkeys_type():
    key = ''.join(random.choices('0123456789ABCDEF', k=8))
    subkeys = generate_subkeys(key)
    assert all(isinstance(k, int)for k in subkeys), "todas as subkeys devem obrigatoriamente ser inteiros"

def test_generate_subkeys_deterministic():
    key = ''.join(random.choices('ABCDEF', k=8))
    subkey_one = generate_subkeys(key)
    subkey_two = generate_subkeys(key)
    assert subkey_one == subkey_two, "as subkeys devem ser identicas com as mesmas chaves"