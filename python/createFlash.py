import re
from searchKeywords import searchKeywords
from searchKeywords import checkForDate
from searchKeywords import hasDateIn
from searchKeywords import searchAdjective
from searchKeywords import searchAdverb

def createFlash(sentence):
	#split either side of the queriable word
	words = ["is","isn't","was","wasn't","can","can't"]

	questAns= re.split(' was | wasn\'t | is | isn\'t | can | can\'t | could | couldn\'t ',sentence)

	if "was" in sentence:
		if questAns[0].lower() != "what":
			if questAns[0].lower() == "there":
				subject = "the " + questAns[1].split(" ")[1]
				toCheck = questAns[1].replace(subject, "")
			else:
				subject = questAns[0]
				toCheck = questAns[1]
			tmp = searchKeywords(toCheck)
			if len(tmp) > 0:
				if subject == "I":
					question = "Was I " + tmp[0] + "?"
					if "not" in sentence.split(" "):
						answer = "false"
					else:
						answer = "true"
				else:
					question = "Was " + subject + " a " + tmp[0] + "?"
					if "not" in sentence.split(" "):
						answer = "false"
					else:
						answer = "true"
			else:
				question = "What was " + subject.split(" ")[-1]+ " " + questAns[1].split(" ")[1] + "?"
				if "not" in sentence.split(" "):
					answer = "this"
				else:
					answer = "not this"
			if hasDateIn(questAns[1]):
				tmp = checkForDate(questAns[1])
				question = "When was " + subject + "?"
				answer = tmp
			

	if "is" in sentence:
		if questAns[0].lower() != "what":
			subject = questAns[0]
			toCheck = questAns[1]
			tmp = searchKeywords(toCheck)
			if len(tmp) > 0:
				if len(searchAdjective(toCheck)) > 0:
					question = "Is " + subject + " the " + searchAdjective(toCheck)[-1] + " "+ tmp[-1] + "?"
					if "not" in sentence.split(" "):
						answer = "false"
					else:
						answer = "true"
				else:
					if subject.lower() == "there":
						subject = tmp[0]
						question = "Is there a " + subject + "?"
						if "not" in sentence.split(" "):
							answer = "false"
						else:
							answer = "true"
					else:
						question = "Is " + subject + " a "+ tmp[-1] + "?"
						if "not" in sentence.split(" "):
							answer = "false"
						else:
							answer = "true"
			else:
				tmp = searchAdjective(toCheck)
				question = "Is " + subject + " " + tmp[-1] + "?"
				if "not" in sentence.split(" "):
					answer = "false"
				else:
					answer = "true"


	if "can" in sentence:
		if questAns[0].lower() != "what":
			subject = questAns[0]
			toCheck = questAns[1]
			tmp = searchAdverb(toCheck)
			if len(tmp) < 1:
				tmp = searchKeywords(toCheck)
			question = "What can " + subject + " do?"
			answer = tmp
			
	if "could" in sentence:
		if questAns[0].lower() != "what":
			subject = questAns[0]
			toCheck = questAns[1]
			tmp = searchAdverb(toCheck)
			if len(tmp) < 1:
				tmp = searchKeywords(toCheck)
			question = "What could " + subject + " do?"
			answer = tmp

			
	
	return {"question":question, "answer":answer}



createFlash("Birds could fly")
createFlash("24-Hours at TechCrunch could kill you")

createFlash("Birds could fly")
createFlash("24-Hours at TechCrunch could kill you")

createFlash("The Sky is blue")
createFlash("Helium is the first element")
createFlash("Pete is a dick")
createFlash("There is an elephant in the room")

createFlash("Iain was a great king")
createFlash("There was a war in the year 2003")
createFlash("Pete Davison was born on the 1st Oct")
createFlash("The 2nd World War was in 1939")
createFlash("That really was not fun")
createFlash("I was evil")