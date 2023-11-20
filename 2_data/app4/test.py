import requests
import json

URL = f"http://127.0.0.1:5000"
# 辞書型をJson形式へ
POST_DATA = json.dumps({"username": "Tatsuki"})

def main():
    # ローカルホスト（http://127.0.0.1:5000）上で実行されているRESTful APIに対して
    # Jsonデータをパラメータとして受け渡し、POSTリクエストを送信    
    response = requests.post(URL, data=POST_DATA)
    print(f"\nurl: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {json.loads(response.json())}\n")

if __name__ == '__main__':
    main()