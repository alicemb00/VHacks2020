def find_weight(word):
    idx = 0
    for i in word:
        idx += int(i)
    return idx

def check_input(sent_word):
    for i in sent_word:
        if i != '1' and i != '0':
            return "Please enter a binary string"
    if len(sent_word) == 23:
        return "SG"
    elif len(sent_word) == 24:
        return "EG"
    else: 
        return "Please enter a word of length 23 or 24"

def decode_golay(sent_word):
    if check_input(sent_word) != "SG" and check_input(sent_word) != "EG":
        return check_input(sent_word)

    if check_input(sent_word) == "SG":
        sent_word += str((find_weight(sent_word) + 1) % 2)
    return sent_word