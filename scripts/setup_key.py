import secrets
with open("data/hmac_secret.key", "wb") as f:
    f.write(secrets.token_bytes(32))
print("HMAC key generated. Add 'data/hmac_secret.key' to .gitignore")