from flask import request
from flask_restful import Resource, Api
import json
from app import app, db
from models import User

class AllUsers(Resource):
    def get(self):
        try:
            users = db.session.query(User).all()
            users_list = []
            for user in users:
                users_list.append(
                    {
                        "id": str(user.id),
                        "username": str(user.username),
                    }
                )
            response = {
                'status': "SUCCESS",
                'users': users_list,
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "error": str(e)
                }

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

            response = {
                'status': "SUCCESS",
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            
        return json.dumps(response)

    def delete(self):
        try:
            db.session.query(User).delete()
            db.session.commit()

            response = {
                'status': "SUCCESS",
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            
        return json.dumps(response)
    
class UserApi(Resource):
    def get(self, id):
        try:
            user = db.session.query(User).get(id)
            response = {
                "status": "SUCCESS",
                'id': user.id,
                'username': user.username
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }

        return json.dumps(response)
    
    def put(self, id):
        try:
            user = db.session.query(User).get(id)
            put_data = json.loads(request.data)
            user.username = put_data["username"]
            db.session.add(user)
            db.session.commit()

            response = {
                'status': "SUCCESS",
                }

        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }

        return json.dumps(response)
    
    def delete(self, id):
        try:
            user = db.session.query(User).filter_by(id=id)
            user.delete()
            db.session.commit()

            response = {
                'status': "SUCCESS",
                }

        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }

        return json.dumps(response)

if __name__ == '__main__':
    api = Api(app)

    api.add_resource(AllUsers, '/')
    api.add_resource(UserApi, '/user/<int:id>')

    with app.app_context():
        db.create_all()
    
    app.run(debug=True)