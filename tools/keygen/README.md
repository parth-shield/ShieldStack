# ShieldStack Keygen Tool

A simple command-line tool to generate cryptographic key pairs (RSA & ECC) for ShieldStack — your embedded security platform.

---

## Features

- Generate **RSA** keys (2048 or 4096 bits)
- Generate **ECC** keys with popular curves (`secp256r1`, `secp384r1`, `secp521r1`)
- Save keys in **PEM** or **DER** format for compatibility with embedded devices and software
- Easy CLI usage for quick key generation

---

## Requirements

- Python 3.6+
- [cryptography](https://cryptography.io/en/latest/) library

Install dependencies using:

pip install cryptography

## Usage

- python keygen.py --algo rsa --keysize 2048 --format pem --outdir keys_rsa/
- python keygen.py --algo ecc --curve secp384r1 --format der --outdir keys_ecc/


## Command-line Arguments

Argument	Description			Default		Choices
--algo		Algorithm to use		rsa		rsa, ecc
--keysize	RSA key size (ignored if ECC)	2048		2048, 4096
--curve		ECC curve name (ignored if RSA)	secp256r1	secp256r1, secp384r1, secp521r1
--format	Output key format		pem		pem, der
--outdir	Output directory for keys	.		Any valid path

## Output

Keys will be saved as:

Private key: private_key.pem or private_key.der
Public key: public_key.pem or public_key.der

depending on your chosen format and output directory.

## Example

Generate 4096-bit RSA keys in PEM format:

python keygen.py --algo rsa --keysize 4096 --format pem --outdir keys_4096/

Generate ECC keys with curve secp521r1 in DER format:

python keygen.py --algo ecc --curve secp521r1 --format der --outdir keys_ecc_der/

License
MIT License © Parth
