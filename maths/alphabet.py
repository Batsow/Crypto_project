'''
provides reusable alphabet mappings for classical ciphers

A -> 0
B -> 1
...
Z -> 25
'''

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

LETTER_TO_NUMBER = {}
for index, letter in enumerate(ALPHABET):
    LETTER_TO_NUMBER[letter] = index
    
  
NUMBER_TO_LETTER = {}
for index, letter in enumerate(ALPHABET):
    NUMBER_TO_LETTER[index] = letter
    
        
# print(NUMBER_TO_LETTER)
# print(LETTER_TO_NUMBER)


def letter_to_number(letter):
    return LETTER_TO_NUMBER[letter]

def number_to_letter(number):
    return NUMBER_TO_LETTER[number]


def clean_text(text):
    letters = []
    for char in text.upper():
        if char in ALPHABET:
            letters.append(char)
            
    result = "".join(letters)
    return result

