from random import getrandbits

def urandom_sw(size: int) -> bytes:
    """Generate n random bytes."""
    return getrandbits(8 * size).to_bytes(size, "little")


