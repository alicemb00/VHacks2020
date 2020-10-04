from nltk.corpus import words
from break_caesar import decrypt, break_caesar

def decrpyt_alpha(sent_word): # main function
    decryptions = decrypt(sent_word) # Call decrypt to return list of of ceaser shifts
    decryptedText, shift, goodDecryption = break_caesar(decryptions) # Check which shift is correct 
    if goodDecryption == False: #
        message = "Caesar Cipher failed"
        shift = "Encryption may be polyalphabetic or use a generic monoalphabetic scheme"
    else:
        message = "Decrypted Text: " + decryptedText
        shift = "Shift: " + str(shift)
    return [message, shift]