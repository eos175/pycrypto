from pycrypto import ecc_secp256k1 as ecc
from pycrypto.os import urandom_sw
from pycrypto import aes

import random


random.seed(0)

data = b"Hola un gusto saludarte"


"""
tag_len = 12
key = urandom_sw(32)
nonce = urandom_sw(12)

print(f"{key.hex()=} {nonce.hex()=}")



out = aes.ccm_encrypt(data, key, nonce, tag_len)
print(f"{out.hex()=}")
print(aes.ccm_decrypt(out, key, nonce, tag_len))

print()

out = aes.gcm_encrypt(data, key, nonce, tag_len)
print(f"{out.hex()=}")
print(aes.gcm_decrypt(out, key, nonce, tag_len))

"""


"""

key = urandom_sw(32)
iv = urandom_sw(16)

print(f"{key.hex()=} {iv.hex()=}")

out = aes.cbc_encrypt(data, key, iv)
print(f"{out.hex()=}")
print(aes.cbc_decrypt(out, key, iv))


"""



priv1, pub1 = ecc.ecdh_generate_keys(urandom_sw)
priv2, pub2 = ecc.ecdh_generate_keys(urandom_sw)


sig = ecc.ecdsa_sign_sha256(priv1, data)

print(f"{priv1.hex()=} {pub1.hex()=} {sig.hex()=}")


print(ecc.ecdsa_verify_sha256(pub1, sig, data))

