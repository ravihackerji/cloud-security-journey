import requests

url = "https://api.github.com"

headers = {
    "Authorization": "Bearer YOUR_DEMO_TOKEN"
}

try:
    response = requests.get(url, headers=headers, timeout=10)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        print("Authentication request completed successfully.")
    elif response.status_code == 401:
        print("Authentication failed.")
    elif response.status_code == 403:
        print("Access forbidden.")
    else:
        print("Unexpected response received.")

except requests.exceptions.RequestException as error:
    print(f"Connection Error: {error}")