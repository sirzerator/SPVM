from bottle import *
from application.pv import PV
from application.point import Point

from collections import defaultdict


class Point_Controller:
	def __init__(self, db):
		self.db = db
		self.point_hook = Point(db)


	# Utility
	def get_current_pv_id(self):
		cookie_data = request.get_cookie('spvm', dict(), secret='secret')

		if not isinstance(cookie_data, dict) and cookie_is_encoded(cookie_data):
			cookie_data = cookie_decode(cookie_data, 'key')

		if 'pv_id' not in cookie_data or cookie_data['pv_id'] is None:
			redirect('/')

		return cookie_data['pv_id']

	### New
	def get_new_point(self):
		return template('point/new', title="New point", pv_id=get_current_pv_id(), points=points, errors=dict())
	get_new_point.route = '/point/new'
	get_new_point.method = 'GET'

	def ajax_get_new_point():
		return template('point/new', ajax=True, title="New point", pv_id=get_current_pv_id(), points=points, errors=dict())
	ajax_get_new_point.route = '/point/ajax/new'
	ajax_get_new_point.method = 'GET'

	def post_new_point(self):
		fields = dict()
		fields['pv_id'] = request.forms.pv_id
		fields['title'] = request.forms.title
		fields['description'] = request.forms.description
		fields['rank'] = request.forms.rank
		fields['parent_id'] = request.forms.parent_id

		validation_result = self.point_hook.create(fields)

		if isinstance(validation_result, dict):
			points = self.point_hook.retrieve(where={'pv_id':fields['pv_id']})

			return template('point/new', pv_id=fields['pv_id'], points=points, errors=validation_result)
		else:
			redirect('/pv/'+fields['pv_id'])
	post_new_point.route = '/point/new'
	post_new_point.method = 'POST'

	def ajax_post_new_point(self):
		fields = dict()
		fields['pv_id'] = request.forms.pv_id
		fields['title'] = request.forms.title
		fields['description'] = request.forms.description
		fields['rank'] = request.forms.rank
		fields['parent_id'] = request.forms.parent_id

		validation_result = self.point_hook.create(fields)

		if isinstance(validation_result, dict):
			return validation_result
		else:
			record = self.point_hook.retrieve_one(where={'id':validation_result})

			return {'id': validation_result, 'parent_id': record['parent_id'], 'number': self.point_hook.get_numbering(int(validation_result))}
	ajax_post_new_point.route = '/point/ajax/new'
	ajax_post_new_point.method = 'POST'

	### Edit
	def get_edit_point(self, point_id=None):
		data = self.point_hook.retrieve_one(where={'id':point_id})

		points = self.point_hook.retrieve(where={'pv_id':data['pv_id']})

		return template('point/edit', title="Edit point", data=data, points=points, errors=dict())
	get_edit_point.route = '/point/edit/<point_id>'
	get_edit_point.method = 'GET'

	def ajax_get_edit_point(self):
		data = self.point_hook.retrieve_one(where={'id':request.query.point_id})

		points = self.point_hook.retrieve(where={'pv_id':data['pv_id']})

		return template('point/edit', ajax=True, title="Edit point", data=data, points=points, errors=dict())
	ajax_get_edit_point.route = '/point/ajax/edit'
	ajax_get_edit_point.method = 'GET'

	def post_edit_point(self):
		fields = dict()
		fields['id'] = request.forms.point_id
		fields['pv_id'] = request.forms.pv_id
		fields['title'] = request.forms.title
		fields['description'] = request.forms.description
		fields['rank'] = request.forms.rank
		fields['parent_id'] = request.forms.parent_id

		validation_result = self.point_hook.update(fields, {'id': fields['id']})

		if isinstance(validation_result, dict):
			data = self.point_hook.retrieve_one(where={'id':fields['id']})

			points = self.point_hook.retrieve(where={'pv_id':fields['pv_id']})

			return template('point/edit', data=data, points=points, errors=validation_result)
		else:
			redirect('/pv/'+fields['pv_id'])
	post_edit_point.route = '/point/edit'
	post_edit_point.method = 'POST'

	def post_edit_point(self):
		fields = dict()
		fields['id'] = request.forms.point_id
		fields['pv_id'] = request.forms.pv_id
		fields['title'] = request.forms.title
		fields['description'] = request.forms.description
		fields['rank'] = request.forms.rank
		fields['parent_id'] = request.forms.parent_id

		validation_result = self.point_hook.update(fields, {'id': fields['id']})

		if isinstance(validation_result, dict):
			return validation_result
		else:
			return {'id': validation_result, 'number': self.point_hook.get_numbering(int(validation_result))}
	post_edit_point.route = '/point/ajax/edit'
	post_edit_point.method = 'POST'

	### Delete
	def get_delete_point(self, point_id=None):
		if point_id is None:
			redirect('/')
		else:
			return template('point/delete', title="Delete point", point_id=point_id)
	get_delete_point.route = '/point/delete/<point_id>'
	get_delete_point.method = 'GET'

	def ajax_get_delete_point(self):
		point_id = request.query.point_id
		return template('point/delete', ajax=True, title="Delete point", point_id=point_id)
	ajax_get_delete_point.route = '/point/ajax/delete'
	ajax_get_delete_point.method = 'GET'

	def post_delete_point(self):
		point_id = request.forms.point_id

		pv_id = self.point_hook.retrieve_one(where={'id':point_id})['pv_id']

		if 'yes' not in request.forms or 'no' in request.forms or point_id is None:
			redirect('/pv/' + str(pv_id))
		else:
			if self.point_hook.delete({'id':point_id}):
				redirect('/pv/' + str(pv_id))
			else:
				print('Error. Do something.') # TODO
	post_delete_point.route = '/point/delete'
	post_delete_point.method = 'POST'

	def ajax_post_delete_point(self):
		point_id = request.forms.point_id
		if point_id is None:
			redirect('/')
		else:
			if self.point_hook.delete({'id':point_id}):
				redirect('/')
			else:
				print('Error. Do something.') # TODO
	ajax_post_delete_point.route = '/point/ajax/delete'
	ajax_post_delete_point.method = 'POST'