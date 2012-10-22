#!/usr/bin/python
# -*- coding: utf-8 -*-
from application.model import Model
from datetime import datetime


class Point(Model):
	def __init__(self, db):
		self.table = 'point'
		self.rows = [
			'id',
			'pv_id',
			'parent_id'
			'title',
			'description',
			'rank'
		]
		self.validation = {
				'pv_id': {
					'type': int,
					'required': True
				},
				'parent_id': {
					'type': int
				},
				'title': {
					'type': str,
					'minLength': 1,
					'maxLength': 100,
					'empty': False,
					'required': True
				},
				'description': {
					'type': str
				},
				'rank': {
					'type': int
				}
		}
		self.description = '''
			CREATE  TABLE  IF NOT EXISTS "point" (
				"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
				"pv_id" INTEGER NOT NULL,
				"parent_id" INTEGER,
				"title" TEXT NOT NULL,
				"description" TEXT,
				"rank" INTEGER NOT NULL DEFAULT 0
			)
		'''

		super(PV, self).__init__(db)

	#def create(self, fields):
		#return super(PV, self).create(fields)

	def retrieve(self, fields=None, where='1=1', join=None):
		return self.db.retrieve(self.table, fields, where, join)

	#def update(self, fields=None, where='1=1'):
		#pass

	def delete(self, where=None):
		return self.db.delete(self.table, where)
