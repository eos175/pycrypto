from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = [i.strip() for i in f]


setup(
    name="pycrypto",
    version="0.0.1",
    description="crypto wrapper for aes, ecc",
    url="https://github.com/eos175/pycrypto.git",
    author="eos175",
    author_email="eos175@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    python_requires=">=3.7.0",
    install_requires=requirements
)

