# "Guess the number" mini-project by Sheena

# http://www.codeskulptor.org/#user43_4VgVQmR8uu_2.py

# input will come from buttons and an input field
# all output for the game will be printed in the console

# import modules
import random
import simplegui
import math

# initialize global variable num_range
num_range = 100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_range, secret_number, chances_left
    secret_number = random.randrange(0, num_range)
    chances_left = int(math.ceil(math.log(num_range + 1, 2)))
    
    print ""
    print "New game starts!"
    print "The secret number is between 0 and", num_range
    print "You have", chances_left, "chances. Good luck!"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    guess_number = int(guess)
    print ""
    print "Guess was", guess_number
    
    # Compare the guess number to the secret number
    global secret_number, chances_left
    
    if chances_left > 1:
        if secret_number > guess_number:
            print "Higher"
            chances_left -= 1
            print "Number of remaining guesses is", chances_left
            
        elif secret_number < guess_number:
            print "Lower"
            chances_left -= 1 
            print "Number of remaining guesses is", chances_left
            
        else:
            print "Correct! You win!"
            new_game()
    else:
        if secret_number == guess_number:
            print "Correct! You win!"
            new_game()
        else:
            print "Out of chances! You lose!"
            new_game()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100)", range100)
f.add_button("Range is [0, 1000)", range1000)
f.add_input("Enter your guess:", input_guess, 50)
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
