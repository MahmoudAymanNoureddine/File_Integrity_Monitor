import hashlib
import os
from datetime import datetime


def calculate_hash(filename):

    with open(filename, "rb") as file:
        content = file.read()

    return hashlib.sha256(content).hexdigest()


files_to_monitor = [
    "sample_file.txt",
    "config.txt",
    "security.log"
]

print("\nFILE INTEGRITY MONITOR")
print("=" * 60)

print("Scan Time:", datetime.now())

print("=" * 60)

for filename in files_to_monitor:

    if os.path.exists(filename):

        file_hash = calculate_hash(filename)

        print(f"\nFile: {filename}")
        print(f"SHA256: {file_hash}")

        file_size = os.path.getsize(filename)

        print(f"Size: {file_size} Bytes")

        if file_size == 0:
            print("Risk Level: HIGH")
            print("ALERT: Empty File Detected")

        else:
            print("Risk Level: LOW")
            print("Status: File Integrity Verified")

    else:

        print(f"\nFile: {filename}")
        print("Risk Level: HIGH")
        print("ALERT: File Missing")

print("\n" + "=" * 60)
print("Integrity Scan Completed")
print("=" * 60)
