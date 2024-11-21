from interface.interface_layout import layout
from modules.generator import Generator
from modules.validator import validate_password
from modules.password_list_show import passw_list_show, passw_headlist_show
from modules.list_cleaner import cleaner
from modules.cli_cleaner import cli_cleaner
from questionary import select, Style, text, confirm
from colorama import Fore
from time import sleep

class App:
    def run(self):
        custom_style = Style([
            ('pointer', 'fg:#e80013'),
            ('highlighted', 'fg:#fff'),
            ('question', 'fg:#ff3d4d',),
            ('text', 'fg:#e80013')
        ])
        
        generator = Generator()
        layout()
        sleep(1)
        
        while True:
            try:
                user_input = select(
                    "Functions:",
                    choices=[
                        "Password Generator",
                        "Password List Generator",
                        "Password Validator",
                        "Show Password List",
                        "Clear Password List",
                        "Exit"
                    ],
                    style=custom_style,
                    qmark="",
                    instruction=" "
                ).ask()
                
                if user_input == "Password Generator":
                    cli_cleaner()
                    layout()
                    
                    length = select(
                        "Password Length:",
                        choices=["8", "12", "16", "20", "24", "28"],
                        style=custom_style,
                        qmark="",
                        instruction=" "
                    ).ask()
                    
                    print(f"\n\t{Fore.WHITE}{generator.passwgen(int(length))}\n")
                    print(f"{Fore.GREEN}Password copied!")
                    
                if user_input == "Password List Generator":
                    cli_cleaner()
                    layout()
                    
                    length = select(
                        "Password Length:",
                        choices=["8", "12", "16", "20", "24", "28", "Random"],
                        style=custom_style,
                        qmark="",
                        instruction=" "
                    ).ask()
                    
                    passw_qty = text("Enter the quantity of passwords: ", 
                                    style=custom_style, 
                                    qmark=""
                                    ).ask()
                    
                    generator.password_list(length, passw_qty)
                    print(f"{Fore.GREEN}Password list created!")
                
                if user_input == "Password Validator":
                    cli_cleaner()
                    layout()
                    
                    password = text("Enter the password: ",
                                    style=custom_style, 
                                    qmark=""
                                    ).ask()
                    print(f"{Fore.GREEN}\n\t{validate_password(password)}\n")
                        
                if user_input == "Show Password List":
                    cli_cleaner()
                    layout()
                    
                    show_options = select(
                        "Show Options:",
                        choices=[
                            "Show All",
                            "Show Head(First 5 lines)"
                        ],
                        style=custom_style,
                        qmark="",
                        instruction=" "
                        ).ask()
                    
                    if show_options == "Show All":
                        print(passw_list_show())
                        
                    elif show_options == "Show Head(First 5 lines)":
                        pasw_show = passw_headlist_show()
                        print(pasw_show)
                
                if user_input == "Clear Password List":
                    cli_cleaner()
                    layout()
                    confirmation = confirm("Are you sure?").ask()
                    if confirmation:
                        cleaner()
                        print(f"{Fore.GREEN}Password list cleared!")
                    else:
                        cli_cleaner()
                        layout()
                
                if user_input == "Exit":
                    print(f"{Fore.WHITE}Goodbye!{Fore.RESET}")
                    break
                
            except ValueError:
                print(f"{Fore.WHITE}Invalid input.{Fore.RESET}")
                
if "__main__" == __name__:
    app = App()
    app.run()
    