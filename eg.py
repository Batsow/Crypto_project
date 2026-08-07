text = "Hi , I . Miss you"
letters = []
for char in text:
    if char.isalpha():
        letters.append(char.upper())

print(letters)
result = "".join(letters)
print(result)