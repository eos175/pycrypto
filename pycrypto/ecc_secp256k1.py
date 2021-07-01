from fastecdsa import keys, ecdsa
from fastecdsa.curve import secp256k1
from fastecdsa.point import Point
from os import urandom

from .hashe import sha256

CURVE = secp256k1


"""

https://github.com/AntonKueltz/fastecdsa

"""


def int_to_bytes(n: int, n_bits: int = 256) -> bytes:
    return n.to_bytes(n_bits >> 3, "big")

def bytes_to_int(b: bytes) -> int:
    return int.from_bytes(b, "big")


    
def encode_public_key(p: Point) -> bytes:
    return int_to_bytes(p.x) + int_to_bytes(p.y)


def decode_public_key(b: bytes):
    x, y = bytes_to_int(b[:32]), bytes_to_int(b[32:])
    return Point(x, y, curve=CURVE)
    


def ecdh_generate_keys(randfunc=urandom):
    priv_key = keys.gen_private_key(CURVE, randfunc)
    pub_key = keys.get_public_key(priv_key, CURVE)
    return int_to_bytes(priv_key), encode_public_key(pub_key)


def ecdh_shared_secret(priv_key: bytes, others_pub: bytes):
    Qp = decode_public_key(others_pub)
    d = bytes_to_int(priv_key)
    z = (Qp * d).x
    return int_to_bytes(z)



def ecdsa_sign_sha256(priv_key: bytes, data: bytes):
    d = bytes_to_int(priv_key)
    tmp = sha256(data)
    r, s = ecdsa.sign(tmp, d, curve=CURVE, prehashed=True) 
    return int_to_bytes(r) + int_to_bytes(s)


def ecdsa_verify_sha256(pub_key: bytes, sig: bytes, data: bytes) -> bool:
    r, s = bytes_to_int(sig[:32]), bytes_to_int(sig[32:])
    Q = decode_public_key(pub_key)
    tmp = sha256(data)
    return ecdsa.verify((r, s), tmp, Q, curve=CURVE, prehashed=True)





if __name__ == "__main__":
    
    priv_key, pub_key = ecdh_generate_keys()
    
    msg = b"hola, como estas?"
    sig = ecdsa_sign_sha256(priv_key, msg)
    valid = ecdsa_verify_sha256(pub_key, sig, msg)
    
    print("priv_key ", priv_key.hex())
    print("pub_key  ", pub_key.hex())
    print("sign     ", sig.hex())
    print("valid    ", valid)
    
    
    priv_key1, pub_key1 = ecdh_generate_keys()
    priv_key2, pub_key2 = ecdh_generate_keys()
    
    secret1 = ecdh_shared_secret(priv_key1, pub_key2)
    secret2 = ecdh_shared_secret(priv_key2, pub_key1)
    
    print()
    
    print("secret", secret1 == secret2, secret1.hex())


