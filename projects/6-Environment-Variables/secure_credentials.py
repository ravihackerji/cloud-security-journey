import os

api_key = os.getenv("API_KEY", "Not Configured")
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID", "Not Configured")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY", "Not Configured")

print("=" * 50)
print("Secure Credential Reader")
print("=" * 50)

print(f"API Key           : {api_key}")
print(f"AWS Access Key    : {aws_access_key}")

if aws_secret_key == "Not Configured":
    print("AWS Secret Key    : Not Configured")
else:
    print("AWS Secret Key    : ************")