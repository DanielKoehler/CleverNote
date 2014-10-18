import re

def paraToSentence(paraText):
	return re.split('\.|\?|\!', paraText)