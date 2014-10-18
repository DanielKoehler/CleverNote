from nltk.corpus import wordnet as wn
import nltk

def main():
	tockens = nltk.word_tokenize("King Iain can rule")
	text = nltk.Text(tockens)
	tags = nltk.pos_tag(text)

	print tags

def wordType(word):
	return wn.synsets(word)[0].lexname().split(".")[0]


if __name__ == "__main__":
	main()
