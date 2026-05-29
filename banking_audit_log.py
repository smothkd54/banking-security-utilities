from datetime import datetime
import generate_secure_token

def write_secure_audit_log(account_id, action_type, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Now this works – the function exists in the module
    key = generate_secure_token.load_hmac_key("hmac_secret.key")
    payload = f"{timestamp}|{account_id}|{action_type}|{amount}"
    full_sig = generate_secure_token.hmac_sign(payload, key)
    short_sig = full_sig[:16]
    
    log_line = f"[{timestamp}] ACCT: {account_id} | {action_type} | AMT: ${amount} | SIG: {short_sig}\n"
    
    with open("banking_ledger.log", "a") as ledger:
        ledger.write(log_line)
    
    print(f"=== SECURE TRANSACTION LEDGER RECORDED ===")
    print(f"{action_type} of ${amount} for Account {account_id}")
    print(f"HMAC Signature: {short_sig}\n")

if __name__ == "__main__":
    print("Initializing Connected Banking Services...")
    write_secure_audit_log("ACC-9982", "DEPOSIT", "1500.00")
    write_secure_audit_log("ACC-1104", "WITHDRAWAL", "45.50")
    write_secure_audit_log("ACC-3341", "DEPOSIT", "250.75")
    write_secure_audit_log("ACC-2705", "WITHDRAWAL", "120.00")
    write_secure_audit_log("ACC-5562", "DEPOSIT", "3000.00")
    write_secure_audit_log("ACC-8910", "WITHDRAWAL", "99.99")
    write_secure_audit_log("ACC-1237", "DEPOSIT", "47.25")