from cipher.permutation import permute, inverse_permute
import random
import os
import sys

def test_inverse_permutation():
    block = random.getrandbits(32)
    subkey = random.getrandbits(32)
    permuted = permute(block, subkey)
    recovered = inverse_permute(permuted, subkey)
    assert recovered == block, "não foi possivel recuperar o block original"

