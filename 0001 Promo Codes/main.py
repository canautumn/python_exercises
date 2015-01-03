import os
import binascii

def num_to_string(number, pad_to_length=None):
    """
    https://github.com/stochastic-technologies/shortuuid/blob/develop/shortuuid/main.py
    """
    alphabet = list("23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
                    "abcdefghijkmnopqrstuvwxyz")
    output = ""
    while number:
        number, digit = divmod(number, len(alphabet))
        output += alphabet[digit]
    if pad_to_length:
        remainder = max(pad_to_length - len(output), 0)
        output = output + alphabet[0] * remainder
    return output
    
def promo_code(length):
    return num_to_string(int(binascii.b2a_hex(os.urandom(length)), 16), 
                         pad_to_length=length)[:length]
    
if __name__ == '__main__':
    length = 10
    for _ in range(200):
        print promo_code(length)
