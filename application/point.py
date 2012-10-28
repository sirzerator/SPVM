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
		self.belongs_to = {
			'pv': {
				'table':'pv',
				'key':'pv_id'
			},
			'parent': {
				'table':'point',
				'key':'parent_id'
			}
		}
		self.has_many = {
			'children': {
				'table':'point',
				'key':'parent_id'
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

		super(Point, self).__init__(db)
