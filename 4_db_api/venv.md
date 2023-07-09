* 仮想環境の作成

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
```

* API実行

```sh
cd ./app # ディレクトリ移動
python api.py # Flaskサーバー起動
python test.py # APIテスト
```