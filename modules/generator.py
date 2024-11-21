from random import choice
from string import ascii_letters,digits,punctuation,ascii_uppercase,hexdigits
from pyperclip import copy

class Generator:
    def passwgen(self, passw_length):
        password = ""
        
        while len(password) <= passw_length:
            password += choice(
                ascii_letters + digits + punctuation + ascii_uppercase + hexdigits
                )
            
        copy(password)
        
        return password

    def password_list(self, passw_length, passw_qty):
        with open("password_list.txt", "a") as file:
            num = 0
            passwords = []
            passw_qty = int(passw_qty)
            
            while num <= passw_qty:
                password = ""
                if passw_length != "Random":
                    passw_length = int(passw_length)
                    while len(password) <= passw_length:
                        password += choice(
                            ascii_letters + digits + punctuation + ascii_uppercase + hexdigits
                            )
                else:
                    lengths = [8, 12, 16, 20, 24, 28]
                    passw_length = choice(lengths)
                    while len(password) <= passw_length:
                        password += choice(
                            ascii_letters + digits + punctuation + ascii_uppercase + hexdigits
                            )
                        
                file.write(password+"\n")
                file.write("\n")
                
                passwords.append(password)
                num+=1
                
            file.close()
            
        return password