#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime


class Model:

	def __init__(self, db):
		self.db = db
		self.db.create_table(self.description)

	def create(self, fields):
		print('Not implemented.')
		raise NotImplementedError

	def retrieve(self, fields=None, where=None, join=None):
		print('Not implemented.')
		raise NotImplementedError

	def update(self, fields=None, where=None):
		print('Not implemented.')
		raise NotImplementedError

	def delete(self, where=None):
		print('Not implemented.')
		raise NotImplementedError

	# TODO Define defaults, possible keys/values
	def validate(self, fields=None):
		if self.validation is None:
			return dict()
		else:
			validation_errors = dict()
			for field_name, field_validation in self.validation.items():
				if field_name in fields:
					if 'required' in field_validation and field_validation['required']:
						if 'empty' in field_validation and not field_validation['empty']:
							if len(fields[field_name].strip()) == 0:
								validation_errors[field_name] = 'Field ' + field_name + ' : cannot be empty.'
					if 'type' in field_validation and not isinstance(fields[field_name], field_validation['type']) :
						validation_errors[field_name] = 'Field ' + field_name + ' : incorrect type.'
					if 'dateFormat' in field_validation:
						try:
							datetime.strptime(fields[field_name], field_validation['dateFormat'])
						except ValueError:
							validation_errors[field_name] = 'Field ' + field_name + ' : incorrect date/time format.'
				elif 'required' in field_validation and field_validation['required']:
					validation_errors[field_name] = 'Field ' + field_name + ' : not present.'

		return validation_errors