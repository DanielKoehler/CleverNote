from nltk.corpus import wordnet
from docToPara import docToPara
from paraToSentence import paraToSentence
from isQueriable import isQueriable

import sys
import re

sys.argv.append(1)
sys.argv.append("King Iain ruled from 1808-1809 \n it's a terrible time")
sys.argv.append("Kings,Iain")

# Doc ID | Doc | Tags
# int    | Str | Str[]

def main():
	# Get system arguments
	docID = sys.argv[1]
	docText = sys.argv[2]
	docTags = sys.argv[3]
	docFlash = []
	docKeys = [] + list(docTags)

	#break document into paragraphs
	pArray = docToPara(docText)

	#store hash of paragraphs
	#not sure how to implement just yet

	#for each paragraph
	for p in pArray:
		#break paragraph into sentences
		sArray = paraToSentence(pArray)

		#for each sentence
		for s in sArray:
			#see if the sentence is even reasonably questionable
			if isQueriable(s):


				#try and form a question and add it to the collection of flash cards
				docFlash.append(analyseSentence(s))
	

	

if __name__ == "__main__":
	main()