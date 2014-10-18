from nltk.corpus import wordnet
import sys

sys.argv.append(1)
sys.argv.append("King Iain ruled from 1808-1809")
sys.argv.append("Kings,Iain")

# Doc ID | Doc | Tags
# int    | Str | Str[]

def main():
	# Get system arguments
	docID = sys.argv[1]
	docText = sys.argv[2]
	docTags = sys.argv[3]
	# Split text into array of strings
	words = splitWords(docText)
	# Get Lexnames for words
	print getLexNames(words[0])[0]

def splitWords(phrase):
	return phrase.split(" ")

def getLexNames(word):
	a = []
	for synset in wordnet.synsets(word):
		a.append(synset.lexname().split(".")[0])
	return a

if __name__ == "__main__":
	main()