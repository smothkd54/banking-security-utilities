from src.audit import write_secure_audit_log

if __name__ == "__main__":
    print("Initializing Connected Banking Services...")
    write_secure_audit_log("ACC-9982", "DEPOSIT", "1500.00")
    write_secure_audit_log("ACC-1104", "WITHDRAWAL", "45.50")
    write_secure_audit_log("ACC-3341", "DEPOSIT", "250.75")
    write_secure_audit_log("ACC-2705", "WITHDRAWAL", "120.00")
    write_secure_audit_log("ACC-5562", "DEPOSIT", "3000.00")
    write_secure_audit_log("ACC-8910", "WITHDRAWAL", "99.99")
    write_secure_audit_log("ACC-1237", "DEPOSIT", "47.25")