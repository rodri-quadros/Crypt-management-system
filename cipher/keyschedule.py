from utils.bitops import rotate_left

def generate_subkeys(str_key):
    if len(str_key) == 8:
        int_key = int(str_key, 16)
        subkey_one = int_key & 0xFFFFFFFF
        subkey_two = rotate_left(int_key, 12) & 0xFFFFFFFF
        subkey_three = (int_key ^ 0xA5A5A5A5) & 0xFFFFFFFF
        return [subkey_one, subkey_two, subkey_three] 
    else:
        raise ValueError("A chave precisa ter 8 caracteres hexadecimais")