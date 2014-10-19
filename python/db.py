from pymongo import MongoClient

dbIP = 'localhost'
dbPort = 27017

client = MongoClient(dbIP, dbPort)
db = client['pythonDB']

def addFlash(hashStr, flash):
	flashTable = db['flash']	
	flashTable.insert({"hashStr": hashStr, "flash": flash})

def addXtra(hashStr, data):
	xtraTable = db['xtra']	
	xtraTable.insert({"hashStr": hashStr, "data": data})

def addHash(hashStr):
	hpTable = db['hp']	
	hpTable.insert({"hashStr": hashStr})

def getFlash(hashStr):
	a = []
	flashTable = db['flash']
	for r in flashTable.find({"hashStr": hashStr}):
		a.append(r['flash'])
	return a

def getXtra(hashStr):
	a = []
	xtraTable = db['xtra']
	for r in xtraTable.find({"hashStr": hashStr}):
		a.append(r['data'])
	return a

def hashExists(hashStr):
	hpTable = db['hasheet']
	r = hpTable.findOne({"hashStr": hashStr})
	if r == None:
		return False
	else:
		return True

def compareHash(hashStr1, hashStr2):
	if hash1 == hash2:
		return True
	else:
		return False