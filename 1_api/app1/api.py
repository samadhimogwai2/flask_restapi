from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        response = {'msg': 'Hello world'}
        return json.dumps(response)
    
# 指定のパスにアクセスした場合、HelloWorldを実行    
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
    