import hashlib
import os

files_to_monitor = [
    "sample_file.txt",
    "config.txt",
    "security.log"
]

BASELINE_FILE = "baseline_hashes.txt"

# ==========================
# Generate SHA256 Hash
# ==========================
def get_file_hash(file_name):

    with open(file_name, "rb") as file:
        data = file.read()

    return hashlib.sha256(data).hexdigest()


# ==========================
# Create Baseline
# ==========================
if not os.path.exists(BASELINE_FILE):

    print("Creating Baseline Hashes...\n")

    baseline = open(BASELINE_FILE, "w")

    for file_name in files_to_monitor:

        file_hash = get_file_hash(file_name)

        baseline.write(f"{file_name}:{file_hash}\n")

        print(f"Baseline Saved -> {file_name}")

    baseline.close()

    print("\nBaseline Created Successfully.")
    print("Run the program again for monitoring.")

# ==========================
# Monitoring Mode
# ==========================
else:

    baseline_hashes = {}

    baseline = open(BASELINE_FILE, "r")

    for line in baseline:

        file_name, file_hash = line.strip().split(":")
        baseline_hashes[file_name] = file_hash

    baseline.close()

    modified_files = 0

    print("\nFILE INTEGRITY MONITOR")
    print("=" * 50)

    for file_name in files_to_monitor:

        current_hash = get_file_hash(file_name)

        print(f"\nFile: {file_name}")

        if current_hash == baseline_hashesprint("Status : SAFE")

        else:
            print("Status : MODIFIED")
            modified_files += 1

    print("\n" + "=" * 50)

    print("Files Checked :", len(files_to_monitor))
    print("Modified Files:", modified_files)

    print("=" * 50)

    if modified_files == 0:
        print("Risk Level : LOW")

    elif modified_files == 1:
        print("Risk Level : MEDIUM")

    else:
        print("Risk Level : HIGH")
