'''This code shuffles a pack of cards, deals two cards to n players
and reveals the whole board and the hands of the players'''

# Creating a pack of cards

suit = 'c s d h'.split()
pic = [str(x) for x in range(2, 11)] + 'J Q K A'.split()
deck = []
for p in range(len(pic)):
	for s in suit:
		deck.append(pic[p] + s)

# Shuffling and dealing

import random

def pokerdeal(n):
	random.shuffle(deck)
	first = deck[:n]
	second = deck[n:n*2]
	for cards in range(n):
		hands[cards].append(first[cards])
		hands[cards].append(second[cards])
	return hands
	
players = int(input("Input the number of players: "))
hands = [[] for x in range(players)]
for i in sorted(pokerdeal(players)):
  print(i, '\n')
ostatok = deck[:players] + deck[players:players*2]	# что мы взяли в сумме из колоды
deck = [d for d in deck if d not in ostatok]

# Dealing the board

flop = deck[1] + ' ' + deck[2] + ' ' + deck[3]
turn = deck[5]
river = deck[7]
input("\n" + "Press Enter to view the board" + "\n")
print(flop, turn, river, sep = '\n')
