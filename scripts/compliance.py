import sys
from src.compliance import validate_card_number, sanitize_email, sanitize_phone, sanitize_account_number, check_password_strength

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None

    if cmd == "validate-card" and len(sys.argv) > 2:
        result = validate_card_number(sys.argv[2])
        print(f"{'✅ VALID' if result else '❌ INVALID'} card number")

    elif cmd == "sanitize-email" and len(sys.argv) > 2:
        print(sanitize_email(sys.argv[2]))

    elif cmd == "sanitize-phone" and len(sys.argv) > 2:
        print(sanitize_phone(sys.argv[2]))

    elif cmd == "sanitize-acct" and len(sys.argv) > 2:
        print(sanitize_account_number(sys.argv[2]))

    elif cmd == "check-password" and len(sys.argv) > 2:
        result = check_password_strength(sys.argv[2])
        print(f"Rating: {result['rating']} ({result['score']}/5)")
        if result['feedback']:
            print("Improvements:")
            for fb in result['feedback']:
                print(f"  - {fb}")

    else:
        print("Usage: python -m scripts.compliance <command> [args]")
        print("  validate-card <number>")
        print("  sanitize-email <email>")
        print("  sanitize-phone <phone>")
        print("  sanitize-acct <account>")
        print("  check-password <password>")
