from os import system, name

def cli_cleaner():
    system('cls' if name == 'nt' else 'clear')