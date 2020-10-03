from nltk.corpus import words

def encrypt(toDecode):
    toDecode = toDecode.lower()
    dictionary = {}

    for toShift in range(26):
        total = ""
        for letter in toDecode:
            if 96 < ord(letter) < 123:
                letter = ord(letter) + toShift
                if letter > 122:
                    letter = letter - 26
                total += chr(letter)
            else:
                total += " "

        dictionary[toShift] = total

    return dictionary

def break_caesar(encryptions):
    for shift, value in encryptions.items():
        if (value in words.words()):
            return {shift: value}


def decrpyt_alpha(sent_word): # main function
    encryptions = encrypt("ifmmp")
    return break_caesar(encryptions)