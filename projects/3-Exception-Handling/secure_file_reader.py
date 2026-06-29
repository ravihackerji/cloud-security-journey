import logging
import csv

logging.basicConfig(
    filename="error.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

try:
    with open("users.csv", "r") as file:
        reader = csv.DictReader(file)

        print("Users in File:\n")

        for row in reader:
            print(row["User"], "-", row["MFA"])

        logging.info("File processed successfully.")

except FileNotFoundError:
    print("Error: users.csv not found.")
    logging.error("users.csv file not found.")

except Exception as error:
    print(f"Unexpected Error: {error}")
    logging.error(f"Unexpected Error: {error}")

finally:
    print("\nProgram Finished.")
    logging.info("Program Finished.")