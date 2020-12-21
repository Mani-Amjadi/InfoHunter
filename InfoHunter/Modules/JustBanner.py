from colorama import Fore , Style
from time import sleep
from os import system
import sys
##################################
if "win" in sys.platform :
    command = "cls"
elif "linux" in sys.platform :
    command = "clear"
##################################
def __Start__():
    sleep(0.2)
    system(command)
    print (Fore.LIGHTGREEN_EX + """
  _____        __                            _             
  \_   \_ __  / _| ___     /\  /\_   _ _ __ | |_ ___ _ __  
   / /\/ '_ \| |_ / _ \   / /_/ / | | | '_ \| __/ _ \ '__|""" + Fore.RED + """ Github : https://github.com/Mani-Amjadi"""+Fore.LIGHTCYAN_EX+"""
/\/ /_ | | | |  _| (_) | / __  /| |_| | | | | ||  __/ |""" + Fore.RED + " Created By Mani Amjadi" +Fore.LIGHTCYAN_EX+ """   
\____/ |_| |_|_|  \___/  \/ /_/  \__,_|_| |_|\__\___|_|""" + Fore.RED + " Version 1.0")