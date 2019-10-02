#!python
#@author prakashkl88@GitHub

from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Sachin_Tendulkar",
        "age": 43,
        "sport": "Cricket",
        "rank": 1 
    },
    {
        "name": "Roger_Federer",
        "age": 37,
        "sport": "Tennis",
        "rank": 3
    },
    {
        "name": "Christiano_Ronaldo",
        "age": 35,
        "sport": "Football",
        "rank": 2
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("sport")
        parser.add_argument("rank")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "sport": args["sport"],
            "rank": args["rank"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("sport")
        parser.add_argument("rank")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["sport"] = args["sport"]
                user["rank"] = args["rank"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "sport": args["sport"],
            "rank": args["rank"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/user/<string:name>")

app.run(debug=True)
