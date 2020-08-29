# Hi-Lo Card Game
# USING A WHILE OR A DO-WHILE LOOP write a program which allows
# the user to play the Hi-Lo Card game:

# The Hi-Lo card game is one where the user is presented with an initial card
# (2 – 10, Jack, Queen, King, or Ace) 
# and has to guess that the next card with be 
# Higher (Hi), Lower (Lo) or Equal to the current card.
# They must guess successfully 4 times in a row in order to win.
import random
import sys

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

# CREATE CARD CLASS
class Card():
	def __init__(self, suit, rank):
		self.rank = rank
		self.suit = suit
		self.value = values[self.rank]

	def __str__(self):
		return f"{self.rank} of {self.suit}"


# CREATE DECK CLASS
class Deck():
	def __init__(self):
		# empty deck
		self.deck = []
		# fill deck
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))

	def __str__(self):
		deck_print = []
		for card in self.deck:
			deck_print.append(card.__str__())
		return str(deck_print)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

def user_guess():
	guess = input("Will the next card be higher (h), lower (l), equal (e): ")
	if guess == "exit":
		sys.exit()
	return guess


deck = Deck()
deck.shuffle()
last_card = deck.deal()
print(f"Last was card: {last_card.__str__()}")
correct_guesses = 0
while True:
	next_card = deck.deal()
	print(next_card.__str__())
	guess = user_guess()
	print(f"Last card was: {next_card.__str__()}")
	if next_card.value > last_card.value and guess == 'h':
		print("CORRECT")
		correct_guesses += 1
	elif next_card.value < last_card.value and guess == 'l':
		print("CORRECT")
		correct_guesses += 1
	elif next_card.value == last_card.value and guess == 'e':
		print("CORRECT")
		correct_guesses += 1
	else:
		print("INCORRECT")
		correct_guesses = 0

	last_card = next_card
	print(f"Correct guesses: {correct_guesses}")
	if correct_guesses == 4:
		print("WINNER!")
		break
