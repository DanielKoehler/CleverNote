import nltk

def getLexical(sentence):
	tokens = nltk.word_tokenize(sentence)
	text = nltk.Text(tokens)
	tags = nltk.pos_tag(text)

	return tags

def analyseSentence(sentence):
	pass
