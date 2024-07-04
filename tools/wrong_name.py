import pandas as pd 
import random
import csv
import word_shuffler

alphabet = ['ا', 'ب', 'پ', 'ت', 'ث','ج', 'چ', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'ژ', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ک', 'گ', 'ل', 'م', 'ن', 'ه', 'ی']
surnames = pd.read_csv("~/personal/correct_dataset/surname_2.csv")["Names"]
names = pd.read_csv("~/personal/correct_dataset/names.csv")["Names"]


def generate_word(name_size: int):
    random_name = random.choices(alphabet, k=name_size)
    return ''.join(random_name)


def count_part(name):
    splited_name = name.split()
    return len(splited_name)

# generates wrong names
with open("name_wrong.txt", 'wt') as file:
    for name in list(names):
        if count_part(name) == 1:
            new_word = generate_word(len(name))
            file.write(new_word + "\n")

        elif count_part(name) == 2:
            new_word = generate_word(len(name[0])) + generate_word(len(name[1]))
            file.write(new_word + "\n")

        elif count_part(name) == 3:
            new_word = generate_word(len(name[0])) + generate_word(len(name[1]))\
                + generate_word(len(name[2])) 
            file.write(new_word + "\n")

file.close()

# generates wrong surnames
with open("surname_wrong.txt", 'wt') as file:
    for surname in list(surnames):
        if count_part(surname) == 1:
            new_word = generate_word(len(surname))
            file.write(new_word + "\n")

        elif count_part(surname) == 2:
            new_word = generate_word(len(surname[0])) + generate_word(len(surname[1]))
            file.write(new_word + "\n")

        elif count_part(surname) == 3:
            new_word = generate_word(len(surname[0])) + generate_word(len(surname[1]))\
                + generate_word(len(surname[2])) 
            file.write(new_word + "\n")

file.close()