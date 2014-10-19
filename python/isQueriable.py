#is going to guess the likelyhood that a sentence is queriable
#based on if the sentences contain a collection of words
def isQueriable(sentenceText):
	words = ["is","isn't","was","wasn't","can","can't"]
	queriable = False
	for word in words:
		if word in sentenceText.split(" "):
			queriable = True
	return queriable