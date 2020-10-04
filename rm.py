def validate_word(sent_word, r, m):
    if not(sent_word and r and m):
        return "Please fill out all fields"
    if not(r.isdigit) or len(r) != 1:
        return "Please enter a positive integer less than 10 for r"
    if not(m.isdigit) or len(m) != 1:
        return "Please enter a positive integer less than 10 for m"

    m = int(m)
    r = int(r)

    for i in sent_word:
        if i != '1' and i != '0':
            return "Please enter a binary string"

    if len(sent_word) != 2**m:
        return "Please enter a binary string of length " + str(2**m)

    if r > m:
        return "Please enter a larger m value than r value"
    
    if r < 0:
        return "Please enter positive values"

    return "valid"

def split_num(num_str):     # make life easier when entering words
    return [int(i) for i in num_str]

def join_num(split_num):
    num_str = ""
    for i in split_num:
        num_str += str(i)
    return num_str

def find_weight(word):
    idx = 0
    for i in word:
        idx += int(i)
    return idx

def add_words(w1, w2):
    new_word = []
    for (idx, val) in enumerate(w1):
        new_word += [(int(val) + int(w2[idx])) % 2]
    return new_word

def zero_case(m):
    return {join_num([0 for _ in range(2**m)]), join_num([1 for _ in range(2**m)])}

def force_length(bin_str, m):
    if(len(str(bin_str)[2:]) < m):
        return join_num([0 for _ in range(m - len(str(bin_str)[2:]))]) + str(bin_str)[2:]
    return str(bin_str)[2:]

def equal_case(m):
    code = set()
    for i in range(2**(2**m)):
        code.add(force_length(bin(i), 2**m))
    return code

def get_rm_code(r, m):
    if r == m:
        return equal_case(m)
    elif r == 0:
        return zero_case(m)
    else:
        code = set()
        set_1 = get_rm_code(r, m-1)
        set_2 = get_rm_code(r-1, m-1)
        for i in set_1:
            for j in set_2:
                code.add(i + join_num(add_words(split_num(i), split_num(j))))
        return code


def decode_rm(sent_word, r, m):
    if (validate_word(sent_word, r, m) != "valid"):
        return ["", validate_word(sent_word, r, m)]

    m = int(m)
    r = int(r)
    n = 2**m
    d = 2**(m-r)
    code = get_rm_code(r, m)
    min_correctable = (d - 1) // 2
    error = ""
    codeword = ""
    for i in code:
        if find_weight(add_words(sent_word, i)) <= min_correctable:
            error = join_num(add_words(sent_word, i))
            codeword = i
            break

    if error == "":
        if min_correctable == 0:
            output_message = ["Note: the distance of this code is " + str(d) + ", so no error pattern of any weight can be corrected", "Ask for retransmission"]
        else: 
            output_message = ["", "Ask for retransmission"]
    else: 
        output_message = ["Found the following error pattern: " + error, " Correct to: " + codeword]

    return output_message