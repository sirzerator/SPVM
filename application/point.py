#!/usr/bin/python
# -*- coding: utf-8 -*-
from application.model import Model


class Point(Model):
	def __init__(self, db):
		self.table = 'point'
		self.rows = [
			'id',
			'pv_id',
			'parent_id',
			'title',
			'description',
			'rank'
		]
		self.validation = {
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
					'type': int,
					'default': 0,
					'required': True
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
			'subpoints': {
				'table':'point',
				'key':'parent_id',
				'delete':'cascade',
				'update':None
			}
		}
		self.old_description = '''
			CREATE TABLE  IF NOT EXISTS "point" (
				"id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
				"pv_id" INTEGER NOT NULL,
				"parent_id" INTEGER,
				"title" TEXT NOT NULL,
				"description" TEXT,
				"rank" INTEGER DEFAULT 0
			)
		'''
		
		super(Point, self).__init__(db)
		
	def get_numbering(self, point_id):
		numbering = ""
		
		point = self.retrieve_one(where={'id': point_id})
		
		if point['parent_id'] != "0" and point['parent_id'] != "":
			numbering += str(self.get_numbering(point['parent_id']))
			
			all_points = self.retrieve(where={'pv_id': point['pv_id'], 'parent_id': point['parent_id']}, order='rank ASC', recursion=0)
			
			point_number = 1
			print(all_points)
			for point in all_points['rows']:
				if point['id'] != point_id:
					point_number += 1
				else:
					break;
						
			numbering += str(point_number) + '.'
		else:
			all_points = self.retrieve(where={'pv_id': point['pv_id'], 'parent_id': ""}, order='rank ASC', recursion=0)
			
			point_number = 1
			print(all_points)
			for point in all_points['rows']:
				if point['id'] != point_id:
					point_number += 1
				else:
					break;
					
			numbering += str(point_number) + '.'
		
		return numbering
