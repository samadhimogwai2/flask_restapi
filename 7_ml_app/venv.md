* 仮想環境の作成

```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
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