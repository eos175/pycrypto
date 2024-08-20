# PyCrypto

> A fast cryptography library by [eos175](https://github.com/eos175)

**PyCrypto** leverages [pycryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html) for AES and [fastecdsa](https://github.com/AntonKueltz/fastecdsa) for ECC. These packages are written in `C` and benefit from hardware acceleration.

## Installation

```bash
sudo dnf install python-devel gmp-devel
```

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install https://github.com/eos175/pycrypto.git
```

## API

### AES

```python
def cfb128_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes: ...
def cfb128_decrypt(data: bytes, key: bytes, iv: bytes) -> bytes: ...

def gcm_encrypt(data: bytes, key: bytes, nonce: bytes) -> bytes: ...
def gcm_decrypt(data: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes | None: ...

def ccm_encrypt(data: bytes, key: bytes, nonce: bytes) -> bytes: ...
def ccm_decrypt(data: bytes, key: bytes, nonce: bytes, tag: bytes) -> bytes | None: ...
```

## TODO

- [ ] Add the rest of the API to the README
- [x] Create setup
