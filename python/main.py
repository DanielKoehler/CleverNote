from nltk.corpus import wordnet
from docToPara import docToPara
from paraToSentence import paraToSentence
from isQueriable import isQueriable
from analyseSentence import analyseSentence
from searchKeywords import searchKeywords
<<<<<<< HEAD
from pymongo import MongoClient
=======
>>>>>>> 33eb2582530880fd8534f048843bcbfd05385bca
import db
import sys
import re
import hashlib

sys.argv.append(1)
sys.argv.append("King Iain ruled from 1808-1809 \n it's a terrible time \n there is little hope")
sys.argv.append("Kings,Iain")

<<<<<<< HEAD

# Doc ID | Doc | Tags
# int    | Str | Str[]

=======
>>>>>>> 33eb2582530880fd8534f048843bcbfd05385bca
def main():
	# Get system arguments
	docID = sys.argv[1]
	docText = sys.argv[2]
	docTags = sys.argv[3]
	docFlash = []
	docKeys = docTags.split(",")

	#break document into paragraphs
	pArray = docToPara(docText)

	#for each paragraph

	for p in pArray:
		if db.hashExists(p):
			pass

		else:

			#store hash of paragraphs
			#addHash(docID,hashlib.md5(p))

			#break paragraph into sentences
			sArray = paraToSentence(p)

			#for each sentence
			for s in sArray:
				#see if the sentence is even reasonably questionable
				if isQueriable(s):

					#find nouns and add them to the keywords array
					docKeys += searchKeywords(s)


					#try and form a question and add it to the collection of flash cards
					docFlash.append(analyseSentence(s))
			#add questions to DB


	print docKeys

if __name__ == "__main__":
	main()