from bottle import request

class REST_Service:
	def __init__(self, service_root=None, api_major_version=None):
		self.service_root = "api" if service_root is None else service_root
		self.api_major_version = api_major_version if api_major_version is not None else "v1"

		self.get.__dict__['route'] = "/" + self.service_root + "/" + self.api_major_version + "/" + self.service_name + "/"
		self.get.__dict__['method'] = 'GET'

		self.get_one.__dict__['route'] = "/" + self.service_root + "/" + self.api_major_version + "/" + self.service_name + "/<pv_id>"
		self.get_one.__dict__['method'] = 'GET'

	### GET
	def get(self):
		where = dict()
		for query_parameter in request.query.items():
			print(query_parameter)
			where[query_parameter[0]] = query_parameter[1]
		return self.service_hook.retrieve(where=where, recursion=0)

	def get_one(self, pv_id):
		return self.service_hook.retrieve(where={'id':pv_id}, recursion=0)['rows'][0]

	### PUT

	### POST

	### DELETE
