# Error correct Hamming Code
import math

def find_weight(word):
    idx = 0
    for i in word:
        idx += int(i)
    return idx

def split_num(num_str):     # make life easier when entering words
    return [int(i) for i in num_str]

def join_num(split_num):
    num_str = ""
    for i in split_num:
        num_str += str(i)
    return num_str

def build_I(n): # Build Identity matrix
    I = []
    for i in range(n):
        num_str = ""
        for j in range(n):
            if(j==i):
                num_str += "1"
            else:
                num_str += "0"
        I = I + [num_str]
    
    return I

def validate_word(word):
    n = len(word)
    if not(word):
        return "Please enter a binary string"
    for i in word:
        if i != '1' and i != '0':
            return "Please enter a binary string"
    
    if math.log2(n + 1) != int(math.log2(n + 1)):
        return "Please enter a word of the proper length"

    return int(math.log2(n + 1))

def build_H(r):
    H = [[0 for _ in range(r)] for _ in range(2**r - 1)]
    for i in range(2**r - 1):
        row = bin(i + 1)
        length = len(str(row)[2:])
        row = "0" * (r - length) + str(row)[2:]
        for j in range(r):
            H[i][j] = int(row[j])
        print(row)
    return H

def adjust_H(H):
    adjusted = [[0 for _ in range(len(H[0]))] for _ in range(len(H))]
    idx = 0
    top = []
    bottom = []
    for (num, row) in enumerate(H):
        identity = True
        for (i, col) in enumerate(row):
            if i == idx and col == 0:
                identity = False
            elif i != idx and col == 1:
                identity = False
        if(identity):
            top = top + [idx]
            idx += 1
        else:
            top = top + [num]

        


def find_syndrome(v, M):    # Find syndrome with word v and parity check matrix M
    s = []
    for i in range(len(M[0])):
        wt = 0
        for j in range(len(v)):
            wt += v[j] * M[j][i]
        s = s + [(wt % 2)]
    return s

def correct_hamming(word):
    r = validate_word(word)
    if type(r) != int:
        return [r, "", ""]

    H = build_H(r)
    s = find_syndrome(split_num(word), H)

    for (idx, row) in enumerate(H):
        if s == row:
            row_num = idx
            break

    error = [0 for _ in range(len(word))]
    error[idx] = 1
    sent = split_num(word)
    if sent[idx] == 0:
        sent[idx] = 1
    else:
        sent[idx] = 0

    codeword = join_num(sent)
    message = "Decoded: Not supported at this time"
    return ["Error pattern of " + join_num(error) + " found", "Correct received word to " + codeword, message]