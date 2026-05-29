import os
import re
import generate_secure_token

def verify_ledger_integrity(log_file_path="banking_ledger.log"):
    print("=== BANKING LEDGER INTEGRITY AUDIT (HMAC VERIFICATION) ===")
    print(f"Target file: {log_file_path}\n")
    
    if not os.path.exists(log_file_path):
        print("❌ Ledger file not found!")
        return False
    
    # Load the HMAC key (same as used for logging)
    try:
        key = generate_secure_token.load_hmac_key("hmac_secret.key")
    except FileNotFoundError:
        print("❌ HMAC key file 'hmac_secret.key' not found!")
        return False
    
    tamper_detected = False
    line_number = 0
    
    with open(log_file_path, "r", encoding="utf-8") as f:
        for line in f:
            line_number += 1
            line = line.strip()
            if not line:
                continue
            
            # Parse log line format: [timestamp] ACCT: X | ACTION: Y | AMT: $Z | SIG: hex
            pattern = r'\[(.*?)\]\s+ACCT:\s+(\S+)\s+\|\s+(\w+)\s+\|\s+AMT:\s+\$([\d.]+)\s+\|\s+SIG:\s+(\S+)'
            match = re.match(pattern, line)
            if not match:
                print(f"Line {line_number:2d}: ⚠️  MALFORMED LINE")
                tamper_detected = True
                continue
            
            timestamp, account, action, amount, stored_sig = match.groups()
            payload = f"{timestamp}|{account}|{action}|{amount}"
            computed_sig = generate_secure_token.hmac_sign(payload, key)[:16]
            
            if computed_sig == stored_sig:
                print(f"Line {line_number:2d}: ✅ VERIFIED (Account {account})")
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