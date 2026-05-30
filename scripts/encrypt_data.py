import sys
from pathlib import Path
from src.encrypt import generate_key, encrypt_data, decrypt_data, encrypt_file, decrypt_file


base_dir = Path(__file__).parent.parent
key_path = base_dir / "data" / "encryption_key.key"

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None

    if cmd == "genkey":
        key = generate_key()
        key_path.parent.mkdir(exist_ok=True)
        key_path.write_bytes(key)
        print(f"Key saved to {key_path}")

    elif cmd == "encrypt":
        key = key_path.read_bytes()
        result = encrypt_data(sys.argv[2], key)
        print(result)

    elif cmd == "decrypt":
        key = key_path.read_bytes()
        result = decrypt_data(sys.argv[2], key)
        print(result)

    elif cmd == "encrypt-file":
        key = key_path.read_bytes()
        result = encrypt_file(sys.argv[2], key)
        print(f"Saved to {result}")

    elif cmd == "decrypt-file":
        key = key_path.read_bytes()
        result = decrypt_file(sys.argv[2], key)
        print(f"Saved to {result}")

    else:
        print("Usage: python -m scripts.encrypt_data <genkey|encrypt|decrypt> [data]")