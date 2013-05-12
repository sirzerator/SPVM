#!/usr/bin/python
# -*- coding: utf-8 -*-
from models.model import Model


class Participant(Model):
	def __init__(self, db):
		self.table = 'participant'
		self.rows = [
			'id',
			'full_name',
			'pv_id',
			'group_id'
		]
		self.validation = {
			'full_name': {
				'type': str,
				'empty': False,
				'minLength':1,
				'maxLength':100,
				'required': True
			}
		}
		self.belongs_to = {
			'pv': {
				'table':'pv',
				'key':'pv_id'
			},
			'group': {
				'table':'group',
				'key':'group_id'
			}
		}
		self.has_many = {
			'points': {
				'table':'point',
				'key':'participant_id',
				'delete':'cascade',
				'update':None
			}
		}

		super(Participant, self).__init__(db)
