from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        try: 
            query_data = request.args
            response = {
                'query_data': str(query_data),
                'query_data.get': str(query_data.get("username"))
                }
        except Exception as e:
            response = {'error': str(e)}
        return json.dumps(response)
    
class User(Resource):
    def get(self):
        try: 
            query_data = request.args
            response = {
                'query_data': str(query_data),
                'query_data.get': str(query_data.get("username"))
                }
        except Exception as e:
            response = {'error': str(e)}
        return json.dumps(response)

api.add_resource(HelloWorld, '/')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
    