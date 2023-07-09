* 仮想環境の作成

```sh
cd ./6_ml_api # ディレクトリ移動
python3 -m venv venv # 仮想環境作成
source venv/bin/activate # 環境の中にはいる
python3 -m pip install --upgrade pip # pip upgrade
pip3 install -r requirements.txt # ライブラリインストール
```

* backend サーバー起動

```sh
cd ./backend
python api.py
```
