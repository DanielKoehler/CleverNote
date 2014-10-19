import nltk
import re

def searchKeywords(sentence):
	a = []
	for word in getLexical(sentence):
		if "NN" in word[1]:
			a.append(word[0])
	return a

def getLexical(sentence):
	tokens = nltk.word_tokenize(sentence)
	text = nltk.Text(tokens)
	tags = nltk.pos_tag(text)

	return tags

def hasDateIn(sentence):
	words = ["Jan","Feb","Mar","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
	for sentSplit in sentence.split(" "):
		for word in words:
			if word in sentSplit:
				return True
	match = re.search(r'\d{4}', sentence)
	if match == None:
		return False
	else:
		return True

def checkForDate(sentence):
	words = ["Jan","Feb","Mar","April","May","June","July","Aug","Sept","Oct","Nov","Dec"]
	for sentSplit in sentence.split(" "):
		for word in words:
			if word in sentSplit:
				return word
	match = re.search(r'\d{4}', sentence)
	return match.group()

def searchAdjective(sentence):
	a = []
	for word in getLexical(sentence):
		if "JJ" in word[1]:
			a.append(word[0])
	return a

def searchAdverb(sentence):
	a = []
	for word in getLexical(sentence):
		if "RB" in word[1]:
			a.append(word[0])
	return a
	