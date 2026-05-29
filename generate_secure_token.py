import secrets

def generate_secure_token():
    # Generates a secure, random hexadecimal string
    secret_key = secrets.token_hex(16)
    print("=== SECURE SERVER KEY GENERATED ===")
    print(secret_key)
    
def generate_api_key():
    """Generate a secure API key with prefix"""
    key = secrets.token_hex(24)
    return f"bsu_{key}"

if __name__ == "__main__":
    generate_secure_token()
    print("\n=== SECURE API KEY GENERATED ===")
    print(generate_api_key())