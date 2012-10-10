#!/usr/bin/python
# -*- coding: utf-8 -*-
from application.model import Model


class PV(Model):
	def __init__(self, db):
		self.table = 'pv'
		self.rows = [
			'title'
		]
		self.validate = {
				'title': {
					'type': str,
					'length': None
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

	def create(self, fields):
		return self.db.create(self.table, fields)

	def retrieve(self, fields=None, where='1=1', join=None):
		return self.db.retrieve(self.table, fields, where, join)

	#def update(self, fields=None, where='1=1'):
		#pass

	def delete(self, where='1=0'):
		return self.db.delete(self.table, where)
