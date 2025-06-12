import random

def permute(block: int, subkey: int) -> int:
    positions = list(range(32))
    random.seed(subkey)
    random.shuffle(positions)
    new_block = 0
    for i in range(32):
        if (block >> i) & 1:
            new_block |= (1 << positions[i])
    return new_block

def inverse_permute(block: int, subkey: int) -> int:
    positions = list(range(32))
    random.seed(subkey)
    random.shuffle(positions)
    new_inversed_block = 0
    for i in range(32): 
        if (block >> positions[i]) & 1:
            new_inversed_block |= (1 << i)
    return new_inversed_block