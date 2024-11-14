"""
Miguel's Cipher
Author: Miguel Caparróz
Description: A Cipher that's very simple

...and no, this code has no comments. [Try looking the decoding program]
"""

from string import ascii_letters

def encode(txt2encode):
    encoded = []
    i = 1
    for letter in txt2encode:
        if (letter == " "):
            encoded.append(" ")
            continue
        elif letter not in ascii_letters:
            encoded.append(letter)
            continue
        curr_letter = ascii_letters.find(letter)
        curr_letter += i
        while (curr_letter > 51):
            curr_letter -= 52
        encoded.append(ascii_letters[curr_letter])
        i += 1
    return "".join(encoded)