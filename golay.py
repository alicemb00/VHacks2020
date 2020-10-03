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

def add_words(w1, w2):
    new_word = []
    for idx, val in enumerate(w1):
        new_word += [(val + w2[idx]) % 2]
    return new_word

def find_min_distance(s, B):    # add s to every row of B and find minimum distance
    d = len(s)
    row = ""
    for (idx, word) in enumerate(B):
        wt = 0
        for (i, num) in enumerate(word):
            wt += (s[i] + num) % 2 
        if wt < d:
            d = wt
            row = word
            num = idx
            
    return {"distance": d, "row": row}
            

def find_syndrome(v, M):    # Find syndrome with word v and parity check matrix M
    s = []
    for i in range(len(M[0])):
        wt = 0
        for j in range(len(v)):
            wt += v[j] * M[j][i]
        s = s + [(wt % 2)]
    return s
        
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

    B = ["110111000101", "101110001011", "011100010111", "111000101101", "110001011011", "100010110111", "000101101111", "001011011101", "010110111001", "101101110001", "011011100011", "111111111110"]
    H = build_I(12) + B
    B_split = [split_num(i) for i in B]     # Matrix B in problem
    H_split = [split_num(i) for i in H]     # Parity check matrix used for problem
    w = split_num(sent_word)

    s1 = find_syndrome(w, H_split)
    s2 = find_syndrome(s1, B_split)

    if find_weight(s1) <= 3:
        error = join_num([s1] + [0 for _ in range(12)])
        codeword = add_words(s1, error)
        message = codeword[0:12]

    return sent_word