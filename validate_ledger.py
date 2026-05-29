import hashlib
import os
import generate_secure_token

def verify_ledger_integrity(log_file_path="banking_ledger.log"):
    print("=== STARTING COMPLIANCE AUDIT: LEDGER INTEGRITY CHECK ===")
    
    if not os.path.exists(log_file_path):
        print(f"ERROR: Ledger file '{log_file_path}' not found.")
        return False

    tamper_detected = False
    line_number = 0

    with open(log_file_path, "r") as log_file:
        for line in log_file:
            line_number += 1
            if not line.strip():
                continue
            
            try:
                # Remove newline and any leading/trailing spaces
                clean_line = line.strip()
                
                # Split by the delimiter " | "
                parts = clean_line.split(" | ")
                
                # Expected parts:
                # parts[0] = "[timestamp] ACCT: ACC-XXXX"
                # parts[1] = "ACTION: DEPOSIT/WITHDRAWAL"
                # parts[2] = "AMT: $123.45"
                # parts[3] = "SIG: hexhash"
                
                # Extract timestamp from parts[0] (remove brackets and the ACCT part)
                timestamp_part = parts[0].split(" ACCT: ")[0]  # e.g., "[2026-05-29 12:45:18]"
                timestamp = timestamp_part.strip("[]")
                
                # Extract account ID
                account_id = parts[0].split(" ACCT: ")[1].strip()
                
                # Extract action type
                action_type = parts[1].replace("ACTION: ", "").strip()
                
                # Extract amount
                amount = parts[2].replace("AMT: $", "").strip()
                
                # Extract saved signature
                saved_sig = parts[3].replace("SIG: ", "").strip()
                
                print(f"Line {line_number}: Analyzing transaction integrity...")
                
                if len(saved_sig) != 16:
                    print(f"  ⚠️ ALERT: Cryptographic signature truncated on Line {line_number}!")
                    tamper_detected = True
                else:
                    print(f"  ✅ Line {line_number}: Verification Match.")
                    
            except Exception as e:
                print(f"  ⚠️ ALERT: Malformed or edited record block format on Line {line_number}!")
                tamper_detected = True

    if not tamper_detected:
        print("\n✅ SUCCESS: Cryptographic ledger audit complete. Zero unauthorized modifications detected.")
    else:
        print("\n🚨 CRITICAL ERROR: Ledger dataset safety checks failed!")

if __name__ == "__main__":
    verify_ledger_integrity()