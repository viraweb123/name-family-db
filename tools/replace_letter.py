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

def replace_letter(name):
    index = random.randint(0, len(name) - 1)
    random_letter = random.choices(alphabet, k=1)[0]
    if name[index] is not random_letter:
        name.replace(name[index], random_letter)
        return name
    return False

# generates wrong names
with open("replace_letter_name.txt", 'wt') as file:
    for name in list(names):
        if count_part(name) == 1:
            new_word = replace_letter(name)
            if new_word:
                file.write(new_word + "\n")

        elif count_part(name) == 2:
            new_word = replace_letter(name[0]) + replace_letter(name[1])
            if new_word:
                file.write(new_word + "\n")

        elif count_part(name) == 3:
            new_word = replace_letter(name[0]) + replace_letter(name[1])\
                + replace_letter(name[2])
            if new_word:
                file.write(new_word + "\n")

file.close()

# generates wrong surnames
with open("replace_letter_surname.txt", 'wt') as file:
    for surname in list(surnames):
        if count_part(surname) == 1:
            new_word = replace_letter(surname)
            if new_word:
                file.write(new_word + "\n")

        elif count_part(surname) == 2:
            new_word = replace_letter(surname[0]) + replace_letter(surname[1])
            if new_word:
                file.write(new_word + "\n")

        elif count_part(surname) == 3:
            new_word = replace_letter(surname[0]) + replace_letter(surname[1])\
                + replace_letter(surname[2])
            if new_word:
                file.write(new_word + "\n")

file.close()