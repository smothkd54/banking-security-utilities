from datetime import datetime
from .crypto import load_hmac_key, hmac_sign

def write_secure_audit_log(account_id, action_type, amount):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = load_hmac_key("data/hmac_secret.key")
    payload = f"{timestamp}|{account_id}|{action_type}|{amount}"
    full_sig = hmac_sign(payload, key)
    short_sig = full_sig[:16]
    log_line = f"[{timestamp}] ACCT: {account_id} | {action_type} | AMT: ${amount} | SIG: {short_sig}\n"
    with open("data/banking_ledger.log", "a") as ledger:
        ledger.write(log_line)
    print(f"=== SECURE TRANSACTION LEDGER RECORDED ===")
    print(f"{action_type} of ${amount} for Account {account_id}")
    print(f"HMAC Signature: {short_sig}\n")