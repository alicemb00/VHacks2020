def decrypt(toDecode):
    toDecode = toDecode.lower()

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
        print(toShift, total)

def decrpyt_alpha(sent_word): # main function
    return decrypt(sent_word)