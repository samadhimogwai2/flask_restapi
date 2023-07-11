* 仮想環境の作成

```sh
cd ./7_ml_app # ディレクトリ移動
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

* frontend project作成

```sh
npm init vite-app frontend # プロジェクト(フォルダ)作成
cd frontend # 現在のディレクトリ移動
npm install # 必要なものをインストール
npm install vue-router@4 # 必要なものをインストール
npm install axios # 必要なものをインストール
npm run dev # サーバー立てる
```