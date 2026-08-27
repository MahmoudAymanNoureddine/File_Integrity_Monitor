import hashlib


def calculate_hash(filename):

    file = open(filename, "rb")

    content = file.read()

    file.close()

    return hashlib.sha256(content).hexdigest()


baseline_hash = calculate_hash("sample_file.txt")

print("\nFILE INTEGRITY MONITOR")
print("=" * 50)

print("Baseline Hash:")
print(baseline_hash)

print("\nModify the file and press Enter to continue...")
input()

current_hash = calculate_hash("sample_file.txt")

print("\nCurrent Hash:")
print(current_hash)

print("\n" + "=" * 50)

if baseline_hash == current_hash:

    print("STATUS : FILE INTEGRITY VERIFIED")

else:

    print("WARNING : FILE INTEGRITY COMPROMISED")
