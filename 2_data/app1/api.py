from flask import Flask
from flask_restful import Resource, Api
import json
import traceback

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        response = {'msg': 'HelloWorld'}
        return json.dumps(response)
    
class Try(Resource):
    def get(self):
        try:
            int("Error") # ここでError
            response = {'msg': 'Try'}
        except Exception as e:
            response = {'error': str(e)}
        return json.dumps(response)
    
class Trace(Resource):
    def get(self):
        try:
            int("Error") # ここでError
            response = {'msg': 'Trace'}
        except Exception:
            response = {'error': str(traceback.format_exc())}
        return json.dumps(response)

api.add_resource(HelloWorld, '/')
api.add_resource(Try, '/try')
api.add_resource(Trace, '/trace')

if __name__ == '__main__':
    app.run(debug=True)
    