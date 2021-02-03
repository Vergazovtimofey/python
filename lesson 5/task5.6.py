subj = {}
with open("lessons.txt", 'r') as my_file:
    for line in my_file:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {subj}')


