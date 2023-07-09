* 仮想環境の作成

```sh
cd ./4_db_api # ディレクトリ移動
python3 -m venv venv # 仮想環境作成
source venv/bin/activate # 環境の中にはいる
python3 -m pip install --upgrade pip # pip upgrade
pip3 install -r requirements.txt # ライブラリインストール
```

* API実行

```sh
cd ./app # ディレクトリ移動
python api.py # Flaskサーバー起動
python test.py # APIテスト
```
