from bottle import *
from models.pv import PV
from models.point import Point
from models.participant import Participant

from collections import defaultdict


class PV_Controller:
	def __init__(self, db):
		self.db = db
		self.pv_hook = PV(db)
		self.point_hook = Point(db)
		self.participant_hook = Participant(db)

	### New
	def get_new_pv(self):
		return template('pv/new', title="New PV", errors=dict(), data=defaultdict(lambda:''))
	get_new_pv.route = '/pv/new'
	get_new_pv.method = 'GET'

	def ajax_get_new_pv(self):
		return template('pv/new', ajax=True, title="New PV", errors=dict(), data=defaultdict(lambda:''))
	ajax_get_new_pv.route = '/pv/ajax/new'
	ajax_get_new_pv.method = 'GET'

	def post_new_pv(self):
		fields = dict()
		fields['title'] = request.forms.title
		fields['date'] = request.forms.date
		fields['time'] = request.forms.time
		fields['location'] = request.forms.location
		fields['description'] = request.forms.description

		validation_result = self.pv_hook.create(fields)
		if isinstance(validation_result, dict):
			return template('pv/new', title="New PV", errors=validation_result, data=request.forms)
		else:
			redirect('/')
	post_new_pv.route = '/pv/new'
	post_new_pv.method = 'POST'

	def ajax_post_new_pv(self):
		fields = dict()
		fields['title'] = request.forms.title
		fields['date'] = request.forms.date
		fields['time'] = request.forms.time
		fields['location'] = request.forms.location
		fields['description'] = request.forms.description

		validation_result = self.pv_hook.create(fields)
		if isinstance(validation_result, dict):
			return validation_result
		else:
			return {'id': validation_result}
	ajax_post_new_pv.route = '/pv/ajax/new'
	ajax_post_new_pv.method = 'POST'

	### Edit
	def get_edit_pv(self, pv_id=None):
		data = self.pv_hook.retrieve_one(where={'id':pv_id})

		return template('pv/edit', title="New PV", data=data, errors=dict())
	get_edit_pv.route = '/pv/edit/<pv_id>'
	get_edit_pv.method = 'GET'

	def ajax_get_edit_pv(self):
		data = self.pv_hook.retrieve_one(where={'id':request.query.pv_id})

		return template('pv/edit', ajax=True, title="New PV", data=data, errors=dict())
	ajax_get_edit_pv.route = '/pv/ajax/edit'
	ajax_get_edit_pv.method = 'GET'

	def post_edit_pv(self):
		fields = dict()
		fields['id'] = request.forms.pv_id
		fields['title'] = request.forms.title
		fields['date'] = request.forms.date
		fields['time'] = request.forms.time
		fields['location'] = request.forms.location
		fields['description'] = request.forms.description

		validation_result = self.pv_hook.update(fields, {'id': fields['id']})

		if isinstance(validation_result, dict):
			return template('pv/edit', data=fields, errors=validation_result)
		else:
			redirect('/')
	post_edit_pv.route = '/pv/edit'
	post_edit_pv.method = 'POST'

	def ajax_post_edit_pv(self):
		fields = dict()
		fields['id'] = request.forms.pv_id
		fields['title'] = request.forms.title
		fields['date'] = request.forms.date
		fields['time'] = request.forms.time
		fields['location'] = request.forms.location
		fields['description'] = request.forms.description

		validation_result = self.pv_hook.update(fields, {'id': fields['id']})
		if isinstance(validation_result, dict):
			return validation_result
		else:
			return {'id': validation_result}
	ajax_post_edit_pv.route = '/pv/ajax/edit'
	ajax_post_edit_pv.method = 'POST'

	### Delete
	def get_delete_pv(self, pv_id=None):
		if pv_id is None:
			redirect('/')
		else:
			return template('pv/delete', title="Delete PV", pv_id=pv_id)
	get_delete_pv.route = '/pv/delete/<pv_id>'
	get_delete_pv.method = 'GET'

	def ajax_get_delete_pv(self):
		pv_id = request.query.pv_id
		return template('pv/delete', ajax=True, title="Delete PV", pv_id=pv_id)
	ajax_get_delete_pv.route = '/pv/ajax/delete'
	ajax_get_delete_pv.method = 'GET'

	def post_delete_pv(self):
		pv_id = request.forms.pv_id
		if 'yes' not in request.forms or 'no' in request.forms or pv_id is None:
			redirect('/')
		else:
			if self.pv_hook.delete({'id':pv_id}):
				redirect('/')
			else:
				print('Error. Do something.') # TODO
	post_delete_pv.route = '/pv/delete'
	post_delete_pv.method = 'POST'

	def ajax_post_delete_pv(self):
		pv_id = request.forms.pv_id
		print(pv_id)
		if pv_id is None:
			redirect('/')
		else:
			if self.pv_hook.delete({'id':pv_id}):
				redirect('/')
			else:
				print('Error. Do something.') # TODO
	ajax_post_delete_pv.route = '/pv/ajax/delete'
	ajax_post_delete_pv.method = 'POST'

	### Select
	def get_pv(self, pv_id=None):
		if pv_id is None:
			redirect('/')
		else:
			try:
				isinstance(int(pv_id), int)
			except ValueError:
				redirect('/')

			cookie_data = request.get_cookie('spvm', dict(), secret='secret')

			if not isinstance(cookie_data, dict) and cookie_is_encoded(cookie_data):
				cookie_data = cookie_decode(cookie_data, 'key')

			cookie_data['pv_id'] = pv_id

			response.set_cookie('spvm', cookie_encode(cookie_data, 'key'), secret='secret', path='/')

			pv_data = self.pv_hook.retrieve_one(where={'id':pv_id})

			points = self.point_hook.retrieve(where={'pv_id':pv_id, 'parent_id':''}, order="rank ASC", recursion=3)

			participants = self.participant_hook.retrieve(where={'pv_id':pv_id})

			return template('main', pv_id=pv_id, pv_data=pv_data, points=points, participants=participants)
	get_pv.route = '/pv/<pv_id>'
	get_pv.method = 'GET'

	### Unselect
	def close_pv(self):
		cookie_data = request.get_cookie('spvm', dict(), secret='secret')

		if not isinstance(cookie_data, dict) and cookie_is_encoded(cookie_data):
			cookie_data = cookie_decode(cookie_data, 'key')

		cookie_data['pv_id'] = 0

		response.set_cookie('spvm', cookie_encode(cookie_data, 'key'), secret='secret', path='/')

		redirect('/')
	close_pv.route = '/pv/close'
	close_pv.method = 'GET'

	### Configure TODO
	def config_pv(self):
		redirect('/')
	config_pv.route = '/pv/config'
	config_pv.method = 'GET'