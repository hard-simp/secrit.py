#!/usr/bin/env python3
import gnupg
import os

# Initialize GPG instance
gpg = gnupg.GPG()
_PASSWORD_STORE_PATH = os.path.expanduser("~/.password-store/")

def get(entry_path: str) -> str:
    """Retrieve decrypted content of a password store entry."""
    full_path = os.path.join(_PASSWORD_STORE_PATH, entry_path + ".gpg")

    # Ensure the file exists
    if not os.path.exists(full_path):
        raise FileNotFoundError(f"File not found: {full_path}")

    # Decrypt the file
    with open(full_path, "rb") as f:
        decrypted_data = gpg.decrypt_file(f)
        if not decrypted_data.ok:
            raise ValueError("Failed to decrypt the data")

    return str(decrypted_data).strip()  # Return the decrypted content
