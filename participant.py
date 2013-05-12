from bottle import *
from application.pv import PV
from application.participant import Participant

from collections import defaultdict


class Participant_Controller:
	def __init__(self, db):
		self.db = db
		self.participant_hook = Participant(db)


	# Utility
	def get_current_pv_id(self):
		cookie_data = request.get_cookie('spvm', dict(), secret='secret')

		if not isinstance(cookie_data, dict) and cookie_is_encoded(cookie_data):
			cookie_data = cookie_decode(cookie_data, 'key')

		if 'pv_id' not in cookie_data or cookie_data['pv_id'] is None:
			redirect('/')

		return cookie_data['pv_id']

	### New
	def get_new_participant(self):
		return template('participant/new', title="New participant", pv_id=self.get_current_pv_id(), errors=dict(), data=defaultdict(lambda:''))
	get_new_participant.route = '/participant/new'
	get_new_participant.method = 'GET'

	def ajax_get_new_participant(self):
		return template('participant/new', ajax=True, title="New participant", pv_id=self.get_current_pv_id(), errors=dict(), data=defaultdict(lambda:''))
	ajax_get_new_participant.route = '/participant/ajax/new'
	ajax_get_new_participant.method = 'GET'