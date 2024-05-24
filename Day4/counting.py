#version that reads the file 3 times, less efficient.
import sys

# I'm defining 3 function for counting the charactors, lines and words:

def count_characters(filename):
    with open(filename, 'r') as file:
        text = file.read()       
        return sum(1 for charactor in text if charactor != ' ')

def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)
  
# Defining a main function that checks for errors and uses the above 3 functions:
def main():
    if len(sys.argv) != 2:
        print("Usage: python counting.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    
    try:
        num_characters = count_characters(filename)
        num_lines = count_lines(filename)
        num_words = count_words(filename)
        
        print("Number of characters:", num_characters)
        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
    
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
