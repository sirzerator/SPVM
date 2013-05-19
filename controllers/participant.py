from bottle import *
from models.pv import PV
from models.participant import Participant

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

	def post_new_participant(self):
		fields = dict()
		fields['pv_id'] = request.forms.pv_id
		fields['full_name'] = request.forms.full_name

		validation_result = self.participant_hook.create(fields)

		if isinstance(validation_result, dict):
			return template('participant/new', ajax=True, title="New participant", pv_id=self.get_current_pv_id(), errors=dict(), data=validation_result)
		else:
			redirect('/pv/'+fields['pv_id'])
	post_new_participant.route = '/participant/new'
	post_new_participant.method = 'POST'

	def ajax_post_new_participant(self):
		fields = dict()
		fields['pv_id'] = request.forms.pv_id
		fields['full_name'] = request.forms.full_name

		validation_result = self.participant_hook.create(fields)

		if isinstance(validation_result, dict):
			response.status = 400
			return validation_result
		else:
			return {'id': validation_result}
	ajax_post_new_participant.route = '/participant/ajax/new'
	ajax_post_new_participant.method = 'POST'

	### Edit
	def get_edit_participant(self, participant_id=None):
		data = self.participant_hook.retrieve_one(where={'id':participant_id})

		return template('participant/edit', title="Edit participant", data=data, errors=dict())
	get_edit_participant.route = '/participant/edit/<participant_id>'
	get_edit_participant.method = 'GET'

	def ajax_get_edit_participant(self):
		data = self.participant_hook.retrieve_one(where={'id':request.query.participant_id})

		return template('participant/edit', ajax=True, title="Edit participant", data=data, errors=dict())
	ajax_get_edit_participant.route = '/participant/ajax/edit'
	ajax_get_edit_participant.method = 'GET'

	def post_edit_participant(self):
		fields = dict()
		fields['id'] = request.forms.participant_id
		fields['pv_id'] = request.forms.pv_id
		fields['full_name'] = request.forms.full_name

		validation_result = self.participant_hook.update(fields, {'id': fields['id']})

		if isinstance(validation_result, dict):
			data = self.participant_hook.retrieve_one(where={'id':fields['id']})

			return template('participant/edit', data=data, errors=validation_result)
		else:
			redirect('/pv/'+fields['pv_id'])
	post_edit_participant.route = '/participant/edit'
	post_edit_participant.method = 'POST'

	def ajax_post_edit_participant(self):
		fields = dict()
		fields['id'] = request.forms.participant_id
		fields['pv_id'] = request.forms.pv_id
		fields['full_name'] = request.forms.full_name

		validation_result = self.participant_hook.update(fields, {'id': fields['id']})

		if isinstance(validation_result, dict):
			return validation_result
		else:
			return {'id': validation_result}
	ajax_post_edit_participant.route = '/participant/ajax/edit'
	ajax_post_edit_participant.method = 'POST'

	### Delete
	def get_delete_participant(self, participant_id=None):
		if participant_id is None:
			redirect('/')
		else:
			return template('participant/delete', title="Delete participant", participant_id=participant_id)
	get_delete_participant.route = '/participant/delete/<participant_id>'
	get_delete_participant.method = 'GET'

	def ajax_get_delete_participant(self):
		participant_id = request.query.participant_id
		return template('participant/delete', ajax=True, title="Delete participant", participant_id=participant_id)
	ajax_get_delete_participant.route = '/participant/ajax/delete'
	ajax_get_delete_participant.method = 'GET'

	def post_delete_participant(self):
		participant_id = request.forms.participant_id

		pv_id = self.participant_hook.retrieve_one(where={'id':participant_id})['pv_id']

		if 'yes' not in request.forms or 'no' in request.forms or participant_id is None:
			redirect('/pv/' + str(pv_id))
		else:
			if self.participant_hook.delete({'id':participant_id}):
				redirect('/pv/' + str(pv_id))
			else:
				print('Error. Do something.') # TODO
	post_delete_participant.route = '/participant/delete'
	post_delete_participant.method = 'POST'

	def ajax_post_delete_participant(self):
		participant_id = request.forms.participant_id
		if participant_id is None:
			redirect('/')
		else:
			if self.participant_hook.delete({'id':participant_id}):
				redirect('/')
			else:
				print('Error. Do something.') # TODO
	ajax_post_delete_participant.route = '/participant/ajax/delete'
	ajax_post_delete_participant.method = 'POST'