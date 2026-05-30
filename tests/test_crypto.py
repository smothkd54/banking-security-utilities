 
import pytest
from src.crypto import hmac_sign, generate_secure_token, hash_string

def test_hmac_sign_returns_64_chars():
    sig = hmac_sign("test_data", b"secret_key")
    assert len(sig) == 64
    assert isinstance(sig, str)

def test_generate_secure_token_default_length():
    token = generate_secure_token()
    assert len(token) == 32

def test_hash_string_sha256():
    result = hash_string("hello")
    assert len(result) == 64