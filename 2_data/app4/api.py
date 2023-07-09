from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    
    def post(self):
        try:
            data = json.loads(request.data)
            response = {
                'data': f'あなたが送ったdataは{data}',
                'dict': f'あなたのusernameは{data["username"]}'
                }
        except Exception as e:
            response = {'error': str(e)}
        return json.dumps(response)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
    