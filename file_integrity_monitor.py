import hashlib
import os
import json
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


# Create Baseline
if not os.path.exists(baseline_file):

    with open(baseline_file, "w") as file:

        for filename, file_hash in current_hashes.items():
            file.write(f"{filename}|{file_hash}\n")

    print("Baseline created successfully.")
    print("Run the program again to start monitoring.")

else:

    baseline_hashes = {}

    with open(baseline_file, "r") as file:

        for line in file:

            filename, file_hash = line.strip().split("|")

            baseline_hashes[filename] = file_hash

    scan_time = str(datetime.now())

    modified_files = 0
    missing_files = 0

    report_lines = []
    json_report = []

    print("\nFILE INTEGRITY MONITOR")
    print("=" * 70)
    print("Scan Time :", scan_time)
    print("=" * 70)

    report_lines.append("FILE INTEGRITY MONITOR")
    report_lines.append("=" * 70)
    report_lines.append(f"Scan Time : {scan_time}")
    report_lines.append("=" * 70)

    for filename in files_to_monitor:

        print(f"\nFile: {filename}")

        if not os.path.exists(filename):

            print("Status      : MISSING")
            print("Risk Level  : HIGH")
            print("Alert       : File Missing")

            modified_files += 1
            missing_files += 1

            json_report.append({
                "file": filename,
                "status": "MISSING",
                "risk_level": "HIGH",
                "timestamp": scan_time
            })

            continue

        current_hash = current_hashes[filename]
        baseline_hash = baseline_hashes.get(filename)

        file_size = os.path.getsize(filename)

        print("Size        :", file_size, "Bytes")
        print("Current Hash:", current_hash)

        if current_hash == baseline_hash:

            status = "VERIFIED"
            risk_level = "LOW"

            print("Status      :", status)
            print("Risk Level  :", risk_level)

        else:

            status = "MODIFIED"
            risk_level = "HIGH"

            print("Status      :", status)
            print("Risk Level  :", risk_level)
            print("Alert       : File Integrity Compromised")

            print("\nPrevious Hash:")
            print(baseline_hash)

            print("\nCurrent Hash:")
            print(current_hash)

            modified_files += 1

        report_lines.append(f"\nFile: {filename}")
        report_lines.append(f"Status: {status}")
        report_lines.append(f"Risk Level: {risk_level}")

        json_report.append({
            "file": filename,
            "status": status,
            "risk_level": risk_level,
            "previous_hash": baseline_hash,
            "current_hash": current_hash,
            "timestamp": scan_time
        })

    print("\n" + "=" * 70)

    print("SCAN SUMMARY")

    print("=" * 70)

    print("Files Monitored :", len(files_to_monitor))
    print("Modified Files  :", modified_files)
    print("Missing Files   :", missing_files)

    if modified_files > 0:

        overall_risk = "HIGH"
        recommendation = "Immediate Investigation Required"

    else:

        overall_risk = "LOW"
        recommendation = "Continue Monitoring"

    print("\nOverall Risk Level :", overall_risk)
    print("Recommendation     :", recommendation)

    print("=" * 70)

    report_lines.append("\nSCAN SUMMARY")
    report_lines.append(f"Files Monitored: {len(files_to_monitor)}")
    report_lines.append(f"Modified Files: {modified_files}")
    report_lines.append(f"Missing Files: {missing_files}")
    report_lines.append(f"Overall Risk Level: {overall_risk}")
    report_lines.append(f"Recommendation: {recommendation}")

    # Save Text Report
    with open("security_report.txt", "w") as file:

        for line in report_lines:
            file.write(line + "\n")

    # Save JSON Report
    with open("security_report.json", "w") as file:

        json.dump(json_report, file, indent=4)

    print("\nSecurity Report Saved:")
    print("security_report.txt")

    print("\nJSON Report Saved:")
    print("security_report.json")
