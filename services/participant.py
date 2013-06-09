from bottle import *
from services.rest import REST_Service
from models.participant import Participant


class Participant_Service(REST_Service):
	def __init__(self, db):
		self.service_hook = Participant(db)

		self.service_name = "participant"

		super(Participant_Service, self).__init__()
