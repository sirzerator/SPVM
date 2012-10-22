#!/usr/bin/python
# -*- coding: utf-8 -*-
from application.model import Model
from datetime import datetime


class PV(Model):
	def __init__(self, db):
		self.table = 'pv'
		self.rows = [
			'id',
			'user_id',
			'title'
			'date',
			'time',
			'location',
			'description',
			'code_id',
			'lock_id',
			'created',
			'modified'
		]
		self.validation = {
				'user_id': {
					'type': int
				},
				'title': {
					'type': str,
					'minLength': 1,
					'maxLength': 100,
					'empty': False,
					'required': True
				},
				'date': {
					'type': str,
					'dateFormat': '%Y-%m-%d',
					'required': True
				},
				'time': {
					'type': str,
					'dateFormat': '%H:%M:%S',
					'required': True
				},
				'location': {
					'type': str
				},
				'description': {
					'type': str
				},
				'code_id': {
					'type': int
				},
				'lock_id': {
					'type': int
				}
		}
		self.description = '''
			CREATE TABLE IF NOT EXISTS "pv" (
				"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
				"user_id" INTEGER NOT NULL DEFAULT 0,
				"title" TEXT,
				"date" DATE NOT NULL DEFAULT CURRENT_DATE,
				"time" TIME NOT NULL DEFAULT CURRENT_TIME,
				"location" TEXT,
				"description" TEXT,
				"code_id" INTEGER NOT NULL DEFAULT 0,
				"lock_id" INTEGER NOT NULL DEFAULT 0,
				"created" DATETIME NOT NULL,
				"modified" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
			)
		'''

		super(PV, self).__init__(db)

	#def create(self, fields):
		#return super(PV, self).create(fields)

	#def retrieve(self, fields='*', where=None, join=None):
		#return self.db.retrieve(self.table, fields, where, join)

	#def update(self, fields=None, where='1=1'):
		#pass

	#def delete(self, where='1=0'):
		#return self.db.delete(self.table, where)
