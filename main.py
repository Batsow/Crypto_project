from maths.alphabet import letter_to_number
from maths.alphabet import number_to_letter
from maths.alphabet import clean_text
from ciphers.shift_cipher import encrypt, decrypt


'''
Testing if the alphabet.py code works proper
'''
text1 = "This Message"
text2 = ("Hello, World! I am 200 years old")

print(clean_text(text1))
print(clean_text(text2))

print(letter_to_number("A"))
print(letter_to_number("T"))

print(number_to_letter(0))
print(number_to_letter(19))



'''
shift cipher test
'''

message = "THIS MESSAGE IS TOP SECRET"
key = 3

ciphertext = encrypt(message, key)
print("Ciphertext:", ciphertext)

print(encrypt("XYZ", 3))
print(encrypt("HELLO", -3))

plaintext = decrypt(ciphertext, key)
print("Plaintext:", plaintext)

print(decrypt("ABC", 3))
print(decrypt("HELLO", -3))


