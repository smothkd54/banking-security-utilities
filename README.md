[![Test](https://github.com/smothkd54/banking-security-utilities/actions/workflows/test.yml/badge.svg)](https://github.com/smothkd54/banking-security-utilities/actions/workflows/test.yml)

# Banking Security Utilities 🔐

A collection of security utilities for banking and financial applications.

## Features
- Cryptographically secure token/key generation using Python's `secrets` module (better than `random`)
- Secure transaction audit logging with HMAC-SHA256 signatures
- HMAC-based ledger integrity verification
- Fernet-based symmetric data encryption (strings and files)
- Key rotation for encrypted data
- Credit card validation (Luhn algorithm)
- PII sanitization (email, phone, account masking with country-aware formatting)
- Password strength evaluation (0-5 score)

## How to Use

```bash
# Clone the repository
git clone https://github.com/smothkd54/banking-security-utilities.git

# Navigate to the project directory
cd banking-security-utilities

# Install the package
pip install -e .

# --- Token & Key Generation ---
# Generate HMAC secret key (first time only)
python -m scripts.setup_key

# Run the secure token generator
python -m scripts.generate_token

# --- Audit Logging ---
# Run the secure transaction audit log
python -m scripts.run_audit

# Validate ledger integrity with HMAC verification
python -m scripts.validate_ledger

# --- Data Encryption ---
# Generate encryption key (first time only)
python -m scripts.encrypt_data genkey

# Encrypt a string
python -m scripts.encrypt_data encrypt "Hello Bank"

# Decrypt a string
python -m scripts.encrypt_data decrypt "gAAAAAB..."

# Encrypt a file
python -m scripts.encrypt_data encrypt-file report.pdf

# Decrypt a file
python -m scripts.encrypt_data decrypt-file data\report.pdf.enc

# Rotate encryption key (re-encrypts all .enc files)
python -m scripts.encrypt_data rotate

# --- Compliance Utilities ---
# Validate credit card number (Luhn algorithm)
python -m scripts.compliance validate-card 4111111111111111

# Sanitize PII
python -m scripts.compliance sanitize-email "john@bank.com"
python -m scripts.compliance sanitize-phone "+1-234-555-7890"
python -m scripts.compliance sanitize-acct "1234567890"

# Check password strength
python -m scripts.compliance check-password "MyP@ssw0rd!"

# --- Testing ---
pip install -e ".[dev]"
pytest tests/ -v
```

## Project Structure

```
banking-security-utilities/
├── src/
│   ├── __init__.py
│   ├── crypto.py          # Token/key generation, hashing, HMAC
│   ├── audit.py           # Secure transaction audit logging
│   ├── validate.py        # Ledger integrity verification
│   ├── encrypt.py         # Fernet encryption, key rotation
│   ├── compliance.py      # Card validation, PII sanitizer, password strength
│   ├── auth.py            # (coming soon)
│   └── monitor.py         # (coming soon)
├── scripts/
│   ├── __init__.py
│   ├── setup_key.py
│   ├── generate_token.py
│   ├── run_audit.py
│   ├── validate_ledger.py
│   ├── encrypt_data.py
│   └── compliance.py
├── data/                  # Runtime files (gitignored)
├── tests/
│   ├── __init__.py
│   ├── test_crypto.py
│   ├── test_validate.py
│   └── test_compliance.py
├── .github/
│   └── workflows/
│       └── test.yml
├── pyproject.toml
├── LICENSE
└── README.md
```

## Example Output

### Secure Token Generator

```
🔐 Banking Security Utilities
Generated on: 2026-05-30 05:10:28

=== SECURE TOKEN GENERATED (32 characters) ===
bc55b1e7798100336d8870759891a472

=== API KEY GENERATED ===
bsu_d26553e7db7d8ced48ba6f87d9e32af1e62b92065086c81f

=== STRONG PASSWORD GENERATED (16 characters) ===
wh2)%HX#D&9qMZJS
✓ Contains uppercase, lowercase, number & special character

=== SECRET KEY GENERATED ===
e0eef682bb9cf97e22c60f3841d5c1ed60ae60264ba087a4365de92b850a0a4b

=== EXAMPLE HASH (SHA-256) ===
5697f67bc0e58b8a8a87d1c1168b99ff10bfa9ec885913db1a4ddd9f477085c9
```

### Secure Transaction Audit Log

```
=== SECURE TRANSACTION LEDGER RECORDED ===
DEPOSIT of $1500.00 for Account ACC-9982
HMAC Signature: 799e4cef805d7d1b

=== SECURE TRANSACTION LEDGER RECORDED ===
WITHDRAWAL of $45.50 for Account ACC-1104
HMAC Signature: e2893b7380a29510
```

### Ledger Integrity Audit (HMAC)

```
Line 1: ✅ VERIFIED (Account ACC-9982)
Line 2: ✅ VERIFIED (Account ACC-1104)
```

### Data Encryption

```
=== ENCRYPTION KEY GENERATED ===
Key saved to data/encryption_key.key

=== ENCRYPTED ===
gAAAAABqGrAbeFJOZ14IA5o85nEUynqHLIDSzUX8DI_VLa-f0lnOYrp_xHdnRkc247I6xqypruCDsz8EQxkXt8Rex4TQZQGdxg==
```

### Compliance

```
=== CARD VALIDATION ===
✅ VALID card number

=== PII SANITIZATION ===
Email: j***@bank.com
Phone: +1 *** *** 7890
Account: ****-7890

=== PASSWORD STRENGTH ===
Rating: Very Strong (5/5)
```

## Security Best Practices
- Token/key generation: `secrets.token_hex(16)` → 32-character hex string, 16 bytes entropy
- Ledger signing: HMAC-SHA256 ensures transaction integrity and tamper detection
- Data encryption: Fernet (AES-128-CBC with HMAC-SHA256)
- Key rotation: all encrypted files re-encrypted on key change
- Key storage: `data/encryption_key.key` and `data/hmac_secret.key` are gitignored

## License
MIT License — see the [LICENSE](LICENSE) file for details.
