punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# function to strip puntuations from words passed to the function
def strip_punctuation(word):
    print(word)
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
            print(word)
    return word
