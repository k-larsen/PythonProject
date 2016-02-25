import random

print "Welcome to Mastermind\n" \
      "You're objective is to guess a 4 digit number\n" \
      "For every number that is accurate to the hidden number a COW will be awarded,\n" \
      "For every number that is in the sequence but not in the right place will be awarded with a BULL\n"\
      "Guess until you get the number correct\nGood Luck"

number = random.randint(1000, 9999) # generate random number with 4 digits


# bulk of game --> actual guessing process
def guessGame(number):
    guess = raw_input("Enter a 4 digit number: ")
    cow = 0
    bull = 0
    guessCount = 0
    while str(number) != guess:
        for i in range(4):
            if guess[i] == str(number)[i]:
                cow+=1
            else:
                for j in range(1,3):
                    if guess[i] == str(number)[j]:
                        bull+=1
                        

        # put number into strings to compare indices
        print "COW: "+str(cow)
        print "BULL: "+str(bull)


        guessCount+=1
        guess = raw_input("Enter a 4 digit number")
    print "You took "+str(guessCount)+" tries."


guessGame(number)