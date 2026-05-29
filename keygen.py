import secrets

def generate_secure_token():
    # Generates a secure, random hexadecimal string
    secret_key = secrets.token_hex(16)
    print("=== SECURE SERVER KEY GENERATED ===")
    print(secret_key)

if __name__ == "__main__":
    generate_secure_token()
