# Twelve Days of Christmas

# Write a program to produce the lyrics (all 12 verses) of the Twelve Days of Christmas. This is a cumulative song as each verse is build on top of the previous verses.  You must
# have a loop for the verses,build up each of the verses within a loop (or switch statement),use at least one switch statement in your solution,
# only write the lines of text (or constants representing them) from the song once in your program
# (e.g. you cannot have more than one statement in the entire program which prints out "my true love sent to me")... 

# On the first day of Christmas
# my true love sent to me:
# a Partridge in a Pear Tree. 
# On the second day of Christmas
# my true love sent to me:
# 2 Turtle Doves
# and a Partridge in a Pear Tree. 
# On the third day of Christmas
# my true love sent to me:
# 3 French Hens,
# 2 Turtle Doves
# and a Partridge in a Pear Tree
#  ...


ordinals = ["first" , "second" , "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth", "tenth", "eleventh", "twelfth"]
lines = ["A partridge in a pear tree", "Two turtle doves", "Three french hens", "Four calling birds", "Five gold rings", "Six geese a laying", 
"Seven swans a swimming", "Eight maids a milking", "Nine ladies dancing", "Ten lords a leaping", "Eleven pipers piping", "Twelve drummers drumming"]
index = [0]

for ordinal in ordinals:
	print(f"On the {ordinal} day of Christmas\nMy true love send to me:")
	for num in index:
		print(lines[num])
	# add value to front of index list >>> [0] >>> [1, 0] >>> [2, 1, 0]
	index.insert(0, index[0]+1)
	# adjust the last line of the verse
	if len(index) == 1:
		lines[0] = "And a partridge in a pear tree"
	print("\n")

