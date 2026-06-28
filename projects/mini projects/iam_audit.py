import csv

input_file = "users.csv"
output_file = "mfa_report.csv"

disabled_users = []

print("=" * 50)
print("AWS IAM MFA Audit Report")
print("=" * 50)

with open(input_file, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["MFA"] == "Disabled":
            disabled_users.append(row)

print("\nUsers with MFA Disabled:\n")

for user in disabled_users:
    print(f"- {user['User']}")

print(f"\nTotal Users without MFA: {len(disabled_users)}")

with open(output_file, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["User", "MFA"])

    writer.writeheader()

    writer.writerows(disabled_users)

print(f"\nReport Generated Successfully: {output_file}")