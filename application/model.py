#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import datetime


class Model:

	def __init__(self, db):
		self.db = db

	def create_table(self):
		self.db.create_table(self.description)

	def create(self, fields):
		validation_errors = self.validate(fields)
		if len(validation_errors) == 0:
			if 'created' in self.rows and 'created' not in fields.keys():
				fields['created'] = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

			if self.db.create(self.table, fields):
				return self.db.last_insert_rowid()
			else:
				return {'database':'DB Error.'}

		return validation_errors

	def retrieve(self, fields=list('*'), where=None, order=None, **options):
		recursion = options['recursion'] if 'recursion' in options else 1;

		if isinstance(fields, str):
			fields = [fields]

		base = self.db.retrieve(self.table, fields, where, order);

		if isinstance(self.has_many, dict):
			rows_by_level = list()
			rows_by_level.append(base['rows'])

			current_level = 0
			while current_level < recursion and rows_by_level:
				rows_by_level.append(list())
				for row in rows_by_level[current_level]:
					for relation_name, relation_attributes in self.has_many.items():
						row_where = {relation_attributes['key']:row['id']}

						row[relation_name] = self.db.retrieve(relation_attributes['table'], '*', row_where)

						rows_by_level[current_level+1].extend(row[relation_name]['rows'])
				current_level += 1

		return base

	def retrieve_one(self, fields=list('*'), where=None, order=None):
		if isinstance(fields, str):
			fields = [fields]

		return self.db.retrieve(self.table, fields, where, order)['rows'][0];

	def update(self, fields=None, where=None):
		validation_errors = self.validate(fields)
		if len(validation_errors) == 0:
			if self.db.update(self.table, fields, where):
				return fields['id']
			else:
				return {'database':'DB Error.'}

		return validation_errors

	def delete(self, where=None):
		if isinstance(self.has_many, dict):
			for has_many_relation in self.has_many:
				if 'delete' in self.has_many[has_many_relation]:
					if self.has_many[has_many_relation]['delete'] == 'cascade':
						table_module = __import__('application.' + self.has_many[has_many_relation]['table'], fromlist=['application'])
						classname = self.has_many[has_many_relation]['table'][0].upper() + self.has_many[has_many_relation]['table'][1:]
						table_hook = getattr(table_module, classname)(self.db)

						children_where = dict()
						children_where[self.has_many[has_many_relation]['key']] = where['id']

						if isinstance(table_hook.belongs_to, dict):
							for child_belongs_to_relation in table_hook.belongs_to:
								print(child_belongs_to_relation)
								if table_hook.belongs_to[child_belongs_to_relation]['table'] == table_hook.table:
									if table_hook.belongs_to[child_belongs_to_relation]['key'] not in children_where:
										children_where[table_hook.belongs_to[child_belongs_to_relation]['key']] = ''

						children = table_hook.retrieve(['id'], children_where, None, recursion=0)
						if children['count'] > 0:
							for row in children['rows']:
								result = table_hook.delete({'id':row['id']})
								if result is False:
									return {'database':'DB Error.'}

		return self.db.delete(self.table, where)

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
					if 'type' in field_validation:
						if field_validation['type'] == int:
							try:
								int(fields[field_name])
							except(ValueError):
								if fields[field_name].strip() != "":
									validation_errors[field_name] = 'Field ' + field_name + ' : integer type expected.'
						elif not isinstance(fields[field_name], field_validation['type']):
							validation_errors[field_name] = 'Field ' + field_name + ' : incorrect type.'
					if 'dateFormat' in field_validation:
						try:
							datetime.strptime(fields[field_name], field_validation['dateFormat'])
						except ValueError:
							validation_errors[field_name] = 'Field ' + field_name + ' : incorrect date/time format.'
				elif 'required' in field_validation and field_validation['required']:
					validation_errors[field_name] = 'Field ' + field_name + ' : not present.'

		return validation_errors