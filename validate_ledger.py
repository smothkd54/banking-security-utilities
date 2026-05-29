import os
import generate_secure_token

def parse_log_line(line: str):
    """Extract fields from a log line and return dict, or None if malformed."""
    # Expected format:
    # [timestamp] ACCT: ACC-XXXX | ACTION: DEPOSIT/WITHDRAWAL | AMT: $123.45 | SECURE_TOKEN: xxxx | SIGNATURE: xxxx
    try:
        # Split by " | "
        parts = line.strip().split(" | ")
        if len(parts) != 4:   # [timestamp+ACCT], ACTION, AMT, SECURE_TOKEN+SIGNATURE
            return None
        
        # First part contains timestamp and account
        first = parts[0]
        # Extract timestamp (between [ and ])
        timestamp = first.split("]")[0].strip("[")
        account = first.split("ACCT:")[1].strip()
        
        # Action
        action = parts[1].replace("ACTION:", "").strip()
        
        # Amount
        amount = parts[2].replace("AMT: $", "").strip()
        
        # Last part: SECURE_TOKEN: ... | SIGNATURE: ...
        last = parts[3]
        token_part = last.split("|")[0].replace("SECURE_TOKEN:", "").strip()
        sig_part = last.split("SIGNATURE:")[1].strip()
        
        return {
            "timestamp": timestamp,
            "account": account,
            "action": action,
            "amount": amount,
            "token": token_part,
            "signature": sig_part
        }
    except Exception:
        return None

def verify_ledger_integrity(log_file_path="banking_ledger.log"):
    print("=== BANKING LEDGER INTEGRITY AUDIT (FULL VERIFICATION) ===")
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
            
            parsed = parse_log_line(line)
            if not parsed:
                print(f"Line {line_number:2d}: ⚠️  MALFORMED LINE")
                tamper_detected = True
                continue
            
            # Rebuild the exact raw payload that was originally hashed
            # Must match the format in write_secure_audit_log:
            # f"{timestamp}|{account_id}|{action_type}|{amount}|{runtime_session_token}"
            raw_payload = f"{parsed['timestamp']}|{parsed['account']}|{parsed['action']}|{parsed['amount']}|{parsed['token']}"
            
            # Recompute signature (first 16 chars, as stored)
            computed_sig = generate_secure_token.hash_string(raw_payload)[:16]
            stored_sig = parsed['signature'][:16]   # just in case longer
            
            if computed_sig == stored_sig:
                print(f"Line {line_number:2d}: ✅ VERIFIED (Account {parsed['account']})")
            else:
                print(f"Line {line_number:2d}: 🚨 TAMPERED! Computed {computed_sig} vs stored {stored_sig}")
                tamper_detected = True
    
    print("\n" + "="*65)
    if not tamper_detected:
        print("🎉 LEDGER INTEGRITY CONFIRMED – All signatures match.")
    else:
        print("⚠️  INTEGRITY VIOLATION – Some records have been altered.")
    
    return not tamper_detected

if __name__ == "__main__":
    verify_ledger_integrity()