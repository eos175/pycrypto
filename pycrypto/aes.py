from Crypto.Cipher import AES


"""

https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

"""



def cbc_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding = AES.block_size - (len(data) % AES.block_size)
    data += bytearray([padding]) * padding # PKCS#7
    return cipher.encrypt(data)

def cbc_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = cipher.decrypt(data)
    padding = data[-1]
    if data[-padding:] != bytearray([padding]) * padding:
        raise ValueError("[!] Invalid padding.")
    return data[:-padding]





def cfb128_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.encrypt(data)


def cfb128_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.decrypt(data)



def gcm_encrypt(data: bytes, key: bytes, nonce: bytes, tag_len: int = 16) -> bytes:
    cipher = AES.new(key, AES.MODE_GCM, nonce, mac_len=tag_len)
    return cipher.encrypt(data) + cipher.digest()


def gcm_decrypt(data: bytes, key: bytes, nonce: bytes, tag_len: int = 16) -> bytes or None:
    data, tag = data[:-tag_len], data[-tag_len:]
    cipher = AES.new(key, AES.MODE_GCM, nonce, mac_len=tag_len)
    out = cipher.decrypt(data)
    try:
        cipher.verify(tag)
    except ValueError as e:
        return None
    return out



def ccm_encrypt(data: bytes, key: bytes, nonce: bytes, tag_len: int = 16) -> bytes:
    cipher = AES.new(key, AES.MODE_CCM, nonce, mac_len=tag_len)
    return cipher.encrypt(data) + cipher.digest()

def ccm_decrypt(data: bytes, key: bytes, nonce: bytes, tag_len: int = 16) -> bytes or None:
    data, tag = data[:-tag_len], data[-tag_len:]
    cipher = AES.new(key, AES.MODE_CCM, nonce, mac_len=tag_len)
    out = cipher.decrypt(data)
    try:
        cipher.verify(tag)
    except ValueError:
        return None
    return out
    
