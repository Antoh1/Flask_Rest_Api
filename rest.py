from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///video.db'

db = SQLAlchemy(app)

app.app_context().push()

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    views = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Video(name = {name} , likes = {likes}, views= {views})' 

#db.create_all()

#making sure information passed conforms to rules using parse_args() in reqparse object
vid_put_args = reqparse.RequestParser()
vid_put_args.add_argument("name", type=str, help="name of the video to put", location='form', required=True)
vid_put_args.add_argument("likes", type=int, help="No of likes of the video to put", location='form', required=True)
vid_put_args.add_argument("views", type=int, help="No of Views of the video to put", location='form', required=True)
vid_patch_args = reqparse.RequestParser()
vid_patch_args.add_argument("views", type=int, help="No of Views of the video to patch", location='form')
vid_patch_args.add_argument("likes", type=int, help="No of likes of the video to patch", location='form')
vid_patch_args.add_argument("name", type=str, help="Name of the video to patch", location='form')


resource_fields = {
    'id' : fields.Integer,
    'name' : fields.String,
    'likes' : fields.Integer,
    'views' : fields.Integer
}

class index(Resource):
    @marshal_with(resource_fields)
    def get(self, vid_id):
        result = Video.query.filter_by(id=vid_id).first()
        if not result:
            abort(404, message="Video does not exist")
        return result

    @marshal_with(resource_fields)
    def put(self, vid_id):
        args = vid_put_args.parse_args()
        result = Video.query.filter_by(id=vid_id).first()
        if result:
            abort(409, message="Video already exists")
        video = Video(id=vid_id, views=args['views'], likes=args['likes'], name=args['name'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, vid_id):
        args = vid_patch_args.parse_args()
        result = Video.query.filter_by(id=vid_id).first()
        if not result:
            abort(404, message="Video does not exist")
        if args['name']:
            result.name = args['name']
        if args['likes']:
            result.likes = args['likes']
        if args['views']:
            result.views = args['views']
        db.session.commit()
        return result, 201
        

    def delete(self, vid_id):
        video_dont_exist(vid_id)
        del youtube_vids[vid_id]
        return "The video deleted successfully", 204       


api.add_resource(index, '/user/<int:vid_id>')


if __name__ == '__main__':
    app.run(debug=True)