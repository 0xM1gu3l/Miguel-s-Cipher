from scripts.encode import encode
from string import ascii_letters

i_key = 0
i_letter = 0
encoded = []
enc_text = open("2encode.txt", "r").read()
key = encode(input("Enter the secret key for encoding (You will need this to decode the message): "))

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
        if curr_letter < 0: curr_letter += 52
    else:
        curr_letter = (ascii_letters.find(key[i_key]) + 1) + curr_letter
        if curr_letter > 51: curr_letter -= 52
    encoded.append(ascii_letters[curr_letter])
    i_letter += 1
    i_key += 1
print("".join(encoded))


"""
Hello -> LoNhN (key: crypto -> dtBtyu)

L  o  N  h N
38 15 40 8 40

d t  B t  y  u
4 20 28 20 25 21

38 - 4 = 34 = H
20 - 15 = 5 = e
40 - 28 = 12 = l
20 - 8 = 12 = l
40 + 25 = 65 - 52 = 13 = o

abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
"""
