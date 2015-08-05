'''
	Python Dice Poker.
	A Python program recreating the dice poker game from The Witcher
	Final verison should allow multiple players and AI players.
'''
import random
import string
# AI constants
HUMAN = True
AI = False

# 'hand' value constants
NOTHING = 0
PAIR = 1
TWOPAIR = 2
THREEOFKIND = 3
FIVEHIGHSTRAIGHT = 4 # dice 1-5 inclusive
SIXHIGHSTRAIGHT = 5 # dice 2-6 inclusive
FULLHOUSE = 6 # Pair + 3of Kind
FOUROFKIND = 7
FIVEOFKIND = 8

class Die(object):
	# Represents a single die in the game.

	def __init__(self):
		self.value = -1 # What the die 'reads' what it has been rolled as.
		self.needRoll = True # determines if a die needs a roll or not. Allows all dice to have the roll() call but only dice that need it get changed.

	# rolls the die setting it's value to a random int between 1 and 6.
	def roll(self):
		if self.needRoll:
			self.value = random.randint(1,6)
			self.needRoll = False

class Player(object):
	# A player in the dice poker game, can be human or AI

	def __init__(self, humanity, name):
		self.name = name # the name of the player.
		self.isHuman = humanity # determines if the player is AI or human
		self.dice = [Die() for i in range(5)] # The five die that the player has

	def report(self): # prints out the current dice the player has
		print self.name + " dice are:"
		diceNum = 1
		for die in self.dice:
			print "Die " + str(diceNum) + ": [" + str(die.value) + "],",
			diceNum += 1

	def makeRolls(self, rollsNeededStr = ''): # setups certain dice to be specificly rolled and sends roll commands to all dice.
		rollsNeeded = []
		for char in rollsNeededStr:
			if char in string.digits and int(char) in range(1,6):
				rollsNeeded.append(self.dice[int(char) - 1])
		for die in rollsNeeded:
			die.needRoll = True
		for die in self.dice:
			die.roll()

	def score(self):
		#funtion that takes a list of die and returns a score based off the dice
		numPairs = 0
		trip = False

		# Five of Kind Check
		five = True
		checkVal = self.dice[0].value
		for die in self.dice[1::]:
			if die.value != checkVal:
				five = False
				break
		if five == True:
			return FIVEOFKIND

		# Four of Kind/Full House/Trips/Pair Check
		count = 0
		for die1 in self.dice:
			for die2 in self.dice:
				if die1.value == die2.value:
					count += 1
			if count == 4:
				return FOUROFKIND
			if count == 3:
				trip = True
			if count == 2:
				numPairs += 1
			count = 0
		if trip and numPairs == 2:
			return FULLHOUSE
		if trip:
			return THREEOFKIND
		if numPairs == 4:
			return TWOPAIR
		if numPairs == 2:
			return PAIR

		# six or five high straight (2-6)/(1-5) check
		diceVals = []
		for die in self.dice:
			diceVals.append(die.value)
		diceVals.sort()
		if diceVals == range(2,7):
			return SIXHIGHSTRAIGHT
		if diceVals == range(1,6):
			return FIVEHIGHSTRAIGHT

		return NOTHING

#testing stuff
me = Player(HUMAN,"Kyle")
me.makeRolls()
me.report()
print "Your score is:", me.score()


