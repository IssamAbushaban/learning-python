if __name__ == '__main__':
    lowerBound = 1
    upperBound = 10
    answerNum  = 5

    print("Guess the number: A fun little game!")
    print("It's between " + lowerBound + " and " + upperBound + "! What do you think it is? ")
    theGuess = input("Your guess: ")

    if (theGuess == answerNum):
        print("You win!")
    else:
        print("You lose!")
