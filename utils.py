import string

BASE62 = string.ascii_letters + string.digits

def encode(num):
    if num == 0:
        return BASE62[0]
    
    base = len(BASE62)
    short = []
    
    while num > 0:
        short.append(BASE62[num % base])
        num //= base
        
    return ''.join(reversed(short))

def decode(short):
    base = len(BASE62)
    num = 0
    
    for char in short:
        num = num * base + BASE62.index(char)
        
    return num