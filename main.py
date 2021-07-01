from pycrypto.ecc_secp256k1 import ecdh_generate_keys
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



key = urandom_sw(32)
iv = urandom_sw(16)

print(f"{key.hex()=} {iv.hex()=}")

out = aes.cbc_encrypt(data, key, iv)
print(f"{out.hex()=}")
print(aes.cbc_decrypt(out, key, iv))



