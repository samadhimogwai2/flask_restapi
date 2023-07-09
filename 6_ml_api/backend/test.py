import requests
import json
import base64
import os

URL = "http://127.0.0.1:5000"
IMAGE_URL = "http://127.0.0.1:5000/image"

POST_DATA = {
    'image_name': 'sample.jpg',
    'image_b64': '',
}

# Step 0: Load Image
print("\nLoad Image")
with open("./images/sample.jpg", "rb") as f:
    image_b64 = base64.b64encode(f.read()).decode("utf-8")
POST_DATA["image_b64"] = image_b64

# DELETE POST GET
# --------------------------------------------------------
# DELETE ALL TASKS
response = requests.delete(URL)
print(f"\nDELETE url: {response.url}")
print(f"DELETE content: {json.loads(response.json())}")

# POST
response = requests.post(IMAGE_URL, data=json.dumps(POST_DATA))
print(f"\nPOST url: {response.url}")
print(f"POST content: {json.loads(response.json())}")

# GET ALL Tasks
response = requests.get(URL)
tasks = json.loads(response.json())
sample_id = tasks["task_list"][0]["id"]
TASK_URL = os.path.join(URL, sample_id)
print(f"\nGET url: {response.url}")
print(f"content: {json.loads(response.json())}\n")
# --------------------------------------------------------


# ID
# --------------------------------------------------------
# GET A USER 
response = requests.get(TASK_URL)
print(f"\nGET url: {response.url}")
print(f"content: {json.loads(response.json())}")

# DELETE A USER DATA
response = requests.delete(TASK_URL)
print(f"\nDELETE url: {response.url}")
print(f"content: {json.loads(response.json())}\n")
# --------------------------------------------------------
