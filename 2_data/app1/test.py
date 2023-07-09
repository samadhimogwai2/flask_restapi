import requests
import json

URL = f"http://127.0.0.1:5000"
TRY_URL = f"http://127.0.0.1:5000/try"
TRACE_URL = f"http://127.0.0.1:5000/trace"

def main():
    
    # /
    response = requests.get(URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")

    # /try
    response = requests.get(TRY_URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")

    # /trace
    response = requests.get(TRACE_URL)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")

if __name__ == '__main__':
    main()