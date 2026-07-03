import requests

URL = "https://api.github.com"

try:
    response = requests.get(URL, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("=" * 50)
        print("GitHub Public API Dashboard")
        print("=" * 50)
        print(f"Current User URL : {data['current_user_url']}")
        print(f"Repository URL   : {data['repository_url']}")
        print(f"Issues URL       : {data['issues_url']}")
        print(f"Status Code      : {response.status_code}")
    else:
        print(f"Request Failed with Status Code: {response.status_code}")

except requests.exceptions.RequestException as error:
    print(f"API Connection Error: {error}")