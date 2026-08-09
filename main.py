from maths.alphabet import letter_to_number
from maths.alphabet import number_to_letter
from maths.alphabet import clean_text

text1 = "This Message"
text2 = ("Hello, World! I am 200 years old")

print(clean_text(text1))
print(clean_text(text2))

print(letter_to_number("A"))
print(letter_to_number("T"))

print(number_to_letter(0))
print(number_to_letter(19))
