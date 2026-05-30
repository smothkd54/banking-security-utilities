import secrets
import hashlib
import string
import hmac

def hmac_sign(data: str, key: bytes, algorithm=hashlib.sha256) -> str:
    """Return HMAC hex digest of data using given key and hash algorithm."""
    return hmac.new(key, data.encode(), algorithm).hexdigest()

def generate_secure_token(length: int = 32) -> str:
    """Generate a cryptographically secure random token."""
    token = secrets.token_hex(length // 2)
    print(f"=== SECURE TOKEN GENERATED ({length} characters) ===")
    print(token)
    return token

def generate_api_key(prefix: str = "bsu") -> str:
    """Generate a secure API key with custom prefix."""
    key = secrets.token_hex(24)
    api_key = f"{prefix}_{key}"
    print(f"\n=== API KEY GENERATED ===")
    print(api_key)
    return api_key

def generate_strong_password(length: int = 16) -> str:
    """Generate a strong password that meets banking complexity requirements."""
    if length < 12:
        length = 12
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()-_=+"
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]
    alphabet = lowercase + uppercase + digits + special
    password.extend(secrets.choice(alphabet) for _ in range(length - 4))
    secrets.SystemRandom().shuffle(password)
    final_password = ''.join(password)
    print(f"\n=== STRONG PASSWORD GENERATED ({length} characters) ===")
    print(final_password)
    print("✓ Contains uppercase, lowercase, number & special character")
    return final_password

def generate_secret_key() -> str:
    """Generate a high-entropy secret key (suitable for web frameworks)."""
    key = secrets.token_hex(32)
    print(f"\n=== SECRET KEY GENERATED ===")
    print(key)
    return key

def load_hmac_key(key_path="data/hmac_secret.key") -> bytes:
    with open(key_path, "rb") as f:
        return f.read()

def hash_string(data: str, algorithm: str = "sha256") -> str:
    """Hash a string using SHA-256 or SHA-512."""
    if algorithm == "sha512":
        return hashlib.sha512(data.encode('utf-8')).hexdigest()
    return hashlib.sha256(data.encode('utf-8')).hexdigest()