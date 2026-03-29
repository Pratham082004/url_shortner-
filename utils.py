import string

BASE62 = string.ascii_letters + string.digits + string.digits

def encode(num):
    # Handle the case for 0 explicitly
    if num == 0:
        return BASE62[0]
    
    base = len(BASE62)
    encoded = []

    while num > 0:
        encoded.append(BASE62[num % base])
        num //= base

    return ''.join(reversed(encoded))

def decode(encoded):
    base = len(BASE62)
    num = 0

    for char in encoded:
        num = num * base + BASE62.index(char)

    return num
