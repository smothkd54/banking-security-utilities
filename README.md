# Banking Security Utilities 🔐

A collection of security utilities for banking and financial applications.

## Features
- Secure random token/key generation using Python's `secrets` module
- Cryptographically secure (better than `random` module)
- Suitable for API keys, session tokens, and encryption keys
- Secure transaction audit logging with cryptographic signatures

## How to Use

```bash
# Clone the repository
git clone https://github.com/smothkd54/banking-security-utilities.git

# Navigate to the project directory
cd banking-security-utilities

# Run the secure token generator
python generate_secure_token.py

# Run the secure transaction audit log
python banking_audit_log.py
```

## Example Output

### Secure Token Generator

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

### Secure Transaction Audit Log

```
=== API KEY GENERATED ===
ledger_auth_01039c3ba9b48f404757297a363ebe26364e21698fddbdc0
=== SECURE TRANSACTION LEDGER RECORDED ===
Action Verified: DEPOSIT of $1500.00 for Account ACC-9982
Cryptographic Signature: e6130a77d7fa7b3e [SECURE]

=== API KEY GENERATED ===
ledger_auth_0e41aba3a0ba9c9348740f43f930147f32a2a60bc9884b2d
=== SECURE TRANSACTION LEDGER RECORDED ===
Action Verified: WITHDRAWAL of $45.50 for Account ACC-1104
Cryptographic Signature: 08aefc8d0092ca35 [SECURE]

=== API KEY GENERATED ===
ledger_auth_a8b09845daea65f745d0e7e524d1f0ae8762b3708bf41132
=== SECURE TRANSACTION LEDGER RECORDED ===
Action Verified: DEPOSIT of $250.75 for Account ACC-3341
Cryptographic Signature: c5f283050b9c4cf1 [SECURE]

=== API KEY GENERATED ===
ledger_auth_07dba9369979ab2a83d99c55b74b899390a63e769572ead4
=== SECURE TRANSACTION LEDGER RECORDED ===
Action Verified: WITHDRAWAL of $120.00 for Account ACC-2705
Cryptographic Signature: 32cd56fabbc967a0 [SECURE]

=== API KEY GENERATED ===
ledger_auth_9be7bbac105b21ad3ca4df4c0ba2901c8d7abfc11ddd1a7a
=== SECURE TRANSACTION LEDGER RECORDED ===
Action Verified: DEPOSIT of $3000.00 for Account ACC-5562
Cryptographic Signature: 8f1ab768f423a2d8 [SECURE]

=== API KEY GENERATED ===
ledger_auth_d2a693b8069e05413fc395376c35c8dce10a406eaf839f74
=== SECURE TRANSACTION LEDGER RECORDED ===
Action Verified: WITHDRAWAL of $99.99 for Account ACC-8910
Cryptographic Signature: dda360ba8fda7e5d [SECURE]

=== API KEY GENERATED ===
ledger_auth_df188f2daeb966f79ccaffb960476adcdf316e9e1cab81ba
=== SECURE TRANSACTION LEDGER RECORDED ===
Action Verified: DEPOSIT of $47.25 for Account ACC-1237
Cryptographic Signature: 39051f2d8b24d269 [SECURE]
```

## Security Best Practices
Uses `secrets.token_hex(16)` → 32-character hexadecimal string
16 bytes of entropy (recommended for production use)

## License
MIT License — see the [LICENSE](LICENSE) file for details.
