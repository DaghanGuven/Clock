from datetime import datetime
from time import sleep
import os

print("\033[1m")

current_time = "00:00:00"
clear = lambda: os.system('clear')
figlet_call = lambda: os.system('figlet '+current_time)

while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        figlet_call()
        sleep(1)
        clear()
