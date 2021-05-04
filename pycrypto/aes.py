from Crypto.Cipher import AES


"""

https://pycryptodome.readthedocs.io/en/latest/src/introduction.html

"""


def cfb128_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.encrypt(data)


def cfb128_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    cipher.encrypt_and_digest()
    return cipher.decrypt(data)



def gcm_encrypt(data: bytes, key: bytes, nonce: bytes, mac_len: int = None) -> bytes:
    cipher = AES.new(key, AES.MODE_GCM, nonce, mac_len=mac_len)
    return cipher.encrypt(data), cipher.digest()

def gcm_decrypt(data: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes or None:
    cipher = AES.new(key, AES.MODE_GCM, nonce, mac_len=len(tag))
    d = cipher.decrypt(data)
    try:
        cipher.verify(tag)
    except ValueError:
        return None
    return d



def ccm_encrypt(data: bytes, key: bytes, nonce: bytes, mac_len: int = None) -> bytes:
    cipher = AES.new(key, AES.MODE_CCM, nonce, mac_len=mac_len)
    return cipher.encrypt(data), cipher.digest()

def ccm_decrypt(data: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes or None:
    cipher = AES.new(key, AES.MODE_CCM, nonce, mac_len=len(tag))
    d = cipher.decrypt(data)
    try:
        cipher.verify(tag)
    except ValueError:
        return None
    return d
    


if __name__ == "__main__":
    from os import urandom

    aes_key = urandom(32)
    nonce = urandom(12)
    
    data = b"hola idiota como estas"
    
    data_enc, tag = ccm_encrypt(data, aes_key, nonce)
    
    print(data_enc)
    print(ccm_decrypt(data_enc, aes_key, nonce, tag))
