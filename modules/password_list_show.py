from os.path import exists

def passw_headlist_show():
    if exists("password_list.txt"):
        with open("password_list.txt", "r") as file:
            lines = []
            for x, line in enumerate(file, start=1):
                lines.append(line.strip())
                if x == 10:  
                    break
            return f"{"\n".join(lines) if lines else "No content in file."}"
    else:
        return "No password list found."

def passw_list_show():
        if exists("password_list.txt"):
            with open("password_list.txt", "r") as file:
                content = file.read()
            return f"{"\n" if content else "No content in file."}"
        else:
            return "No password list found."