from pathlib import Path
import secrets

base_dir = Path(__file__).parent.parent
key_path = base_dir / "data" / "hmac_secret.key"
key_path.parent.mkdir(exist_ok=True)
with open(key_path, "wb") as f:
    f.write(secrets.token_bytes(32))
print("HMAC key generated.")