from nltk.corpus import words
from nltk.stem import *

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
    frequencies = []

    for shift, value in encryptions.items():
        parse = value.split() # split sentence into list of words
        word = sum([1 for word in parse if word in words.words()]) # 1 if word is an actual word
        frequencies.append(word) # collect frequencies

    maxfreq = 0
    maxidx = 0
    for index in range(len(frequencies)):
        if frequencies[index] > maxfreq:
            maxfreq = frequencies[index]
            maxidx = index

    return list(encryptions.values())[maxidx] # return decrypted text
