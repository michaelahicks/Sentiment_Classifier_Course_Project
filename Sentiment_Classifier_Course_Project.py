punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

""" function to strip puntuations from words passed to the function """
def strip_punctuation(word):
    print(word)
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
            print(word)
    return word


"""function that takes words in a string and compares them to a postive words
list and increments a counter for each one """

def get_pos(string):
    print(string)
    pos = 0
    words = string.lower().split()
    for word in words:
        s_word = strip_punctuation(word)
        if s_word in positive_words:
            pos = pos + 1
    return pos

"""function that takes words in a string and compares them to a negative words
list and increments a counter for each one """
def get_neg(string):
    print(string)
    neg = 0
    words = string.lower().split()
    for word in words:
        s_word = strip_punctuation(word)
        if s_word in negative_words:
            neg = neg + 1
    return neg
