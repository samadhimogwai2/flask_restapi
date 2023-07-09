import requests
import json

URL = f"http://127.0.0.1:5000"
POST_DATA = json.dumps({"username": "Tatsuki"})

def main():

    response = requests.post(URL, data=POST_DATA)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")

if __name__ == '__main__':
    main()