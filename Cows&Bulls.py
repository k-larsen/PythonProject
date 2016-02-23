import random

print "Welcome to Mastermind\n" \
      "You're objective is to guess a 4 digit number\n" \
      "For every number that is accurate to the hidden number a COW will be awarded,\n" \
      "For every number that is in the sequence but not in the right place will be awarded with a BULL\n"\
      "Guess until you get the number correct\nGood Luck"

number = random.randint(1000, 9999) # generate random number with 4 digits

def guessGame(number):
    return number




