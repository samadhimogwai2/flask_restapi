from flask import request
from flask_restful import Resource, Api
import json
from app import app, db
from models import User

class HelloWorld(Resource):
    def get(self):
        try:
            users = db.session.query(User).all()
            users_list = []
            for user in users:
                users_list.append(
                    {
                        "id": str(user.id),
                        "username": str(user.username)
                    }
                )
            response = {"Users": users_list}
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)
    
    def post(self):
        try:
            data = json.loads(request.data)
            user = User(
                id = data["id"],
                username = data["username"],
            )
            db.session.add(user)
            db.session.commit()
            response = {'msg': "CREATED"}
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)
    
    def delete(self):
        try:
            db.session.query(User).delete()
            db.session.commit()
            response = {"msg": "DELETED"}
        except Exception as e:
            response = {"error": str(e)}
        return json.dumps(response)

if __name__ == '__main__':
    
    api = Api(app)
    api.add_resource(HelloWorld, '/')

    with app.app_context():
        db.create_all()
    
    app.run(debug=True)