from pymongo import MongoClient

dbIP = 'localhost'
dbPort = 27017

client = MongoClient(dbIP, dbPort)
db = client['pythonDB']
hptable = db['hasheet']
flashtable = db['flasheet']
extable = db['extable']

def addHash():
	pass

def hashExists(para):
	pass

def compareHash():
	pass