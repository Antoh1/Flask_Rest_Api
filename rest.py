from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

#making sure information passed conforms to rules using parse_args() in reqparse object
vid_put_args = reqparse.RequestParser()
vid_put_args.add_argument("name", type=str, help="name of the video to put", location='form', required=True)
vid_put_args.add_argument("likes", type=int, help="No of likes of the video to put", location='form', required=True)
vid_put_args.add_argument("views", type=int, help="No of Views of the video to put", location='form', required=True)


youtube_vids = {}

def video_dont_exist(vid_id):
    if vid_id not in youtube_vids:
        abort(404, message="Video not found")

def video_exist(vid_id):
    if vid_id in youtube_vids:
        abort(409, message="Video with the ID already exists")

class index(Resource):
    def get(self, vid_id):
        video_dont_exist(vid_id)
        return youtube_vids[vid_id]

    def put(self, vid_id):
        video_exist(vid_id)
        args = vid_put_args.parse_args()
        youtube_vids[vid_id] = args
        return youtube_vids[vid_id], 201

    def delete(self, vid_id):
        video_dont_exist(vid_id)
        del youtube_vids[vid_id]
        return "The video deleted successfully", 204       


api.add_resource(index, '/user/<int:vid_id>')


if __name__ == '__main__':
    app.run(debug=True)