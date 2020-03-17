
from flask_restful import Api

from app import flaskApp
from .API import API


restServer = Api(flaskApp)


restServer.add_resource(API, "/")
