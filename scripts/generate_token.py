from src.crypto import generate_secure_token, generate_api_key, generate_strong_password, generate_secret_key, hash_string
from datetime import datetime

if __name__ == "__main__":
    print("🔐 Banking Security Utilities")
    print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    generate_secure_token(32)
    generate_api_key("bsu")
    generate_strong_password(16)
    generate_secret_key()
    print("\n=== EXAMPLE HASH (SHA-256) ===")
    print(hash_string("BankingSecure2026!"))