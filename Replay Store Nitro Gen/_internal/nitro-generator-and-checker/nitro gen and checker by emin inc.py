from keyauth import api

import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime

# import json as jsond
# ^^ only for auto login/json writing/reading

# watch setup video if you need help https://www.youtube.com/watch?v=L2eAQOmuUiA

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title Python Example')  # clear console, change title
    elif platform.system() == 'Linux':
        os.system('clear')  # clear console
        sys.stdout.write("\x1b]0;Python Example\x07")  # change title
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'")  # clear console
        os.system('''echo - n - e "\033]0;Python Example\007"''')  # change title

print("Initializing")


def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name = "Gen Replay", # Application Name
    ownerid = "yTCq8jjSKL", # Owner ID
    secret = "580162b36578af660cd482cd24ba4baa13598b68ad8298ab8a42971953caa11a", # Application Secret
    version = "1.0", # Application Version
    hash_to_check = getchecksum()
)

def answer():
    try:
        print("""
1.License Key Only
        """)
        ans = input("Select Option: ")
        if ans == "1":
            key = input('Enter your license: ')
            keyauthapp.license(key)
        else:
            print("\nInvalid option")
            sleep(1)
            clear()
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()

'''try:
    if os.path.isfile('auth.json'): #Checking if the auth file exist
        if jsond.load(open("auth.json"))["authusername"] == "": #Checks if the authusername is empty or not
            print("""
1. Login
2. Register
            """)
            ans=input("Select Option: ")  #Skipping auto-login bc auth file is empty
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license) 
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        else:
            try: #2. Auto login
                with open('auth.json', 'r') as f:
                    authfile = jsond.load(f)
                    authuser = authfile.get('authusername')
                    authpass = authfile.get('authpassword')
                    keyauthapp.login(authuser,authpass)
            except Exception as e: #Error stuff
                print(e)
    else: #Creating auth file bc its missing
        try:
            f = open("auth.json", "a") #Writing content
            f.write("""{
    "authusername": "",
    "authpassword": ""
}""")
            f.close()
            print ("""
1. Login
2. Register
            """)#Again skipping auto-login bc the file is empty/missing
            ans=input("Select Option: ") 
            if ans=="1": 
                user = input('Provide username: ')
                password = input('Provide password: ')
                keyauthapp.login(user,password)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            elif ans=="2":
                user = input('Provide username: ')
                password = input('Provide password: ')
                license = input('Provide License: ')
                keyauthapp.register(user,password,license)
                authfile = jsond.load(open("auth.json"))
                authfile["authusername"] = user
                authfile["authpassword"] = password
                jsond.dump(authfile, open('auth.json', 'w'), sort_keys=False, indent=4)
            else:
                print("\nNot Valid Option") 
                os._exit(1) 
        except Exception as e: #Error stuff
            print(e)
            os._exit(1) 
except Exception as e: #Error stuff
    print(e)
    os._exit(1)'''


import random
import string
import requests
import concurrent.futures

print("""

┏━━━┓╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋┏━━━┓┏┓
┃┏━┓┃╋╋╋╋╋┃┃╋╋╋╋╋╋╋╋┃┏━┓┣┛┗┓
┃┗━┛┣━━┳━━┫┃┏━━┳┓╋┏┓┃┗━━╋┓┏╋━━┳━┳━━┓
┃┏┓┏┫┃━┫┏┓┃┃┃┏┓┃┃╋┃┃┗━━┓┃┃┃┃┏┓┃┏┫┃━┫
┃┃┃┗┫┃━┫┗┛┃┗┫┏┓┃┗━┛┃┃┗━┛┃┃┗┫┗┛┃┃┃┃━┫
┗┛┗━┻━━┫┏━┻━┻┛┗┻━┓┏┛┗━━━┛┗━┻━━┻┛┗━━┛
╋╋╋╋╋╋╋┃┃╋╋╋╋╋╋┏━┛┃
╋╋╋╋╋╋╋┗┛╋╋╋╋╋╋┗━━┛
""")
       
print("Nitro Generator And Checker")

def generate_code(length=19):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

def generate_gift_code():
    code = generate_code()
    return f"https://discord.gift/{code}"

def check_code_validity(code):
    url = f"https://discord.com/api/v8/entitlements/gift-codes/{code.split('/')[-1]}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def save_valid_code(code):
    with open("valid_gift_codes.txt", "a") as file:
        file.write(code + "\n")

def check_code(code):
    if check_code_validity(code):
        print(f"\033[92m{code} - Valid\033[0m")
        save_valid_code(code)
    else:
        print(f"\033[91m{code} - Invalid\033[0m")

def main():
    num_codes = int(input("Enter the number of codes to generate: "))
    
    print("Checking code validity...")
    
    valid_codes = 0
    invalid_codes = 0
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_code, generate_gift_code()) for _ in range(num_codes)]
        for future in concurrent.futures.as_completed(futures):
            if future.result() is None:
                invalid_codes += 1
            else:
                valid_codes += 1
    
    print(f"\nSummary:")
    print(f"Valid codes: {valid_codes}")
    print(f"Invalid codes: {invalid_codes}")

if __name__ == "__main__":
    main()
