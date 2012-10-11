#!/usr/bin/python
# -*- coding: utf-8 -*-


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

	def validate(self, fields=None):
		print('Not implemented.')
		raise NotImplementedError