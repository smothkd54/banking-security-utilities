from src.compliance import validate_card_number, sanitize_email, sanitize_phone, sanitize_account_number, check_password_strength

def test_validate_card_valid():
    assert validate_card_number("4111111111111111") == True

def test_validate_card_invalid():
    assert validate_card_number("1234567890123456") == False

def test_sanitize_email():
    assert sanitize_email("john@bank.com") == "j***@bank.com"

def test_sanitize_phone():
    assert sanitize_phone("+1-234-555-7890") == "****-7890"

def test_sanitize_acct():
    assert sanitize_account_number("1234567890") == "****-7890"

def test_strong_password():
    result = check_password_strength("MyP@ssw0rd!")
    assert result["score"] >= 4

def test_weak_password():
    result = check_password_strength("hello")
    assert result["score"] <= 2
