def thesaurus_adv(*args):
    dict_1 = {}
    for name in args:
        find = name[name.find(' ') + 1]
        if find not in dict_1:
            dict_1[find] = dict()

        if name[0] in dict_1[find]:
            dict_1[find][name[0]].append(name)
        else:
            dict_1[find].setdefault(name[0], [name])
    return dict_1


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Гванов", "Анна Савельева"))



