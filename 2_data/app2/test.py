import requests
import json

param = 1
URL = f"http://127.0.0.1:5000/{param}"
USER_URL = f"http://127.0.0.1:5000/user/{param}"

def main():
    
    # Hello World
    response = requests.get(URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")

    # Uesr
    response = requests.get(USER_URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")

if __name__ == '__main__':
    main()