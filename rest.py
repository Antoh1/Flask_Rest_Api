from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

data = { 'tirop' : {'name':'Kwechi', 'age':32, 'height':5.7},
             'Kip' : {'name':'Rael', 'age':34, 'height':6.8}
            }

class index(Resource):
    def get(self, name):
        return {'user':data[name]}

    # def post(self):
    #     return {'name':'ando', 'age':32}    


api.add_resource(index, '/user/<string:name>')


if __name__ == '__main__':
    app.run(debug=True)