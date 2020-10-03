from nltk.corpus import words
from break_caesar import encrypt, break_caesar

def decrpyt_alpha(sent_word): # main function
    encryptions = encrypt(sent_word)
    return break_caesar(encryptions)