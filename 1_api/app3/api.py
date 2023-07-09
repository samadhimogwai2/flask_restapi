from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        response = {'msg': 'GET'}
        return json.dumps(response)
    
    def post(self):
        response = {'msg': 'POST'}
        return json.dumps(response)
    
    def put(self):
        response = {'msg': 'PUT'}
        return json.dumps(response)
    
    def delete(self):
        response = {'msg': 'DELETE'}
        return json.dumps(response)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
    