#testing that the functions work:

from functions_for_counting import count_characters, count_lines, count_words

def test_count_characters():
    assert count_characters("My name is Avital") == 14
    assert count_characters("I am learning python") == 17

def test_count_lines():
    assert count_lines("My\nname\nis\nAvital") == 4
    assert count_lines("Heya!") == 1

def test_count_words():
    assert count_words("My name is Avital") == 4
    assert count_words("") == 0
