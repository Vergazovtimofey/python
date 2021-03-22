import sys
import json

with open('users.csv', 'r', encoding='utf-8') as my_file:
    users = my_file.read().splitlines()


with open('hobby.csv', 'r', encoding='utf-8') as file:
    hobby = file.read().splitlines()
users_dict = {}
for i, el in enumerate(users):
    if i < len(hobby):
        users_dict[el.replace(",", " ")] = hobby[i].replace(",", "")
    else:
        users_dict[el.replace(",", " ")] = None
print(users_dict)

if len(hobby) > len(users):
    sys.exit(1)


with open("users_dictionary.json", "w", encoding="UTF-8") as f:
    json.dump(users_dict, f, ensure_ascii=False)