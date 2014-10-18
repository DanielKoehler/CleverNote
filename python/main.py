from nltk.corpus import wordnet
import sys
import re

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

	

if __name__ == "__main__":
	main()