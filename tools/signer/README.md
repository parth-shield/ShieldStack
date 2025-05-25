# ShieldStack Signer Tool

This tool is used to digitally sign input files (e.g., firmware binaries) using RSA or ECC private keys. It is a critical part of secure boot chains and firmware authenticity verification.

---

## ✨ Features

- Supports **RSA** and **ECC** private key signing
- Handles keys in **PEM** and **DER** formats
- Outputs raw binary signature file (`.sig`)
- CLI interface for integration into build pipelines

---

## 📦 Usage

### 🔧 Command-line arguments

python3 signer.py --infile <input_file> --key <private_key_file> --format <pem|der> --algo <rsa|ecc> --outfile <signature_file>

## Example (RSA, PEM format)

echo "test firmware" > firmware.bin

python3 signer.py \
  --infile firmware.bin \
  --key ../../keys/private_key.pem \
  --format pem \
  --algo rsa \
  --outfile firmware.sig

## Output

Signed file: firmware.sig

Use with the verifier tool (coming soon) to validate the signature with the public key.

## Requirements

Python 3.x

cryptography package (install via pip install cryptography)

## Important Notes

Never share private keys. Keep them offline and secure.

For production use, always use secure key storage (HSM/TPM) and authenticated firmware channels.

## Future Enhancements

CMS/PKCS#7 or COSE signature support

Embedded signature format (for combining firmware + signature)

Certificate-based signature chains

## License

MIT License © Parth
