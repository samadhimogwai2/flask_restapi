import requests
import json

URL = "http://127.0.0.1:5000"
USER_URL = "http://127.0.0.1:5000/user"

def main():
    # URL
    response = requests.get(URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")

    # USER_URL
    response = requests.get(USER_URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")

if __name__ == '__main__':
    main()