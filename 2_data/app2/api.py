from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, id):
        try:
            response = {
                'class': "HelloWorld",
                'msg': f'あなたが送ったidは{id}です'
                }
        except Exception as e:
            response = {'error': str(e)}
        return json.dumps(response)
    
class User(Resource):
    def get(self, id):
        try:
            response = {
                'class': "User",
                'msg': f'あなたが送ったidは{id}です'
                }
        except Exception as e:
            response = {'error': str(e)}
        return json.dumps(response)

api.add_resource(HelloWorld, '/<int:id>')
api.add_resource(User, '/user/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
    