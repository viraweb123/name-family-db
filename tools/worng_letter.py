import pandas as pd
import random
zs="ضظز"
s_letters="سثص"
def change_letters(word):
    for i in word :
        g=random.randint(0,1)
        d=random.randint(0,2)
        f=random.randint(0,3)
        if 'ز' in word:
            newword=word.replace('ز',zs[d])
        elif 'ظ' in word:
            newword=word.replace('ظ',zs[d])
        elif 'ض' in word:
            newword=word.replace('ض',zs[d]) 
        elif 'س' in word:
            newword=word.replace('س',s_letters[d])
        elif 'ث' in word:
            newword=word.replace('ث',s_letters[d])
        elif 'ص' in word:
            newword=word.replace('ص',s_letters[d])
        elif 'ط' in word:
            newword=word.replace('ط','ت')
        elif 'ت' in word :
            newword=word.replace('ت','ط')
        else:
            return word           
    return newword


surname_data = pd.read_csv("~/personal/correct_dataset/surname_2.csv")["Names"]
name_data = pd.read_csv("~/personal/correct_dataset/names.csv")["Names"]
surname_data.drop_duplicates()
name_data.drop_duplicates()

with open("final_wrong_letter.txt", 'wt') as f:
    for i in surname_data:
        for j in name_data:
            print(change_letters(i) + " " + change_letters(j))
            f.write(change_letters(i) + " " + change_letters(j) + "\n")
f.close()