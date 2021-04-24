from hmac import digest as HMAC
from hashlib import sha1 as Sha1, sha256 as Sha256



def sha1(data: bytes) -> bytes:
    return Sha1(data).digest()


def sha256(data: bytes) -> bytes:
    return Sha256(data).digest()



def hmac_sha1(key: bytes, msg: bytes) -> bytes:
    return HMAC(key, msg, "sha1")

def hmac_sha256(key: bytes, data: bytes) -> bytes:
    return HMAC(key, data, "sha256")



if __name__ == "__main__":
    print(sha1(b"emmanuel").hex())
    
    