

def thesaurus_adv(*names):

    my_list = [*names]
    my_dict = {}
    my_dict1 = {}


    for name in my_list:
        key_1 = name[5]
        key_2 = name[0]
        if key_1 not in my_dict:

             if key_2 not in my_dict1:

                  my_dict1[key_2] = []
             my_dict1[key_2].append(name)

             my_dict[key_1] = []

        my_dict[key_1].append(my_dict1)
    print(my_dict)

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")