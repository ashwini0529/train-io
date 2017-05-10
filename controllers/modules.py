
'''
Middleware for controller to contain all the modules
'''
import tornado.web
import tornado.escape
import time
from bson.json_util import dumps
import datetime
from motor import MotorClient
db = MotorClient('mongodb://root:helloworld@ds023442.mlab.com:23442/train-io')['train-io']
