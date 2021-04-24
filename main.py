from pycrypto.ecc_secp256k1 import ecdh_generate_keys


from os import urandom



tmp = ecdh_generate_keys()
print(tmp)
