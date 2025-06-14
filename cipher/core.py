from cipher.keyschedule import generate_subkeys
from cipher.sbox import generate_sbox, generate_reverse_sbox
from cipher.permutation import permute, inverse_permute
import random

def encrypt_block(block: int, subkeys: list, sbox:dict, verbose_log: list = None) -> int:
    for i in range(3):
        block ^= subkeys[i]
        if verbose_log is not None:
            print(f"rodada {i+1} - após XOR {block:08x}")
        block = substitute_block(block, sbox)
        if verbose_log is not None:
            print(f"rodada {i+1} - após substituição {block:08x}")
        block = permute(block, subkeys[i])    
        if verbose_log is not None:
            print(f"rodada {i+1} - após permutação {block:08x}")
    return block

def decrypt_block(block: int, subkeys: list, sbox_inv: dict) -> int:
    for i in reversed(range(3)):
        block = inverse_permute(block, subkeys[i])
        block = inverse_substitute_block(block, sbox_inv)
        block ^= subkeys[i]
    return block

def substitute_block(block: int, sbox: dict) -> int:
    new_block_generated = 0
    for i in range(8):
        nibble = (block >> (i * 4)) & 0xF
        substitution = sbox[nibble]
        new_block_generated |= (substitution << (i * 4))
    return new_block_generated

def inverse_substitute_block(block: int, sbox_inv: dict) -> int:
    new_block_generated = 0
    for i in range(8):
        nibble = (block >> (i * 4)) & 0xF
        substitution = sbox_inv[nibble]
        new_block_generated |= (substitution << (i * 4))
    return new_block_generated

def encrypt_file(file_path: str, key: str):
    with open(file_path, 'rb') as f:
        data = f.read()
    padding_len = 4 - (len(data) % 4)
    padding = bytes([padding_len] * padding_len)
    data += padding
    subkeys = generate_subkeys(key)
    sbox = generate_sbox(key.encode())
    encrypted_data = b""
    for i in range(0, len(data), 4):
        block_bytes = data[i:i+4]
        block_int = int.from_bytes(block_bytes, 'big')
        encrypted_block = encrypt_block(block_int, subkeys, sbox)
        encrypted_data += encrypted_block.to_bytes(4, 'big')
    output_path = file_path + '.enc'
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    return output_path
    
def decrypt_file(file_path: str, key: str):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    subkeys = generate_subkeys(key)
    sbox = generate_sbox(key.encode())
    sbox_inv = generate_reverse_sbox(sbox)
    decrypted_data = b""
    for i in range(0, len(encrypted_data), 4):
        block_bytes = encrypted_data [i:i+4]
        block_int = int.from_bytes(block_bytes, 'big')
        decrypted_block = decrypt_block(block_int, subkeys, sbox_inv)
        decrypted_data += decrypted_block.to_bytes(4, 'big')
    padding_len = decrypted_data[-1]
    decrypted_data = decrypted_data[:- padding_len]
    output_path = file_path.replace(".enc", "") + ".dec"
    with open(output_path, 'wb') as f: 
        f.write(decrypted_data)
    return output_path
        