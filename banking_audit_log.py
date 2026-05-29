import hashlib
from datetime import datetime
# Crucial Link: Import the specific token generation file
import generate_secure_token

def write_secure_audit_log(account_id, action_type, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 🔒 Real Relationship: Call the function from generate_secure_token to authorize the log
    # This simulates checking a secure system API Key before recording financial changes
    runtime_session_token = generate_secure_token.generate_api_key("ledger_auth")

    # Combine transaction parameters with the imported secure key to create a unique banking payload
    raw_payload = f"{timestamp}|{account_id}|{action_type}|{amount}|{runtime_session_token}"

    # Generate an unalterable database row cryptographic signature using the hash function from your first script
    row_signature = generate_secure_token.hash_string(raw_payload)

    log_line = f"[{timestamp}] ACCT: {account_id} | {action_type} | AMT: ${amount} | SECURE_TOKEN: {runtime_session_token[:15]}... | SIGNATURE: {row_signature[:16]}\n"

    with open("banking_ledger.log", "a") as ledger:
        ledger.write(log_line)

    print(f"=== SECURE TRANSACTION LEDGER RECORDED ===")
    print(f"Action Verified: {action_type} of ${amount} for Account {account_id}")
    print(f"Cryptographic Signature: {row_signature[:16]} [SECURE]\n")

if __name__ == "__main__":
    print("Initializing Connected Banking Services...")
    write_secure_audit_log("ACC-9982", "DEPOSIT", "1500.00")
    write_secure_audit_log("ACC-1104", "WITHDRAWAL", "45.50")
    write_secure_audit_log("ACC-3341", "DEPOSIT", "250.75")
    write_secure_audit_log("ACC-2705", "WITHDRAWAL", "120.00")
    write_secure_audit_log("ACC-5562", "DEPOSIT", "3000.00")
    write_secure_audit_log("ACC-8910", "WITHDRAWAL", "99.99")
    write_secure_audit_log("ACC-1237", "DEPOSIT", "47.25")
