punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

""" function that strips puntuations from words passed to the function """

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

pos_words = open("positive_words.txt", "r")
positive_words = pos_words.read()
positive_words = strip_punctuation(positive_words)
positive_words = positive_words.split()


"""function that takes words in a string and compares them to a postive words
list and increments a counter for each one """

def get_pos(string):
    pos = 0
    words = string.lower().split()
    for word in words:
        s_word = strip_punctuation(word)
        if s_word in positive_words:
            pos = pos + 1
    return pos

neg_words = open("negative_words.txt", "r")
negative_words = neg_words.read()
negative_words = strip_punctuation(negative_words)
negative_words = negative_words.split()

"""function that takes words in a string and compares them to a negative words
list and increments a counter for each one """
def get_neg(string):
    neg = 0
    words = string.lower().split()
    for word in words:
        s_word = strip_punctuation(word)
        if s_word in negative_words:
            neg = neg + 1
    return neg

twitter_file = open("project_twitter_data_two.txt", "r")  #open data file
lines = twitter_file.readlines()  #assign the readlines to a variable

for lin in lines:
    print(lin)

header = lines[0]
print(header)
field_names = header.strip().split(",")
print(field_names)
#print(lines[2])
 
outfile = open("resulting_data_two.csv", "w")
outfile.write('Number of Retweets, Number of Replies, Positve Score, Negative Score, Net Score')
outfile.write('\n')

for line in lines[2:]:
    pos_sent = get_pos(line) #send line to pos function for analysis
    print("******Pos")
    print(pos_sent)
    neg_sent = get_neg(line) #send line to neg function for analysis
    print("******Neg")
    print(neg_sent)
    net_score = pos_sent - neg_sent  #calculate net sentiment score
    print("******Net")
    print(net_score)
    print("******")
    line = line.strip().split(",")   #clean and split line
    row_string = '{},{},{},{},{}'.format(line[1], line[2], pos_sent, neg_sent, net_score)
    outfile.write(row_string)
    outfile.write('\n')
    
pos_words.close()
neg_words.close()
twitter_file.close()
outfile.close()



