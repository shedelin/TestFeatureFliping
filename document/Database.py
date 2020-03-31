from pymongo import MongoClient

class MongoDatabase():

	new = True

	def __init__(self):
		if self.new:
			mongo    = MongoClient('mongodb+srv://adminMiaou:miaoupass@cluster0-igq1s.mongodb.net/test?retryWrites=true&w=majority')
			self.db  = mongo.featureFlipping
			self.new = False
