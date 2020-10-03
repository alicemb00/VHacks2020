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

        dictionary[toShift] = total;

    return dictionary

def break_caesar(encryptions):
    for shift, value in encryptions.items():
        if (value.split()[0] in words.words()):
            return {shift: value}

    return "Unable to break encryption"

encryptions = encrypt("ifmmp ifmmp")
print(break_caesar(encryptions))