 
import os
from pathlib import Path
from src.crypto import hmac_sign, load_hmac_key
from src.validate import verify_ledger_integrity

def test_verify_integrity_on_log(tmp_path):
    # Setup
    log = tmp_path / "banking_ledger.log"
    log.write_text("line that won't match pattern\n")
    # Will fail to parse → returns False
    assert verify_ledger_integrity(str(log)) == False