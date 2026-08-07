from maths.alphabet import letter_to_number
from maths.alphabet import number_to_letter
from maths.alphabet import clean_text

text = "This Message"

print(clean_text(text))
print(letter_to_number("A"))
print(letter_to_number("T"))

print(number_to_letter(0))
print(number_to_letter(19))
