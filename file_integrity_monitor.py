import hashlib
import os
from datetime import datetime


def calculate_hash(filename):

    with open(filename, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


files_to_monitor = [
    "sample_file.txt",
    "config.txt",
    "security.log"
]

baseline_file = "baseline_hashes.txt"

current_hashes = {}

for filename in files_to_monitor:

    if os.path.exists(filename):
        current_hashes[filename] = calculate_hash(filename)


# First Run (Create Baseline)
if not os.path.exists(baseline_file):

    with open(baseline_file, "w") as file:

        for filename, file_hash in current_hashes.items():
            file.write(f"{filename}|{file_hash}\n")

    print("Baseline hashes created successfully.")
    print("Run the program again to start monitoring.")

else:

    baseline_hashes = {}

    with open(baseline_file, "r") as file:

        for line in file:

            filename, file_hash = line.strip().split("|")

            baseline_hashes[filename] = file_hash

    modified_files = 0

    print("\nFILE INTEGRITY MONITOR")
    print("=" * 60)

    print("Scan Time :", datetime.now())

    print("=" * 60)

    for filename in files_to_monitor:

        print(f"\nFile: {filename}")

        if not os.path.exists(filename):

            print("Risk Level : HIGH")
            print("ALERT : File Missing")

            modified_files += 1

            continue

        current_hash = current_hashes[filename]

        baseline_hash = baseline_hashes.get(filename)

        file_size = os.path.getsize(filename)

        print(f"Size : {file_size} Bytes")

        if current_hash == baseline_hash:

            print("Status : VERIFIED")
            print("Risk Level : LOW")

        else:

            print("Status : MODIFIED")
            print("Risk Level : HIGH")
            print("ALERT : File Integrity Compromised")

            modified_files += 1

    print("\n" + "=" * 60)

    print("Modified Files :", modified_files)

    if modified_files > 0:

        print("Overall Risk Level : HIGH")
        print("Recommendation : Immediate Investigation Required")

    else:

        print("Overall Risk Level : LOW")
        print("Recommendation : Continue Monitoring")

    print("=" * 60)
