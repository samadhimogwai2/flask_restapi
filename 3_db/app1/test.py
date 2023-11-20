import requests
import json
import pandas as pd

URL = "http://127.0.0.1:5000"
USERS = [
    {'id': 0, 'username': "Ichiro"},
    {'id': 1, 'username': "Jiro"},
    {'id': 2, 'username': "Saburo"},
    {'id': 3, 'username': "Shiro"},
]

def main():
    # GET
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")

    # --------------------------------------------------------
    # POST
    for user in USERS:
        response = requests.post(URL, data=json.dumps(user))
        print(f"status code: {response.status_code}")
        print(f"content: {json.loads(response.json())}")

    # GET
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")
    # --------------------------------------------------------
    js = json.loads(response.json())
    usernames = [user['username'] for user in js['Users']]
    print(usernames)

    # --------------------------------------------------------
    # DELETE
    response = requests.delete(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}")

    # GET
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")
    # --------------------------------------------------------

if __name__ == '__main__':
    main()