import base64
from pathlib import Path
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key() -> bytes:
    """Generate a new Fernet key."""
    key = Fernet.generate_key()
    print("=== ENCRYPTION KEY GENERATED ===")
    return key

def encrypt_data(data: str, key: bytes) -> str:
    """Encrypt a string using Fernet symmetric encryption."""
    f = Fernet(key)
    token = f.encrypt(data.encode())
    return token.decode()

def decrypt_data(token: str, key: bytes) -> str:
    """Decrypt a Fernet-encrypted token back to the original string."""
    f = Fernet(key)
    data = f.decrypt(token.encode())
    return data.decode()