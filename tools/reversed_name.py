import pandas as pd

surname_data = pd.read_csv("~/personal/correct_dataset/surname_2.csv")["Names"]
name_data = pd.read_csv("~/personal/correct_dataset/names.csv")["Names"]
surname_data.drop_duplicates()
name_data.drop_duplicates()

# sur_select = surname_data.loc[surname_data['Names']]
# name_select = name_data.loc[name_data['Names'] > 10]
print(surname_data)

with open("reverced_name.txt", 'wt') as f:
    for i in surname_data:
        for j in name_data:
            print(i + " " + j)
            f.write(i + " " + j + "\n")
f.close()
# print(sur_select[1])