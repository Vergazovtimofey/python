def prof():
    files = input(' введите через пробел: имя, фамилия, год рождения, город проживания, email, телефон')
    files = files.split()
    soft = ['name:', 'surname:', 'year:', 'city:', 'email:', 'phone:']
    for softs, file in zip(soft, files):
        print(softs, file)
    print(dict(zip(soft, files)))
    print(list(zip(soft, files)))

prof()