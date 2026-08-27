import hashlib


file = open("sample_file.txt", "rb")

content = file.read()

file.close()

file_hash = hashlib.sha256(content).hexdigest()

print("FILE INTEGRITY MONITOR")
print("=" * 40)

print("SHA256 Hash:")
print(file_hash)
