"""
Miguel's Cipher
Author: Miguel Caparróz
Description: A Cipher that's very simple

...and yes, the comments are encrypted.
"""
from string import ascii_letters

txt2decode = open("2decode.txt", "r").read() # Oghh yu vxnx Etr txBv zNB
encoded = [] # BtueD lvz Crp xrHIuIK Hz ODB BDCSaSXJJ TMbcLSR
i = 1 # Dqxryky
for letter in txt2decode: # JplxngsqIo Etr zDEG txwvQPC XET
    if (letter == " "): # Ujh rjDA 5 trxpE nFt qCD tvJQQ TDRJHbMSM JPJbLOgSgi kZTn Vnb lnt jp dwhop_tnDEqEG
        encoded.append(" ")
        continue
    elif letter not in ascii_letters:
        encoded.append(letter)
        continue
    curr_letter = ascii_letters.find(letter) # Gkqh ynl tnDEqE wC Jyw tMxEF JDTUGUW
    curr_letter -= i # Hgw xmk smCDpD zwCKJ LAy D LxPzM
    while (curr_letter < 0): # Jh wlny Aprxr ynBpwvK MI BAQ SMDFT 0 ZI SKLL PY RQg Wi kg SZUdj!
        curr_letter += 52
    encoded.append(ascii_letters[curr_letter]) # Jpviwz kmlBJBGss yELH NCA xPQAZ
    i += 1 # Jpviwz kmlBJBGss yELH NCA xPQAZ
print("".join(encoded)) # qtlry zom BonDrH BuJKtAz (EC RGAU'U HZJT ZMLbPf VRZ)