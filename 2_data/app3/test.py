import requests
import json

URL = f"http://127.0.0.1:5000"
USER_URL = f"http://127.0.0.1:5000/user"
QUERY_DATA = {'username': "Tatsuki"}

def main():
    
    # Hello World
    response = requests.get(URL, params=QUERY_DATA)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")

    # Uesr
    response = requests.get(USER_URL, params=QUERY_DATA)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")

if __name__ == '__main__':
    main()