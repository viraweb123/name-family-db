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

def less_letter(name):
    index = random.randint(0, len(name) - 1)
    name.replace(name[index], '')
    return name

def more_letter(name):
    random_letter = random.choices(alphabet, k=1)[0]
    random_index = random.randint(0, len(name) - 1)
    list_name = list(name)
    list_name.insert(random_index, random_letter)
    return ''.join(list_name)

# generates wrong names
with open("more_name.txt", 'wt') as file:
    for name in list(names):
        if count_part(name) == 1:
            more_word = more_letter(name)
            file.write(more_word + "\n")


        elif count_part(name) == 2:
            more_word = more_letter(name[0]) + more_letter(name[1])
            file.write(more_word + "\n")

        elif count_part(name) == 3:
            more_word = more_letter(name[0]) + more_letter(name[1]) + more_letter(name[2])
            file.write(more_word + "\n")

file.close()

# generates wrong surnames
with open("more_surname.txt", 'wt') as file:
    for surname in list(surnames):
        if count_part(surname) == 1:
            more_word = more_letter(surname)
            file.write(more_word + "\n")


        elif count_part(surname) == 2:
            more_word = more_letter(surname[0]) + more_letter(surname[1])
            file.write(more_word + "\n")

        elif count_part(surname) == 3:
            more_word = more_letter(surname[0]) + more_letter(surname[1]) + more_letter(surname[2])
            file.write(more_word + "\n")

file.close()


# with open("less_name.txt", 'wt') as file:
#     for name in list(names):
#         if count_part(name) == 1:
#             less_word = less_letter(name)
#             file.write(less_word + "\n")


#         elif count_part(name) == 2:
#             less_word = less_letter(name[0]) + less_letter(name[1])
#             file.write(less_word + "\n")

#         elif count_part(name) == 3:
#             less_word = less_letter(name[0]) + less_letter(name[1]) + less_letter(name[2])
#             file.write(less_word + "\n")

# file.close()

# # generates wrong surnames
# with open("less_surname.txt", 'wt') as file:
#     for surname in list(surnames):
#         if count_part(surname) == 1:
#             less_word = less_letter(surname)
#             file.write(less_word + "\n")


#         elif count_part(surname) == 2:
#             less_word = less_letter(surname[0]) + less_letter(surname[1])
#             file.write(less_word + "\n")

#         elif count_part(surname) == 3:
#             less_word = less_letter(surname[0]) + less_letter(surname[1]) + less_letter(surname[2])
#             file.write(less_word + "\n")

# file.close()