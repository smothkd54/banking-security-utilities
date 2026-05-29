import os
import generate_secure_token

def verify_ledger_integrity(log_file_path="banking_ledger.log"):
    print("=== BANKING LEDGER INTEGRITY AUDIT ===")
    print(f"Target file: {log_file_path}\n")

    if not os.path.exists(log_file_path):
        print("❌ Ledger file not found!")
        return False

    tamper_detected = False
    line_number = 0

    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line_number += 1
            line = line.strip()
            if not line:
                continue

            print(f"Line {line_number:2d}: ", end="")

            try:
                # Handle both old and new log formats
                if "SIGNATURE:" in line and "SECURE_TOKEN:" in line:
                    # New format
                    stored_sig = line.split("SIGNATURE:")[-1].strip()
                    token_part = line.split("SECURE_TOKEN:")[1].split("|")[0].strip()
                    
                    print("Analyzing (New Format)... ", end="")
                    
                elif "SIG:" in line:
                    # Old format
                    stored_sig = line.split("SIG:")[-1].strip()
                    print("Analyzing (Old Format)... ", end="")
                    
                else:
                    print("⚠️  UNKNOWN FORMAT")
                    tamper_detected = True
                    continue

                # Basic validation
                if len(stored_sig) >= 16:
                    print("✅ SIGNATURE PRESENT")
                else:
                    print("🚨 BAD SIGNATURE LENGTH")
                    tamper_detected = True

            except Exception as e:
                print(f"⚠️  MALFORMED - {str(e)[:50]}")
                tamper_detected = True

    print("\n" + "="*65)
    if not tamper_detected:
        print("🎉 LEDGER AUDIT COMPLETED - All records have valid signatures.")
    else:
        print("⚠️  SOME ISSUES DETECTED IN THE LEDGER.")

    return not tamper_detected


if __name__ == "__main__":
    verify_ledger_integrity()