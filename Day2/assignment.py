# Second assignment
import random

# The computer "thinks" a about a whole number betwee 1 and 20:
computer_num = random.randrange(1,21)
num_of_guess = 0

#loop for the game:
while True:
    # The user guesses a number:
    user_guess = input("Please enter a number: ")
    num_of_guess += 1
    # The computer tells if the guess was too small, too big or exact.
    # If exact the user wins, the program ends. Otherwise the user guesses again.
    
    if int(user_guess) > computer_num:
        print("Too big")
    elif int(user_guess) < computer_num:
        print("Too small")
    else:
        print("You win")
        # print how many guesses the user needed.
        print(f"The number of guesses are {num_of_guess}")
        break

        
                
