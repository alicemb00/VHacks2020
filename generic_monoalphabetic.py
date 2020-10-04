# to break this algorithm, the statistics of the English language are important to consider
# 1. The most common letter in the English language is 'E' (found in 11% of all English words)
# 2. Two letter words and three letter words are fairly easy to pick out
# 3. Vowels are incredibly important!

def parse_phrase(encrypted_phrase):
    words = encrypted_phrase.split()
    return words

def pick_out_articles(words):
    articles = ["a", "an", "the"]
    short_words = [word for word in words if len(word) <= 3]
    return short_words 
    
def letter_freq(words):
    letters = [] # holds letters of phrase / not punctuation
    for word in words:
        for letter in word:
            if (letter.isalpha()):
                letters.append(letter)

    letter_freq = {}
    for tracker_letter in letters:
        letter_count = 0
        for individual_letter in letters:
            if (tracker_letter == individual_letter):
                letter_count += 1
        
        letter_freq[tracker_letter] = letter_count
    
    return letter_freq

def map_encrypt_decrypt_letters(letter_freq, short_words):
    # assume any given three-letter word maps to the for our first guess
    three_letters = [word for word in short_words if len(word) == 3]
    char_difference = 0
    dictionary_map = {}

    for word in three_letters:
        if (word[0] > 't'):
            char_difference = ord(word[0]) - ord('t')
        else:
            char_difference = ord('t') - ord(word[0])
        
        dictionary_map[word[0]] = 't'
    
    return dictionary_map