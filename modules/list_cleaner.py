from os.path import exists

def cleaner():
    if exists("password_list.txt"):
        with open("password_list.txt", "w") as file:
            pass