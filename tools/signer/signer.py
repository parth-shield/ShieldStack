# tools/signer/signer.py

import argparse
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_der_private_key
from cryptography.hazmat.backends import default_backend

def load_private_key(path, format):
    with open(path, 'rb') as key_file:
        key_data = key_file.read()
        if format == 'pem':
            return load_pem_private_key(key_data, password=None, backend=default_backend())
        elif format == 'der':
            return load_der_private_key(key_data, password=None, backend=default_backend())
        else:
            raise ValueError("Unsupported key format. Use 'pem' or 'der'.")

def sign_file(private_key, data, algo):
    if isinstance(private_key, rsa.RSAPrivateKey):
        return private_key.sign(
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
    elif isinstance(private_key, ec.EllipticCurvePrivateKey):
        return private_key.sign(
            data,
            ec.ECDSA(hashes.SHA256())
        )
    else:
        raise ValueError("Unsupported private key type.")

def main():
    parser = argparse.ArgumentParser(description="ShieldStack Firmware Signer")
    parser.add_argument("--infile", required=True, help="Input file to sign")
    parser.add_argument("--key", required=True, help="Path to private key file")
    parser.add_argument("--format", default="pem", choices=["pem", "der"], help="Key format")
    parser.add_argument("--algo", default="rsa", choices=["rsa", "ecc"], help="Crypto algorithm")
    parser.add_argument("--outfile", default="signature.sig", help="Output signature file")
    args = parser.parse_args()

    # Load data to sign
    with open(args.infile, "rb") as f:
        data = f.read()

    # Load private key
    private_key = load_private_key(args.key, args.format)

    # Sign the file
    signature = sign_file(private_key, data, args.algo)

    # Write the signature
    with open(args.outfile, "wb") as f:
        f.write(signature)

    print(f"[+] File signed successfully. Signature saved to {args.outfile}")

if __name__ == "__main__":
    main()
