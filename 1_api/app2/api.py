from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        response = {'msg': 'HelloWorld'}
        return json.dumps(response)
    
class User(Resource):
    def get(self):
        response = {'msg': 'User'}
        return json.dumps(response)
    
api.add_resource(HelloWorld, '/')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
    