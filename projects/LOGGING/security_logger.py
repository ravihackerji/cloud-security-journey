import logging

logging.basicConfig(
    filename="audit.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Cloud Security Audit Started")

logging.info("Scanning IAM Users")

logging.warning("User John has MFA Disabled")

logging.info("Scanning S3 Buckets")

logging.warning("Public Bucket Found: company-backup")

logging.info("Generating Security Report")

logging.info("Cloud Security Audit Completed")

print("Audit completed successfully. Check audit.log")