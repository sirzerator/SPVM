#!/usr/bin/python
# -*- coding: utf-8 -*-
from optparse import OptionParser
import sys, os
from bottle import route, run, debug, template, redirect, request, response, static_file
from application.pv import PV


# Parsing command line arguments
parser = OptionParser()

parser.add_option("-v", "--verbose", action="store_true", dest="verbose")
parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default=False)

parser.add_option("-H", "--host", action="store", type="string", dest="host", default="localhost")
parser.add_option("-P", "--port", action="store", type="string", dest="port", default="8080")

parser.add_option("-m", "--db-module", "--database-module", action="store", type="string", dest="db_module", default="sqlite3")

parser.add_option("-d", "--db", "--database", action="store", type="string", dest="database", default="spvm")
parser.add_option("-u", "--username", action="store", type="string", dest="username")
parser.add_option("-p", "--password", action="store", type="string", dest="password")

(options, args) = parser.parse_args()

# Loading database (model)
try:
	db_module = __import__('database.' + options.db_module, fromlist=['database'])
except ImportError:
	print('DB Error.')
	exit(1)

# Connecting to database
db_hook = db_module.DBModule(options.database, options.username, options.password)

# Static files
@route('/js/<filepath:path>')
def server_static_js(filepath):
	pathname = os.path.dirname(sys.argv[0])
	realpath = os.path.abspath(pathname)
	return static_file(filepath, root=realpath + '/js/')

@route('/css/<filepath:path>')
def server_static_css(filepath):
	pathname = os.path.dirname(sys.argv[0])
	realpath = os.path.abspath(pathname)
	return static_file(filepath, root=realpath + '/css/')

# Index
@route('/')
def index():
	pv = PV(db_hook)
	pvs = pv.retrieve()
	return template('index', pvs=pvs)

@route('/counter')
def counter():
	count = int(request.cookies.get('counter', '0'))
	count += 1
	response.set_cookie('counter', str(count))
	return 'You visited this page %d times' % count

###
### PV
###

### New
@route('/pv/new', method='GET')
def get_new():
	return template('pv/new', errors=dict())

@route('/pv/ajax/new', method='GET')
def ajax_get_new():
	return template('pv/ajax/new', errors=dict())

@route('/pv/new', method='POST')
def post_new():
	fields = dict()
	fields['title'] = request.forms.title
	fields['date'] = request.forms.date
	fields['time'] = request.forms.time
	fields['location'] = request.forms.location
	fields['description'] = request.forms.description

	pv = PV(db_hook)
	validation_result = pv.create(fields)
	if isinstance(validation_result, dict):
		return template('pv/new', errors=validation_result)
	else:
		redirect('/')

@route('/pv/ajax/new', method='POST')
def ajax_post_new():
	fields = dict()
	fields['title'] = request.forms.title
	fields['date'] = request.forms.date
	fields['time'] = request.forms.time
	fields['location'] = request.forms.location
	fields['description'] = request.forms.description

	pv = PV(db_hook)
	validation_result = pv.create(fields)
	if isinstance(validation_result, dict):
		return validation_result
	else:
		return {'id': validation_result}

### Edit
@route('/pv/edit/<pv_id>', method='GET')
def get_edit(pv_id=None):
	pv = PV(db_hook)
	data = pv.retrieve(where={'id':pv_id})
	return template('pv/edit', data=data['rows'][0], errors=dict())

@route('/pv/ajax/edit', method='GET')
def ajax_get_edit():
	pv = PV(db_hook)
	data = pv.retrieve(where={'id':request.query.pv_id})
	return template('pv/ajax/edit', data=data['rows'][0], errors=dict())

@route('/pv/edit', method='POST')
def post_edit():
	fields = dict()
	fields['id'] = request.forms.pv_id
	fields['title'] = request.forms.title
	fields['date'] = request.forms.date
	fields['time'] = request.forms.time
	fields['location'] = request.forms.location
	fields['description'] = request.forms.description

	pv = PV(db_hook)
	validation_result = pv.update(fields, {'id': fields['id']})
	print(validation_result)
	if isinstance(validation_result, dict):

		return template('pv/edit', data=fields, errors=validation_result)
	else:
		redirect('/')

@route('/pv/ajax/edit', method='POST')
def ajax_post_edit():
	fields = dict()
	fields['id'] = request.forms.pv_id
	fields['title'] = request.forms.title
	fields['date'] = request.forms.date
	fields['time'] = request.forms.time
	fields['location'] = request.forms.location
	fields['description'] = request.forms.description

	pv = PV(db_hook)
	validation_result = pv.update(fields, {'id': fields['id']})
	if isinstance(validation_result, dict):
		return validation_result
	else:
		return {'id': validation_result}

### Delete
@route('/pv/delete/<pv_id>')
def get_delete(pv_id=None):
	if pv_id is None:
		redirect('/')
	else:
		return template('pv/delete', pv_id=pv_id)

@route('/pv/ajax/delete', method='GET')
def ajax_get_delete():
	pv_id = request.query.pv_id
	return template('pv/ajax/delete', pv_id=pv_id)

@route('/pv/delete', method='POST')
def post_delete():
	pv_id = request.forms.pv_id
	if pv_id is None:
		redirect('/')
	else:
		pv = PV(db_hook)
		if pv.delete({'id':pv_id}):
			redirect('/')
		else:
			print('Error. Do something.') # TODO

@route('/pv/ajax/delete', method='POST')
def ajax_post_delete():
	pv_id = request.forms.pv_id
	if pv_id is None:
		redirect('/')
	else:
		pv = PV(db_hook)
		if pv.delete({'id':pv_id}):
			redirect('/')
		else:
			print('Error. Do something.') # TODO


# Loading interface (controller/view)
debug(True)
run(host=options.host, port=options.port, reloader=True)