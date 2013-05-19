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
				'required': True,
				'messages': {
					'required': 'Full name required.',
					'maxLength': 'Too long.',
					'empty': 'Cannot be empty.'
				}
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
		#self.has_many = {
		#	'propositions': {
		#		'table':'proposition',
		#		'key':'participant_id',
		#		'delete':'cascade',
		#		'update':None
		#	}
		#}

		super(Participant, self).__init__(db)
