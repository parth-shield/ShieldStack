#!/usr/bin/env python3

import argparse
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec

def save_private_key(private_key, outpath, file_format):
    if file_format == 'pem':
        encoding = serialization.Encoding.PEM
    else:
        encoding = serialization.Encoding.DER

    with open(outpath, 'wb') as f:
        f.write(private_key.private_bytes(
            encoding=encoding,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

def save_public_key(public_key, outpath, file_format):
    if file_format == 'pem':
        encoding = serialization.Encoding.PEM
    else:
        encoding = serialization.Encoding.DER

    with open(outpath, 'wb') as f:
        f.write(public_key.public_bytes(
            encoding=encoding,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def generate_ecc_keypair(curve_name, outdir, file_format):
    print(f"[+] Generating ECC keypair with curve {curve_name}...")

    curve_map = {
        'secp256r1': ec.SECP256R1(),
        'secp384r1': ec.SECP384R1(),
        'secp521r1': ec.SECP521R1(),
    }

    if curve_name not in curve_map:
        raise ValueError(f"Unsupported curve: {curve_name}")

    private_key = ec.generate_private_key(
        curve_map[curve_name],
        backend=default_backend()
    )

    # Save Private Key
    private_path = os.path.join(outdir, f'private_key.{file_format}')
    save_private_key(private_key, private_path, file_format)

    # Save Public Key
    public_key = private_key.public_key()
    public_path = os.path.join(outdir, f'public_key.{file_format}')
    save_public_key(public_key, public_path, file_format)

    print(f"Keys saved to {outdir}")

def generate_rsa_keypair(key_size, outdir, file_format):
    print(f"[+] Generating RSA keypair with size {key_size} bits...")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )

    # Save Private Key
    private_path = os.path.join(outdir, f'private_key.{file_format}')
    save_private_key(private_key, private_path, file_format)

    # Save Public Key
    public_key = private_key.public_key()
    public_path = os.path.join(outdir, f'public_key.{file_format}')
    save_public_key(public_key, public_path, file_format)

    print(f"Keys saved to {outdir}")

def main():
    parser = argparse.ArgumentParser(description='ShieldStack Key Generator')
    parser.add_argument('--algo', type=str, choices=['rsa', 'ecc'], default='rsa', help='Algorithm (rsa or ecc)')
    parser.add_argument('--keysize', type=int, choices=[2048, 4096], default=2048, help='RSA key size (ignored if ECC)')
    parser.add_argument('--curve', type=str, choices=['secp256r1', 'secp384r1', 'secp521r1'], default='secp256r1', help='ECC curve name (if algo=ecc)')
    parser.add_argument('--outdir', type=str, default='.', help='Output directory')
    parser.add_argument('--format', type=str, choices=['pem', 'der'], default='pem', help='Output key format (pem or der)')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    if args.algo == 'rsa':
        generate_rsa_keypair(args.keysize, args.outdir, args.format)
    elif args.algo == 'ecc':
        generate_ecc_keypair(args.curve, args.outdir, args.format)

if __name__ == '__main__':
    main()
