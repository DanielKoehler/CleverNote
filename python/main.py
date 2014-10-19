from nltk.corpus import wordnet
from docToPara import docToPara
from paraToSentence import paraToSentence
from isQueriable import isQueriable
from analyseSentence import analyseSentence
from searchKeywords import searchKeywords
from pymongo import MongoClient
from createFlash import createFlash
import db
import sys
import re
import hashlib

sys.argv.append(1)
sys.argv.append("King Iain ruled from 1808-1809 \n it's a terrible time \n there is little hope")
sys.argv.append("Kings,Iain")


# Doc ID | Doc | Tags
# int    | Str | Str[]

def main():
	# Get system arguments
	docID = sys.argv[1]
	docText = sys.argv[2]
	docKeys = sys.argv[3].split(',')
	docFlash = []

	#break document into paragraphs
	pArray = docToPara(docText)

	#for each paragraph
	for p in pArray:
		paraFlash = []

		#hash the paragraph
		hashedPara = hashlib.md5(p).hexdigest()

		#if we've scanned the paragraph before
		if db.hashExists(hashedPara):

			#retreive saved data for paragraph
			paraFlash = db.getFlash(hashedPara)
			paraExt = db.getXtra(hashedPara)

		else:

			#store hash of paragraphs
			db.addHash(hashedPara)

			#break paragraph into sentences
			sArray = paraToSentence(p)

			#for each sentence
			for s in sArray:
				#see if the sentence is even reasonably questionable
				if isQueriable(s):

					#find nouns and add them to the keywords array
					docKeys += searchKeywords(s)


					#try and form a question and add it to the collection of flash cards
					paraFlash.append(createFlash(s))
			#add questions to DB
		for flash in paraFlash:
			db.addFlash(hashedPara, flash)
		docFlash += paraFlash
	return docFlash


if __name__ == "__main__":
	main()