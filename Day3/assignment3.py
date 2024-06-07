#third assignment:

import random

def generate_random_number():
    return random.randint(1, 21)

def get_user_guess():
    user_input = input("Please enter a number, or 'x' to exit, 'n' for new game, 's' for cheating: ")
    return user_input.lower().strip()

def ask_play_again():
    while True:
        play_again_input = input("Do you want to play another game? (yes/no): ").lower()
        if play_again_input in ['yes', 'no']:
            return play_again_input == 'yes'
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

def play_game():
    while True:
        computer_num = generate_random_number()
        num_of_guess = 0

        while True:
            user_guess = get_user_guess()
            
            if user_guess == 'x':
                return False
            elif user_guess == 'n':
                break
            elif user_guess == 's':
                print(f"The hidden number is {computer_num}")
            else:
                try:
                    user_guess = int(user_guess)
                    num_of_guess += 1

                    if user_guess > computer_num:
                        print("Too big")
                    elif user_guess < computer_num:
                        print("Too small")
                    else:
                        print("You win!")
                        print(f"The number of guesses is {num_of_guess}")
                        return ask_play_again() 
                except ValueError:
                    print("Invalid input! Please enter a number.")
        
        if not ask_play_again():
            return False

def main():
    while True:
        play_again = play_game()
        if not play_again:
            break

if __name__ == "__main__":
    main()


