import threading
import time
import requests
import pyfiglet
import colorama
from colorama import Fore
import random
import dhooks

colorama.init()

guessed = []

print(f'{Fore.LIGHTBLUE_EX}{pyfiglet.figlet_format(text="VITA C",font="larry3d")}\n'+'           ScriptedLua#2610 | https://github.com/ScriptedLua'+Fore.RED)
print("")
print("WEBHOOK URL"+Fore.RESET)
hook = str(input(""))
hook = dhooks.Webhook(hook)
print(Fore.RED+"DELAY"+Fore.RESET)
delay = float(input(""))

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0".split(" ")

def genStr(l):
    s = ""
    for i in range(l):
        g = random.choice(alphabet)
        if random.randint(1,2) == 1:
            g = g.upper()
        else:
            pass
        s += g
    return s

def checkNitro(nitro):
    api = "https://discord.com/api/v9/entitlements/gift-codes/"+nitro+"?country_code=US&with_application=false&with_subscription_plan=true"
    req = requests.get(api)
    if req.status_code == 200:
        return True
    elif req.status_code == 429:
        return None
    else:
        return False

def genNitro():
    opening = "discord.gift/"
    nitro = None
    while 1:
        nitro = opening + genStr(16)
        if not nitro in guessed:
            guessed.append(nitro)
            break
    return nitro

def main():
    while 1:
        time.sleep(delay)
        nitro = genNitro()
        valid = checkNitro(str(nitro.split("/")[1]))
        if valid:
            print(Fore.GREEN+"[+] VALID NITRO | "+nitro+Fore.RESET)
            hook.send(nitro)
        elif valid == None:
            print(Fore.LIGHTMAGENTA_EX+"RATE LIMITED"+Fore.RESET)
            time.sleep(random.randint(60,75))
        else:
            print(Fore.RED+"[-] INVALID NITRO | "+nitro+Fore.RESET)

threads = []
print(Fore.RED+"THREADS"+Fore.RESET)
threadamt = int(input(""))
for i in range(threadamt):
    t = threading.Thread(target=main)
    t.start()
    threads.append(t)
for t in threads:
    t.join()
