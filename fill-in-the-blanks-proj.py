# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


#sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
#adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
#don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
#tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd-1-1/20min/

attempts = 0

attemptsMax = 5

difficulty = ""

questNum = 0

numQuests = 0

sample = ""

words = []

easyWords = ["Mirko", "Randy", "laser", "window"] 

mediumWords = ["Giant", "Slam", "Warrior", "Fund"]

hardWords = ["Rage", "Axel", "X", "Tooth"]

easySample = "My first cat's name is __1__.  He is named after an MMA fighter from Croatia nicknamed CroCop'.  He is often called '__1__ Crocop', but his real name is '__1__ Filipovic'. My second cat's name is __2__.  He is named after an MMA fighter named '__2__ Couture'. \n \n  __2__ likes to chase the red dot projected from the __3__ pointer.  He likes it so much, that whenever I reach for the __3__ pointer from the pen jar, he runs over towards my desk and gets ready to chase the red dot. \n \n  Even though they are indoor cats, they really enjoy looking out the __4__ at the birds and trees outside."

mediumSample = "In 1987, Hulk Hogan faced Andre the __1__ to defend his WWF World Heavyweight Championship Belt.  It was a tremendous feat of strength when Hulk Hogan performed a scoop __2__ on Andre the __1__.  I never thought he would be able to pick Andre up to __2__ him.   \n \n  Another exciting match in WrestleMania history was when Hulk Hogan faced The Ultimate __3__ in WrestleMania VI.  \n \n (interesting tidbit:  the WWF was later renamed to 'WWE' after they were sued by the 'World Wildlife __4__') "

hardSample = "In the 1992 Sega Genesis hit 'Streets of __1__ 2', you played as either __2__, Max, Blaze, or Skate.  You fought through multiple levels to try and take down the syndicate, led by 'Mr. __3__'.   \n \n  Another videogame series that features a character named __2__ is the 'Twisted Metal' series, which is a vehicular combat game.  In the Twisted Metal games, __2__ is a wierd vehicle hybrid, where he is standing between 2 huge tires.   My favorite game out of the Twisted Metal series (and one of the greatest games of all time IMO) is 'Twisted Metal 2'.  The end boss in Twisted Metal 2 is 'Dark __4__'.  Twisted Metal 2 also features a character named 'Sweet __4__', who I preferred not to use. "

blanks = []

gameOver = False

suppliedWord = ""

#Draw__ functions defined below handle repetitive cosmetic output

def DrawMenu(title):
	sideBorder = "|  "
	numHorizDashes = len(title) + (len(sideBorder)*2)
	print "-" * numHorizDashes
	print sideBorder +title+ sideBorder[::-1]#reverse string code found here:http://stackoverflow.com/questions/931092/reverse-a-string-in-python
	print "-" * numHorizDashes
	return None

	
def DrawDashes(numDashes):
	print "-" * numDashes
	return None

	
def DrawGameWon(endMessage):
	print "\n" *2
	DrawDashes(60)
	print sample
	DrawDashes(60)
	DrawMenu(endMessage)
	return None

#populate the list of blanks based on the specified number of blanks. 
def PopulateBlanks(numBlanks):	
	i = 0
	while i < numBlanks:
		blanks.append("__" +str((i+1))+ "__")		
		i += 1
	return None


def ChooseDiff():		
	selectedDiff = ""
	while selectedDiff == "":
		print " \n Select a difficulty: \n Easy | Medium | Hard \n"
		DrawDashes(6)
		userInput = ""
		userInput = raw_input(userInput)
		userInput = userInput.lower()
		if userInput == "easy" or userInput == "medium" or userInput == "hard":
			selectedDiff = userInput
			print "difficulty selected is " +selectedDiff 
			SetSample(selectedDiff) #set sample based on difficulty 
			SetWords(selectedDiff) #assign words list based on difficulty 
			DrawDashes(6)			
		else:
			print "That is not a valid selection."
			DrawDashes(6)			
	return selectedDiff

	
def PromptUser(questNum):
	print "\n" * 2
	DrawDashes(60)
	print sample
	DrawDashes(60)
	print "\n"
	print "Please input a word for " +blanks[questNum]
	suppliedWord = ""
	return raw_input(suppliedWord)

#check if supplied word matches an item in words[], based on questNum	
def CheckSupplied(suppliedWord):
	if suppliedWord.lower() == words[questNum].lower():
		DrawDashes(6)
		print " \n correct!  the word is: " +words[questNum]
		return True
	else:
		DrawDashes(6)
		print "\n wrong!"
		return False
	return None
#detect if the supplied string matches an item in blanks[] based on questNum		
def CheckIfBlank(word):
	if blanks[questNum] in word:
		#return words[questNum]
		return blanks[questNum]
	return None

#replace specific blanks with specific words, based on current questNum
def ReplaceBlanks(ml_string, parts_of_speech):    
	replaced = []
	origList = ml_string.split(" ")	
	for i in origList:
		if CheckIfBlank(i) != None:
			newWord = i.replace(CheckIfBlank(i), words[questNum])
			replaced += " " +newWord
		else:
			replaced += " " +i
	return "".join(replaced)

#assign sample based on specified difficulty
def SetSample(difficulty):
	global sample
	if difficulty == "easy":
		sample = easySample
	elif difficulty == "medium":
		sample = mediumSample
	elif difficulty == "hard":
		sample = hardSample
	return None

#assign words[] list based on specified difficulty
def SetWords(difficulty):
	global words
	global numQuests
	
	if difficulty == "easy":
		words = easyWords
	elif difficulty == "medium":
		words = mediumWords
	elif difficulty == "hard":
		words = hardWords
	numQuests = len(words)
	PopulateBlanks(numQuests)
	return None

DrawMenu("Fill In The Blanks Game!")
	
difficulty = ChooseDiff()

while gameOver == False:
	suppliedWord = PromptUser(questNum)
	
	#if supplied word matches the word for this questNum:
	if CheckSupplied(suppliedWord) == True:
		#replace the blanks for this questNum with the words for this questNum
		sample = ReplaceBlanks(sample, words)		
		questNum += 1
		#if reached the total number of questions, you won, end game:
		if questNum == numQuests:
			DrawGameWon("*StreetFighter2Voice* YOU WIN!")
			gameOver = True
	#else supplied word doesn't match the word for this questNum:
	else:
		attempts += 1
		#if the current attempts count is less than maximum attempts, notify user & end game:
		if attempts < attemptsMax:
			DrawDashes(6)
			print "\n You have " +str((attemptsMax - attempts))+ " attempts left"
		#else attempts have surpassed maximum attempts, notify user & end game:
		else:
			DrawMenu("*StreetFighter2Voice* You Lose")
			gameOver = True
print "\n" * 2
print "Thanks for playing!"