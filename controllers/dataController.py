
from modules import *

class logData(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		timeStamp = time.time()
		timeOfLogging = datetime.datetime.fromtimestamp(timeStamp).strftime('%Y-%m-%d %H:%M:%S') 
		temperature = self.get_argument('temperature','')
		air_quality = self.get_argument('air_quality','')
		if temperature!='' and air_quality!='':
			yield db.logs.insert({
				'temperature' : temperature,
				'air_quality' : air_quality,
				'time' 		  : timeOfLogging
				})
			self.write(tornado.escape.json_encode({
				'status' : 200,
				'message' : 'Data logged successfully'
				}))
		else:
			self.write(tornado.escape.json_encode({
				'status' : 400,
				'message': 'Parameters missing'
				}))

'''
Class to return JSON of logged data
'''

class showData(tornado.web.RequestHandler):
	@tornado.gen.coroutine
	def get(self):
		data = yield db.logs.find({}).to_list(None)
		print data
		self.write(dumps(data))
