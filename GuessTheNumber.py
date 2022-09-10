import os
import random

# Clear Console
os.system('clear')

# Variable Declaration
lowerBound = random.randint(0,50)
upperBound = lowerBound + random.randint(10,50)
answerNum  = random.randint(lowerBound,upperBound)
guesses    = 0
maxguesses = 5

print("Guess the number: A fun little game!\n")
print("It's between " + 
    str(lowerBound) + " and " + 
    str(upperBound) + "!\n")

while (guesses < maxguesses):
    # Let them know how many guesses they have left
    print("Guesses left: " + str(3 - guesses) + "\n")

    # Ask for an answer
    theGuess = int(input("Your guess: "))
    print()
    
    # Logic for game

    # If we are out of bounds, tell them and return their guess count!
    if (theGuess < lowerBound or theGuess > upperBound ):
        print("That's out of bounds! It's between " + 
            str(lowerBound) + " and " + 
            str(upperBound) + "!\n")
        continue
    
    # If we are the right answer let them know and leave the loop!
    elif (theGuess == answerNum):
        print("You win!\n")
        break

    # If we are too low, tell them to aim higher!
    elif (theGuess < answerNum):
        print("Too low! Aim higher!\n")

    # If we are too high, tell them to aim lower!
    elif (theGuess > answerNum):
        print("Too high! Aim lower!\n")

    # Add a guess
    guesses += 1

