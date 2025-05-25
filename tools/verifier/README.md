# ShieldStack Verifier Tool

This tool is used to verify digital signatures of firmware or binary files using a public key. It ensures the authenticity and integrity of data — essential for secure boot, OTA updates, and trusted communication.

---

## 🔐 Features

- Verifies signatures created by the [Signer Tool](../signer/)
- Supports **RSA** and **ECC** algorithms
- Works with **PEM** and **DER** key formats
- CLI-friendly, build pipeline ready

---

## ⚙️ Usage

python3 verifier.py --infile <firmware_file> --sig <signature_file> --key <public_key_file> --format <pem|der> --algo <rsa|ecc>

## Example (RSA, PEM format)

python3 verifier.py \
  --infile ../../firmware.bin \
  --sig ../../firmware.sig \
  --key ../../keys/public_key.pem \
  --format pem \
  --algo rsa

## Expected Output

[+] Signature is valid ✅

Or if invalid:

[-] Signature verification failed ❌

## Requirements
Python 3.x

cryptography library (pip install cryptography)

## Output
This tool does not modify any files. It only reports whether the signature is valid.

## Use Case
Secure Boot

Firmware Authenticity Check

## OTA Verification

Anti-Rollback Support (future extension)

## Future Enhancements
X.509 certificate-based verification

## Timestamp support

Authenticated firmware headers

## License
MIT License © Parth

