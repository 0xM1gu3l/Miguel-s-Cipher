from scripts.encode import encode
from string import ascii_letters

i_key = 0
i_letter = 0
encoded = []
enc_text = open("2decode.txt", "r").read()
key = encode(input("Enter the secret key for decoding: "))

# Observation: This code sucks :D


for letter in enc_text:
    if letter not in ascii_letters:
        encoded.append(letter)
        continue
    if i_key > len(key) - 1:
        i_key = 0
    curr_letter = ascii_letters.find(letter)
    if ((i_letter + 1) % 2 == 0): #Par subtrai
        curr_letter = (ascii_letters.find(key[i_key]) - 1) - curr_letter
        if curr_letter > 51: curr_letter -= 52
    else:
        curr_letter = curr_letter - (ascii_letters.find(key[i_key]) + 1)
        if curr_letter < 0: curr_letter += 52
    encoded.append(ascii_letters[curr_letter])
    i_letter += 1
    i_key += 1
print("".join(encoded))