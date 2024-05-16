#defining the 3 function that can be imported:

def count_characters(text):
    return sum(1 for character in text if character != ' ')

def count_lines(text):
    return text.count('\n') + 1

def count_words(text):
    return len(text.split())
