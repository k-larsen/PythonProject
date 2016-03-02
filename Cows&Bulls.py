import random

# game instructions
print "Welcome to Mastermind\n" \
      "You're objective is to guess a 4 digit number\n" \
      "For every number that is accurate to the hidden number a COW will be awarded,\n" \
      "For every number that is in the sequence but not in the right place will be awarded with a BULL\n"\
      "Guess until you get the number correct\nGood Luck"

number = ""
# concatenate four integers to make number
for i in range(4):
    number += str(random.randint(0,9))
print number

def checkNumLength(guessNum):
    print "You entered a number with the incorrect length"
    guessNum = raw_input("Enter a number: ")
    return guessNum

# bulk of game --> actual guessing process
def guessGame(number):
    guess = raw_input("Enter a 4 digit number: ")
    if len(guess) > 4 or len(guess) < 4:
        guess = checkNumLength(guess)
    editNumber = number
    guessCount = 1
    while str(number) != guess: # guess number doesn't equal random number
        cow = 0
        bull = 0
        for i in range(4):
            if guess[i] == str(editNumber)[i]:  #current match up is a cow
                cow+=1
                editNumber = str(editNumber)[:i]+"C"+str(editNumber)[i+1:] #replace number in string with C
            else: # check for possible bull with current number in guess number
                for j in range(0,4):
                    if guess[i] == str(editNumber)[j]: # current match is a bull
                        bull+=1
                        editNumber = str(editNumber)[:j]+"B"+str(editNumber)[j+1:] #replace number in string with B
                        break


        # put cows/bulls into strings to compare indices
        print "COW: "+str(cow)+"\n"\
                "BULL: "+str(bull)


        guessCount+=1 # total of guesses increases
        guess = raw_input("Enter a 4 digit number")
        if len(guess) > 4 or len(guess) < 4:
            guess = checkNumLength(guess)
        editNumber = number
    print "YOU WIN!\nYou guessed correctly.\nTries Taken: "+str(guessCount) # once the number is guessed

# play the game
guessGame(number)
