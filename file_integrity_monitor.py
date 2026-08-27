import hashlib

files_to_monitor = [
    "sample_file.txt",
    "config.txt",
    "security.log"
]

print("FILE INTEGRITY MONITOR")
print("=" * 50)

for file_name in files_to_monitor:

    file = open(file_name, "rb")

    data = file.read()

    file_hash = hashlib.sha256(data).hexdigest()

    print(f"\nFile: {file_name}")
    print(f"SHA256: {file_hash}")

    file.close()
