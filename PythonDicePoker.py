'''
	Python Dice Poker.
	A Python program recreating the dice poker game from The Witcher
	Final verison should allow multiple players and AI players.
'''
import random
HUMAN = True
AI = False

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

	def makeRolls(self, rollsNeeded = []): # setups certain dice to be specificly rolled and sends roll commands to all dice.
		for die in rollsNeeded:
			die.needRoll = True
		for die in self.dice:
			die.roll()

#testing stuff
print "But then changed it back in Mac OS"
me = Player(HUMAN,"Kyle")
me.makeRolls()
me.report()
me.makeRolls([me.dice[0],me.dice[4]])
me.report()


