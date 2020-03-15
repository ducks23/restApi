
from flask_restful import Api

from app import flaskApp
from .Task import Task
from .TaskById import TaskById


restServer = Api(flaskApp)


restServer.add_resource(Task, "/api/v1.0/task")
restServer.add_resource(TaskById, "/api/v1.0/task/id/<string:taskId>")
