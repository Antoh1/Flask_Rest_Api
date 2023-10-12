from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

youtube_vids = {}

class index(Resource):
    def get(self, vid_id):
        return youtube_vids[vid_id]

    def put(self, vid_id):
        print(request.form)
        return {}    


api.add_resource(index, '/user/<int:vid_id>')


if __name__ == '__main__':
    app.run(debug=True)