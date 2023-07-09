from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
import json

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
# api
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)

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

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)