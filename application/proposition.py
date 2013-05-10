#!/usr/bin/python
# -*- coding: utf-8 -*-
from application.model import Model


class Proposition(Model):
	def __init__(self, db):
		self.table = 'proposition'
		self.rows = [
			'id',
			'text',
			'pv_id',
			'point_id',
			'participant_id',
			'vote_id',
			'parent_id',
			'attributes'
		]
		self.validation = {
			'text': {
				'type': str,
				'empty': False,
				'required': True
			}
		}
		self.belongs_to = {
			'pv': {
				'table':'pv',
				'key':'pv_id'
			},
			'point': {
				'table':'point',
				'key':'point_id'
			},
			'initiator': {
				'table':'participant',
				'key':'participant_id'
			},
			'parent': {
				'table':'proposition',
				'key':'parent_id'
			}
		}
		self.has_many = {
			'votes': {
				'table':'vote',
				'key':'vote_id',
				'delete':'cascade',
				'update':None
			}
		}

		super(Proposition, self).__init__(db)
