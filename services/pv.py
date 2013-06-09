from bottle import *
from services.rest import REST_Service
from models.pv import PV


class PV_Service(REST_Service):
	def __init__(self, db):
		self.service_hook = PV(db)

		self.service_name = "pvs"

		super(PV_Service, self).__init__()
