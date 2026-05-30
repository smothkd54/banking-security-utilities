import re
import string

def validate_card_number(card_number: str) -> bool:
    """Validate a credit card number using the Luhn algorithm."""
    digits = [int(d) for d in card_number if d.isdigit()]
    if len(digits) < 13 or len(digits) > 19:
        return False
    checksum = 0
    for i, d in enumerate(reversed(digits)):
        n = d * 2 if i % 2 == 1 else d
        checksum += n if n < 10 else n - 9
    return checksum % 10 == 0

def sanitize_email(email: str) -> str:
    """Mask email: user@example.com -> u***@example.com"""
    at_index = email.find("@")
    if at_index == -1:
        return email
    local = email[:at_index]
    domain = email[at_index:]
    return f"{local[0]}***{domain}"

SINGLE_DIGIT_CODES = {"1", "7"}

def sanitize_phone(phone: str) -> str:
    digits = re.sub(r"\D", "", phone)
    if len(digits) < 4:
        return phone
    if phone.strip().startswith("+"):
        code_len = 1 if digits[0] in SINGLE_DIGIT_CODES else 3
        return f"+{digits[:code_len]} *** *** {digits[-4:]}"
    else:
        return f"****-{digits[-4:]}"

def sanitize_account_number(acct: str) -> str:
    """Mask account number: show last 4."""
    digits = re.sub(r"\D", "", acct)
    if len(digits) < 4:
        return acct
    return f"****-{digits[-4:]}"

def check_password_strength(password: str) -> dict:
    """Score password strength (0-5) with feedback."""
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters required")

    if len(password) >= 12:
        score += 1

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Mix uppercase and lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r"[!@#$%^&*()\-_=+\\\]\[{}|;:,.<>/?]", password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    if len(set(password)) >= len(password) * 0.6:
        score += 1
    else:
        feedback.append("Reduce repeated characters")

    rating = ["Very Weak", "Very Weak", "Weak", "Fair", "Strong", "Very Strong"][score]

    return {"score": score, "rating": rating, "feedback": feedback}
