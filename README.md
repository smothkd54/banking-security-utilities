# Banking Security Utilities 🔐

A collection of security utilities for banking and financial applications.

## Features
- Secure random token/key generation using Python's `secrets` module
- Cryptographically secure (better than `random` module)
- Suitable for API keys, session tokens, and encryption keys

## How to Use

```bash
# Clone the repository
git clone https://github.com/your-username/banking-security-utilities.git

# Navigate to the project directory
cd banking-security-utilities

# Run the secure token generator
python generate_secure_token.py
```

## Example Output

```
=== SECURE SERVER KEY GENERATED ===
a1b2c3d4e5f67890123456789abcdef0
```

## Security Best Practices
Uses `secrets.token_hex(16)` → 32-character hexadecimal string
16 bytes of entropy (recommended for production use)

## Roadmap
- Add more security utilities (password strength checker, encryption helpers, etc.)

## License
MIT License
