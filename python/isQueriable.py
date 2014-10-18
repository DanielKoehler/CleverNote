#is going to guess the likelyhood that a sentence is queriable
#based on if the sentences contain a collection of words
def isQueriable(sentenceText):
	for word in words:
		if word in sentenceText.split(" "):
			return true
		else:
			return false