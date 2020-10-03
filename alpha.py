
def decrypt(toDecode):
    toDecode = toDecode.lower()

    for toShift in range(26):
        total = ""
        # Iterate over toDecode
        for letter in toDecode:
            # If the original input is a letter
            if 96 < ord(letter) < 123:
                letter = ord(letter) + toShift
                # Check for wrap around
                if letter > 122:
                    letter = letter - 26
                total += chr(letter)
            # If the original input is not a letter, than assume whitespace
            else:
                total += " "
        print(toShift, total)

def decrpyt_alpha(sent_word): # main function
    return decrypt(sent_word)