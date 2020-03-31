from document import Database
from bson.objectid import ObjectId

Md         = Database.MongoDatabase()
db         = Md.db
dbFeatures = db.Features

class Feature:
	_name        = ''
	_state_us 	 = 'deactivate'
	_state_en 	 = 'deactivate'
	_state_de 	 = 'deactivate'
	_state_cl 	 = 'deactivate'
	_state_fi 	 = 'deactivate'
	_state_it 	 = 'deactivate'
	_state_jp 	 = 'deactivate'
	_state_es 	 = 'deactivate'
	_state_ru 	 = 'deactivate'
	_state_fr 	 = 'deactivate'
	_new_feature = True

	def __init__(self, feature_id=None):
		if None != feature_id:
			self._id         = ObjectId(feature_id)
			self._new_feature = False

			self._populate()

	def commit(self):
		print(self._new_feature)
		if self._new_feature:
			print("create new");
			dbFeatures.insert({
				'name':   		self._name,
				'state_us':  	self._state_us,
				'state_en':  	self._state_en,
				'state_de':  	self._state_de,
				'state_cl':  	self._state_cl,
				'state_fi':  	self._state_fi,
				'state_it':  	self._state_it,
				'state_jp':  	self._state_jp,
				'state_es':  	self._state_es,
				'state_ru':  	self._state_ru,
				'state_fr':  	self._state_fr,
			})
			self._id = dbFeatures.find_one({'name': self._name})['_id']
		else:
			print("update")
			dbFeatures.update({'_id': ObjectId(self._id)}, {
				'name':   		self._name,
				'state_us':  	self._state_us,
				'state_en':  	self._state_en,
				'state_de':  	self._state_de,
				'state_cl':  	self._state_cl,
				'state_fi':  	self._state_fi,
				'state_it':  	self._state_it,
				'state_jp':  	self._state_jp,
				'state_es':  	self._state_es,
				'state_ru':  	self._state_ru,
				'state_fr':  	self._state_fr,
			})

	def _populate(self):
		feature      = 		dbFeatures.find_one({'_id': ObjectId(self._id)})
		self._name   = 		feature['name']
		self._state_us = 	feature['state_us']
		self._state_en = 	feature['state_en']
		self._state_de = 	feature['state_de']
		self._state_cl = 	feature['state_cl']
		self._state_fi = 	feature['state_fi']
		self._state_it =	feature['state_it']
		self._state_jp = 	feature['state_jp']
		self._state_es = 	feature['state_es']
		self._state_ru = 	feature['state_ru']
		self._state_fr = 	feature['state_fr']

	def getId(self):
		return str(self._id)

	def toArray(self):
		result = {
			'_id':    		self.getId(),
			'name':   		self._name,
			'state_us':  	self._state_us,
			'state_en':  	self._state_en,
			'state_de':  	self._state_de,
			'state_cl':  	self._state_cl,
			'state_fi':  	self._state_fi,
			'state_it':  	self._state_it,
			'state_jp':  	self._state_jp,
			'state_es':  	self._state_es,
			'state_ru':  	self._state_ru,
			'state_fr':  	self._state_fr,
		}

		return result

	def getStates(self):
		result = {
			'US':  	self._state_us,
			'EN':  	self._state_en,
			'DE':  	self._state_de,
			'CL':  	self._state_cl,
			'FI':  	self._state_fi,
			'IT':  	self._state_it,
			'JP':  	self._state_jp,
			'ES':  	self._state_es,
			'RU':  	self._state_ru,
			'FR':  	self._state_fr,
		}

		return result
