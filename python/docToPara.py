import re

def docToPara(docText):
	return re.split("\n", docText)
