# tools/verifier/verifier.py

import argparse
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec, padding, rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_der_public_key
from cryptography.hazmat.backends import default_backend

def load_public_key(path, format):
    with open(path, 'rb') as key_file:
        key_data = key_file.read()
        if format == 'pem':
            return load_pem_public_key(key_data, backend=default_backend())
        elif format == 'der':
            return load_der_public_key(key_data, backend=default_backend())
        else:
            raise ValueError("Unsupported key format. Use 'pem' or 'der'.")

def verify_signature(public_key, data, signature):
    if isinstance(public_key, rsa.RSAPublicKey):
        public_key.verify(
            signature,
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
    elif isinstance(public_key, ec.EllipticCurvePublicKey):
        public_key.verify(
            signature,
            data,
            ec.ECDSA(hashes.SHA256())
        )
    else:
        raise ValueError("Unsupported public key type.")

def main():
    parser = argparse.ArgumentParser(description="ShieldStack Verifier Tool")
    parser.add_argument("--infile", required=True, help="Input file to verify")
    parser.add_argument("--sig", required=True, help="Signature file")
    parser.add_argument("--key", required=True, help="Public key file")
    parser.add_argument("--format", default="pem", choices=["pem", "der"], help="Key format")
    parser.add_argument("--algo", default="rsa", choices=["rsa", "ecc"], help="Crypto algorithm")
    args = parser.parse_args()

    with open(args.infile, "rb") as f:
        data = f.read()

    with open(args.sig, "rb") as f:
        signature = f.read()

    public_key = load_public_key(args.key, args.format)

    try:
        verify_signature(public_key, data, signature)
        print("[+] Signature is valid ✅")
    except Exception as e:
        print("[-] Signature verification failed ❌")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

