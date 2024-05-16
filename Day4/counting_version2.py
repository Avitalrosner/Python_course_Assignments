#version that reads the file once - more efficiant.
import sys

# Defining the functions - counting characters, lines, and words:
def count_characters(text):
    return sum(1 for character in text if character != ' ')

def count_lines(text):
    return text.count('\n') + 1

def count_words(text):
    return len(text.split())

# Defining the main function:
def main():
    if len(sys.argv) != 2:
        print("Usage: python counting.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            text = file.read()

        num_characters = count_characters(text)
        num_lines = count_lines(text)
        num_words = count_words(text)
        
        print("Number of characters:", num_characters)
        print("Number of lines:", num_lines)
        print("Number of words:", num_words)
    
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
