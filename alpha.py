from nltk.corpus import words
from break_caesar import encrypt, break_caesar

def decrpyt_alpha(sent_word): # main function
    encryptions = encrypt(sent_word)
    decryptedText, shift = break_caesar(encryptions)
    if sent_word == decryptedText:
        message = "Caesar Cipher failed or word has not been encrypted"
        shift = "Encryption may be polyalphabetic or use a generic monoalphabetic scheme"
    else:
        message = "Decrypted Text: " + decryptedText
        shift = "Shift: " + str(shift)
    return [message, shift] # Please include shift