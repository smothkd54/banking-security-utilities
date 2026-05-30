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

def encrypt_file(input_path: str, key: bytes, output_dir: str = "data") -> str:
    """Encrypt a file and save the .enc copy to output_dir."""
    f = Fernet(key)
    data = Path(input_path).read_bytes()
    token = f.encrypt(data)
    output_name = Path(input_path).name + ".enc"
    output_path = Path(output_dir) / output_name
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_bytes(token)
    print(f"Encrypted → {output_path}")
    return str(output_path)

def decrypt_file(enc_path: str, key: bytes, output_dir: str = "data") -> str:
    """Decrypt a .enc file back to its original form."""
    f = Fernet(key)
    data = Path(enc_path).read_bytes()
    plaintext = f.decrypt(data)
    original_name = Path(enc_path).stem  # strips .enc
    output_path = Path(output_dir) / original_name
    output_path.write_bytes(plaintext)
    print(f"Decrypted → {output_path}")
    return str(output_path)