# High Scores

# Write a program to maintain a list of the high scores obtained in a game.
# The program should first ask the user how many scores they want to maintain and 
# then repeatedly accept new scores from the user and should add the score to the list of high scores (in the appropriate position) if it is higher than any of the existing high scores.
# You must include the following functions:
# initialiseHighScores () which sets all high scores to zero.
# printHighScores() which prints the high scores in the format: “The high scores are 345, 300, 234”, for all exisiting high scores in the list (remember that sometimes it won’t be full).
# higherThan() which takes the high scores and a new score and returns whether the passed score is higher than any of those in the high score list.
# insertScore() which takes the current high score list  and a new score and updates it by inserting the new score at the appropriate position in the list


def initialise_high_scores():
	n = int(input("Enter the number of high scores to maintain: "))
	high_scores = [0] * n
	return high_scores

def print_high_scores(high_scores):
	current_scores = [str(score) for score in high_scores if score != 0]
	print("The high scores are " + ", ".join(current_scores))

def insert_score(high_scores, new_score):
	for score in high_scores:
		if new_score > score:
			high_scores.append(new_score)
			high_scores.sort()
			high_scores = high_scores[::-1]
			high_scores.pop(-1)
			break
	return high_scores

high_scores = initialise_high_scores()
while True:
	new_score = int(input("Enter the next high score: "))
	high_scores = insert_score(high_scores, new_score)
	print_high_scores(high_scores)

