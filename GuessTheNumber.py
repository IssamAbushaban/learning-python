import os
import random

lowerBound = random.randint(0,50)
upperBound = lowerBound + 10
answerNum  = random.randint(lowerBound,upperBound)

#Clear Console
os.system('clear')

print("Guess the number: A fun little game!\n")
print("It's between " + str(lowerBound) + " and " + str(upperBound) + "! What do you think it is?\n")
theGuess = input("Your guess: ")

if (theGuess == str(answerNum)):
    print("You win!")
else:
    print("You lose!")
