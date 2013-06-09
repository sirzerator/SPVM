from bottle import *
from services.rest import REST_Service
from models.point import Point


class Point_Service(REST_Service):
	def __init__(self, db):
		self.service_hook = Point(db)

		self.service_name = "points"

		super(Point_Service, self).__init__()
