from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from request_builder import RequestBuilder
from connections_list import ConnectionsList

app = Flask(__name__)
api = Api(app)

request_builder = RequestBuilder()


class Connection(Resource):
  def get(self, f, t):
    cl = ConnectionsList(request_builder, f, t)
    cl.fetchList()
    cl.fetchDetails()

    return cl.toJSON()


api.add_resource(Connection, "/connection/<f>/<t>")

if __name__ == "__main__":
  app.run(port="5002")
