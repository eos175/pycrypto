# PyCrypto

> rapida lib para criptografia by [eos175](https://github.com/eos175)

**PyCrypto** usa [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html) para AES y [fastecdsa](https://github.com/AntonKueltz/fastecdsa) para ECC. Estos paquetes estan escrito en `C` y tiene *hw acceleration*


## Installation

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install git+ssh://git@github.com/eos175/pycrypto.git
```

## API


AES


```python

def cfb128_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes: ...
def cfb128_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes: ...

def gcm_encrypt(data: bytes, key: bytes, nonce: bytes) -> bytes:
def gcm_decrypt(data: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes or None: ...

def ccm_encrypt(data: bytes, key: bytes, nonce: bytes) -> bytes: ...
def ccm_decrypt(data: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes or None: ...

```


## ToDo

- [ ] agregar el resto de la API al readme
- [x] crear setup
