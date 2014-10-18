import nltk

tokens = nltk.word_tokenize("King Iain can rule")
text = nltk.Text(tokens)
tags = nltk.pos_tag(text)

return tags