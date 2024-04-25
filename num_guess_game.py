import random

# The computer "thinks" a about a whole number betwee 1 and 20:
computer_num = random.randrange(1,21)
num_of_guess = 0

#loop for the game:
while True:
    # The user guesses a number:
    user_guess = input("Please enter a number: ")
    # The computer tells if the guess was too small, too big or exact.
    # If exact the user wins, the program ends. Otherwise the user guesses again.

    if int(user_guess) > int(computer_num):
        print("Too big")
        num_of_guess += 1
    elif int(user_guess) < int(computer_num):
        print("Too small")
        num_of_guess += 1
    else:
        print("You win")
        num_of_guess += 1
        # print how many guesses the user needed.
        print(f"The number of guesses are {num_of_guess}")
        break
        
                













