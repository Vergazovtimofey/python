with open("users.csv", "r", encoding="UTF-8") as file_users:
    with open("hobby.csv", "r", encoding="UTF-8") as file_hobby:
        with open("users_hobby.txt", "w", encoding="UTF-8") as file:
            user_line = file_users.readline().strip()
            while user_line:
                hobby_line = file_hobby.readline().strip()
                file.write(f"{user_line}: {hobby_line}\n")
                user_line = file_users.readline().strip()