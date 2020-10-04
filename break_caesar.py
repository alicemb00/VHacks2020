from nltk.corpus import words
from math import floor

# Create a dictionary with every possible ceaser shift
def decrypt(toDecode):
    toDecode = toDecode.lower()
    dictionary = {}

    # Brute force for every possible ceaser shift
    for toShift in range(26):
        returnStr = ""
        # Iterate over the input string
        for letter in toDecode:
            # If input is a letter, then shift
            if 96 < ord(letter) < 123:
                letter = ord(letter) - toShift
                if letter < 97:
                    letter = letter + 26
                returnStr += chr(letter)
            # if input is not a letter, then ignore
            else:
                returnStr += letter

        dictionary[toShift] = returnStr

    return dictionary

def break_caesar(encryptions):
    frequencies = []
    for shift, value in encryptions.items():
        parse = value.split() # split sentence into list of words
        lengthText = len(parse)
        # Uncomment for sequential search
        # word = sum([1 for word in parse if word in words.words()]) # 1 if word is an actual word

        # Use binary search to see if decrypted word is in dictionary
        wordlist = words.words()
        counter = 0
        for word in parse:
            begin = 0
            end = len(wordlist) - 1
            while (begin <= end):
                mid = floor((begin+end)/2)
                if wordlist[mid] < word:
                    begin = mid + 1
                elif wordlist[mid] > word:
                    end = mid - 1
                else:
                    counter += 1
                    break
        frequencies.append(counter) # collect frequencies

    maxfreq = 0
    maxidx = 0
    # Find how many dictionary words the each version has
    for index in range(len(frequencies)):
        if frequencies[index] > maxfreq:
            maxfreq = frequencies[index]
            maxidx = index
    
    goodDecryption = True
    minScore = (lengthText / 3)
    print(maxfreq)
    print(minScore)
    if (maxfreq < minScore): # If the encrypted text is NOT ceaser shift, return input
        goodDecryption = False
    return list(encryptions.values())[maxidx], maxidx, goodDecryption # return decrypted text / best decryption
