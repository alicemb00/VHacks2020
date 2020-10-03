def split_num(num_str):     # make life easier when entering words
    return [int(i) for i in num_str]

def join_num(split_num):
    num_str = ""
    for i in split_num:
        num_str += str(i)
    return num_str

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


def decode_rm(sent_word):
    return "Decoded RM message"

print(get_rm_code(0, 4))