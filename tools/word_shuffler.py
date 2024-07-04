import pandas as pd
from random import shuffle
def shuffle_word (word):
    word=list(word)
    shuffle(word) 
    return ''.join(word)


surname_data = pd.read_csv("~/personal/correct_dataset/surname_2.csv")["Names"]
name_data = pd.read_csv("~/personal/correct_dataset/names.csv")["Names"]
surname_data.drop_duplicates()
name_data.drop_duplicates()

with open("word_shuffled.txt", 'wt') as f:
    for i in surname_data:
        for j in name_data:
            print(shuffle_word(i) + " " + shuffle_word(j))
            f.write(shuffle_word(i) + " " + shuffle_word(j) + "\n")
f.close()
    