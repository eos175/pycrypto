from setuptools import setup, find_packages

# Load dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="pycrypto",
    version="0.1.0",
    description="A high-performance cryptography wrapper for AES and ECC.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eos175/pycrypto",
    author="eos175",
    author_email="eos175@gmail.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Security :: Cryptography",
    ],
)
