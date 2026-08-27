import hashlib

files_to_monitor = [
    "sample_file.txt",
    "config.txt",
    "security.log"
]

current_hashes = []

print("FILE INTEGRITY MONITOR")
print("=" * 50)

for file_name in files_to_monitor:

    file = open(file_name, "rb")

    data = file.read()

    file_hash = hashlib.sha256(data).hexdigest()

    current_hashes.append(f"{file_name}:{file_hash}")

    print(f"\nFile: {file_name}")
    print(f"SHA256: {file_hash}")

    file.close()

baseline_file = open("baseline_hashes.txt", "w")

for item in current_hashes:
    baseline_file.write(item + "\n")

baseline_file.close()

print("\nBaseline Hashes Saved Successfully.")
