#!/usr/bin/python
# -*- coding: utf-8 -*-
from optparse import OptionParser
import sys, os

import bottle
from bottle import *

from pv import PV_Controller
from point import Point_Controller
from participant import Participant_Controller

from application.pv import PV
from application.point import Point
from application.proposition import Proposition
from application.participant import Participant


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

# Loading database
try:
	db_module = __import__('database.' + options.db_module, fromlist=['database'])
except ImportError:
	print('DB Error.')
	exit(1)

# Connecting to database
db_hook = db_module.DBModule(options.database, options.username, options.password)

# Loading models
pv_hook = PV(db_hook)
point_hook = Point(db_hook)
proposition_hook = Proposition(db_hook)
participant_hook = Participant(db_hook)

# Building tables
pv_hook.create_table()
point_hook.create_table()
proposition_hook.create_table()
participant_hook.create_table()

def setup_routes(obj):
	for kw in dir(obj):
		attr = getattr(obj, kw)
		if hasattr(attr, 'route'):
			if hasattr(attr, 'method'):
				print('routing ' + str(attr) + ' with ' + attr.route + ', ' + attr.method)
				bottle.route(attr.route, attr.method)(attr)
			else:
				bottle.route(attr.route)(attr)

# Loading controllers
pv_controller = PV_Controller(db_hook)
setup_routes(pv_controller)

point_controller = Point_Controller(db_hook)
setup_routes(point_controller)

participant_controller = Participant_Controller(db_hook)
setup_routes(participant_controller)

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
	pvs = pv_hook.retrieve()
	return template('index', pvs=pvs)

@route('/counter')
def counter():
	count = int(request.cookies.get('counter', '0'))
	count += 1
	response.set_cookie('counter', str(count))
	return 'You visited this page %d times' % count

# Loading interface (controller/view)
run(host=options.host, port=options.port, reloader=True, debug=True)
