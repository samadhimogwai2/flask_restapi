from flask import request
from flask_restful import Resource, Api
import json
from app import app, db
from models import Task
import uuid
from io import BytesIO
from PIL import Image
import base64
from image_test import image_recognition

class ImageRecognition(Resource):
    def post(self):
        try:
            # 画像のデータ取得
            data = json.loads(request.data)
            image_byte = base64.b64decode(data["image_b64"].encode("utf-8"))
            image_file = BytesIO(image_byte)
            image_pil = Image.open(image_file)
            score, category_name = image_recognition(image_pil)

            # 画像の認識
            task = Task(
                id = str(uuid.uuid4()),
                image_name = str(data["image_name"]),
                result = f"{category_name}: {100 * score:.1f}%",
            )
            db.session.add(task)
            db.session.commit()

            response = {
                'status': "SUCCESS",
                'data': f"{category_name}: {100 * score:.1f}%",
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }
            
        return json.dumps(response)

class AllTaskAPI(Resource):
    def get(self):
        try:
            tasks = db.session.query(Task).all()
            task_list = []
            for task in tasks:
                task_list.append(
                    {
                        "id": str(task.id),
                        "image_name": str(task.image_name),
                        "result": str(task.result),
                    }
                )
            response = {
                'status': "SUCCESS",
                'task_list': task_list,
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "error": str(e)
                }

        return json.dumps(response)

    def delete(self):
        try:
            db.session.query(Task).delete()
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
    
class TaskApi(Resource):
    def get(self, id):
        try:
            task = db.session.query(Task).get(id)
            response = {
                "status": "SUCCESS",
                    'task': {
                        'id': str(task.id),
                        "image_name": str(task.image_name),
                        "result": str(task.result),
                    }
                }
        except Exception as e:
            response = {
                "status": "FAIL",
                "Error": str(e)
                }

        return json.dumps(response)
    
    def delete(self, id):
        try:
            task = db.session.query(Task).filter_by(id=id)
            task.delete()
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

    api.add_resource(AllTaskAPI, '/')
    api.add_resource(TaskApi, '/<string:id>')
    api.add_resource(ImageRecognition, '/image')

    with app.app_context():
        db.create_all()
    
    app.run(debug=True)