def thesaurus(*names):
    my_list = [*names]
    my_dict = {}

    for name in my_list:
        key_1 = name[0]
        if key_1 not in my_dict:
            my_dict[key_1] = []
        my_dict[key_1].append(name)

    print(my_dict)


thesaurus('игорь ', "вася", 'петя', "сережа", "саша")