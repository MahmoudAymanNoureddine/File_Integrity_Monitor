import hashlib

files_to_monitor = [
    "sample_file.txt",
    "config.txt",
    "security.log"
]

print("FILE INTEGRITY MONITOR")
print("=" * 60)

baseline_hashes = {}

baseline_file = open("baseline_hashes.txt", "r")

for line in baseline_file:
    file_name, file_hash = line.strip().split(":")
    baseline_hashes[file_name] = file_hash

baseline_file.close()

modified_files = 0

for file_name in files_to_monitor:

    file = open(file_name, "rb")

    data = file.read()

    current_hash = hashlib.sha256(data).hexdigest()

    file.close()

    print(f"\nFile: {file_name}")

    if current_hash == baseline_hashesprint("Status : SAFE")

    else:
        print("Status : MODIFIED")
        modified_files += 1

print("\n" + "=" * 60)

print("Files Checked :", len(files_to_monitor))
print("Modified Files:", modified_files)

print("=" * 60)

if modified_files == 0:
    print("Risk Level : LOW")

elif modified_files == 1:
    print("Risk Level : MEDIUM")

else:
    print("Risk Level : HIGH")
