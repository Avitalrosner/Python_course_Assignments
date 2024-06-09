
import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")

        self.computer_num = random.randint(1, 21)
        self.num_of_guess = 0

        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Please enter a number between 1 and 21:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=5)

        self.cheat_button = tk.Button(self.root, text="Show Hidden Number", command=self.show_hidden_number)
        self.cheat_button.pack(pady=5)

        self.new_game_button = tk.Button(self.root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

        self.message_label = tk.Label(self.root, text="")
        self.message_label.pack(pady=10)
    
    def check_guess(self):
        user_input = self.entry.get()
        if user_input.lower() == 'x':
            self.root.quit()
        elif user_input.lower() == 'n':
            self.new_game()
        elif user_input.lower() == 's':
            self.show_hidden_number()
        else:
            try:
                user_guess = int(user_input)
                self.num_of_guess += 1

                if user_guess > self.computer_num:
                    self.message_label.config(text="Too big")
                elif user_guess < self.computer_num:
                    self.message_label.config(text="Too small")
                else:
                    self.message_label.config(text=f"You win! The number was {self.computer_num} in {self.num_of_guess} guesses.")
                    if messagebox.askyesno("Play Again?", "Do you want to play another game?"):
                        self.new_game()
                    else:
                        self.root.quit()
            except ValueError:
                self.message_label.config(text="Invalid input! Please enter a number.")
    
    def show_hidden_number(self):
        messagebox.showinfo("Hidden Number", f"The hidden number is {self.computer_num}")

    def new_game(self):
        self.computer_num = random.randint(1, 21)
        self.num_of_guess = 0
        self.entry.delete(0, tk.END)
        self.message_label.config(text="")
        self.label.config(text="Please enter a number between 1 and 21:")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
