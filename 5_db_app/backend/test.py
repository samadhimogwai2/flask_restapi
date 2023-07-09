import requests
import json
import os

URL = "http://127.0.0.1:5000"
USER_ID = 4
USER_URL = os.path.join(URL, f'user/{USER_ID}')

USERS = [
    {'id': 0, 'username': "Ichiro"},
    {'id': 1, 'username': "Jiro"},
    {'id': 2, 'username': "Saburo"},
    {'id': 3, 'username': "Shiro"},
]
POST_DATA = {
    'id': 4,
    'username': 'Goro'
}
PUT_DATA = {
    "username": "Tatsuki"
    }

def make_sample_users():
    print("\nmake_sample_users")

    # RESET USERS DATA 
    # --------------------------------------------------------
    # DELETE USERS
    response = requests.delete(URL)
    print(f"\nDELETE url: {response.url}")
    print(f"DELETE content: {json.loads(response.json())}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")
    # --------------------------------------------------------

    # CREATE USERS
    # --------------------------------------------------------
    # POST SAMPLE USERS
    for user in USERS:
        response = requests.post(URL, data=json.dumps(user))
        print(f"status code: {response.status_code}")
        print(f"content: {json.loads(response.json())}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nGET url: {response.url}")
    print(f"GET content: {json.loads(response.json())}")
    # --------------------------------------------------------

def make_user():
    print("\n\nmake_user")

    # CREATE A USER
    # --------------------------------------------------------
    # POST
    response = requests.post(URL, data=json.dumps(POST_DATA))
    print(f"\nPOST url: {response.url}")
    print(f"POST DATA: {POST_DATA}")
    print(f"POST content: {json.loads(response.json())}")

    # GET A USER 
    response = requests.get(USER_URL)
    print(f"\nGET url: {response.url}")
    print(f"content: {json.loads(response.json())}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")
    # --------------------------------------------------------

    # CHANGE A USER
    # --------------------------------------------------------
    # PUT ID
    response = requests.put(USER_URL, data=json.dumps(PUT_DATA))
    print(f"\nPUT url: {response.url}")
    print(f"PUT DATA: {PUT_DATA}")
    print(f"content: {json.loads(response.json())}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")
    # --------------------------------------------------------

    # DELETE A USER DATA
    # --------------------------------------------------------
    # DELETE ID
    response = requests.delete(USER_URL)
    print(f"\nDELETE url: {response.url}")
    print(f"content: {json.loads(response.json())}")

    # GET USERS
    response = requests.get(URL)
    print(f"\nstatus code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")
    # CHANGE A USER DATA 
    # --------------------------------------------------------

def main():
    make_sample_users()
    make_user()

if __name__ == '__main__':
    main()