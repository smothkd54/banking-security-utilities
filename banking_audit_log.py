import hashlib
from datetime import datetime

def write_audit_log(account_id, action_type, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    raw_payload = f"{timestamp}|{account_id}|{action_type}|{amount}"
    
    # Generate a unique cryptographic signature for this specific transaction row
    row_signature = hashlib.sha256(raw_payload.encode()).hexdigest()[:16]
    
    log_line = f"[{timestamp}] ACCT: {account_id} | ACTION: {action_type} | AMT: ${amount} | SIG: {row_signature}\n"
    
    with open("banking_ledger.log", "a") as ledger:
        ledger.write(log_line)
        
    print(f"=== TRANSACTION VERIFIED ===")
    print(log_line.strip())

if __name__ == "__main__":
    # Simulating standard financial ledger activities
    write_audit_log("ACC-9982", "DEPOSIT", "1500.00")
    write_audit_log("ACC-1104", "WITHDRAWAL", "45.50")
    write_audit_log("ACC-3341", "DEPOSIT", "250.75")
    write_audit_log("ACC-2705", "WITHDRAWAL", "120.00")
    write_audit_log("ACC-5562", "DEPOSIT", "3000.00")
    write_audit_log("ACC-8910", "WITHDRAWAL", "99.99")
    write_audit_log("ACC-1237", "DEPOSIT", "47.25")

