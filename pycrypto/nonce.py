


"""

TODO(eos175)
    
    Nonce determinista para AES_CCM, AES_GCM compuesto por 32 bits fijos y un contador de 64 bits, 
        tal como lo especifica el NIST
        
        `AES-CCM-ICVlen` https://tools.ietf.org/html/rfc5084
        
        
        
    https://crypto.stackexchange.com/questions/41601/aes-gcm-recommended-iv-size-why-12-bytes
    
    https://crypto.stackexchange.com/questions/43641/implementing-gcm-with-dev-urandom-for-a-nonce


"""


class Nonce:

    def __init__(self, 
        fix: int or bytes
    ):
        if isinstance(fix, int):
            tmp = fix << 64
        else:
            tmp = int.from_bytes(fix, "little")
        
        self.data = tmp
    
    def __bytes__(self):
        self.data += 1
        return self.data.to_bytes(12, "little")

    def __repr__(self):
        t = self.data.to_bytes(12, "little")
        return f"{self.__class__.__name__}({t.hex()})"



if __name__ == "__main__":
    from os import urandom

    a = Nonce(urandom(12))
    b = Nonce(urandom(12))
    print(a, b)
    
    while 1:
        tmp = bytes(a)
        bytes(b)
        print(a, b)
