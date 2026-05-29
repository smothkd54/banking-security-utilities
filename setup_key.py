import secrets
with open("hmac_secret.key", "wb") as f:
    f.write(secrets.token_bytes(32))
print("HMAC key generated. Add 'hmac_secret.key' to .gitignore")