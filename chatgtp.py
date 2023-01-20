import random

#list of words to be used in the game
words = ["python", "programming", "language", "computer", "science"]

#randomly select a word from the list
word = random.choice(words)

#create a variable to keep track of the correct guesses
correct_guesses = []

#create a variable to keep track of the wrong guesses
incorrect_guesses = []

#create a variable to keep track of the number of lives
lives = 6

#create a while loop to keep the game running until the player runs out of lives
while lives > 0:
    #create a variable to keep track of the progress of the word
    progress = ""
    for letter in word:
        if letter in correct_guesses:
            progress += letter
        else:
            progress += "_"
    print(progress)
    print("Lives: " + str(lives))
    print("Incorrect guesses: " + " ".join(incorrect_guesses))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        correct_guesses.append(guess)
    else:
        incorrect_guesses.append(guess)
        lives -= 1
    if "_" not in progress:
        print("Congratulations, you won! The word was " + word)
        break

if lives == 0:
    print("You lost! The word was " + word)
