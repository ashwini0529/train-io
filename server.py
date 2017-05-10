
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
import torn

from routes import *
#Initialize database

from motor import MotorClient
db = MotorClient('mongodb://root:helloworld@ds023442.mlab.com:23442/train-io')['train-io']

settings = dict(
		debug=torn.Debug(),
		db=db
	)

application = Application(route, **settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(torn.Port())
	IOLoop.current().start()

					