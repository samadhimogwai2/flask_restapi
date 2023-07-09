import requests
import json

URL = "http://127.0.0.1:5000"

def main():
    response = requests.get(URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"headers: {response.headers}")
    print(f"content: {json.loads(response.json())}")
    print(f"content type: {type(json.loads(response.json()))}\n")

if __name__ == '__main__':
    main()