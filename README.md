# Banking Security Utilities 🔐

A collection of security utilities for banking and financial applications.

## Features
- Secure random token/key generation using Python's `secrets` module
- Cryptographically secure (better than `random` module)
- Suitable for API keys, session tokens, and encryption keys

## How to Use

```bash
# Clone the repository
git clone https://github.com/smothkd54/banking-security-utilities.git

# Navigate to the project directory
cd banking-security-utilities

# Run the secure token generator
python generate_secure_token.py
```

## Example Output

```
=== SECURE SERVER KEY GENERATED ===
Generated on: 2026-05-29 12:23:47

=== SECURE TOKEN GENERATED (32 characters) ===
13df2682fe4573969a3cd6daa5d1aad0

=== API KEY GENERATED ===
bsu_b8824758560be8598fece33943a7ebcb30c1071b00ee7294

=== STRONG PASSWORD GENERATED (16 characters) ===
-OGVSkX%*4LGqQ+3
✓ Contains uppercase, lowercase, number & special character

=== SECRET KEY GENERATED ===
1edd692a8944618499ea2a3c2de38a8c4d8443029a8551dcd2a55f3e2477fa32

=== EXAMPLE HASH (SHA-256) ===
5697f67bc0e58b8a8a87d1c1168b99ff10bfa9ec885913db1a4ddd9f477085c9
```

## Security Best Practices
Uses `secrets.token_hex(16)` → 32-character hexadecimal string
16 bytes of entropy (recommended for production use)

## License
MIT License
