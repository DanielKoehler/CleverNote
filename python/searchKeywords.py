from analyseSentence import getLexical

def searchKeywords(sentence):
	a = []
	for word in getLexical(sentence):
		if word[1] == "NN":
			a.append(word[0])
	return a