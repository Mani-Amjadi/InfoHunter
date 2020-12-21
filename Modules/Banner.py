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
    try:
        sleep(0.2)
        system(command)
        print (Fore.LIGHTGREEN_EX + """
  _____        __                            _             
  \_   \_ __  / _| ___     /\  /\_   _ _ __ | |_ ___ _ __  
   / /\/ '_ \| |_ / _ \   / /_/ / | | | '_ \| __/ _ \ '__|""" + Fore.RED + """ Github : https://github.com/Mani-Amjadi"""+Fore.LIGHTCYAN_EX+"""
/\/ /_ | | | |  _| (_) | / __  /| |_| | | | | ||  __/ |""" + Fore.RED + " Created By Mani Amjadi" +Fore.LIGHTCYAN_EX+ """   
\____/ |_| |_|_|  \___/  \/ /_/  \__,_|_| |_|\__\___|_|""" + Fore.RED + " Version 1.0")
        sleep(0.2)
        print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "1" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Bypass Cloudflare      " +Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "5" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Find Shared Dns      "+Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "9" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Port Scaner")
        sleep(0.2)
        print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "2" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Technology Detect      " +Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "6" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Http Header          "+Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "10" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Cms Detect")
        sleep(0.2)
        print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "3" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Admin Page Finder      " +Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "7" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Find Ip Location     "+Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "11" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Find Website On Server")
        sleep(0.2)
        print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "4" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Dns Lookup             " +Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "8" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Who Is               "+Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "12" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Find Directory On Website")
        sleep(0.2)
        print ("\n  " + Fore.LIGHTGREEN_EX + "⋆" * 14+ Fore.LIGHTWHITE_EX + "⋆"*14 + Fore.LIGHTCYAN_EX+ "⋆" * 14+ Fore.RED+ "⋆" * 14)
        sleep(0.2)
        print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "99" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " About                 " +Fore.LIGHTGREEN_EX + "[" + Fore.LIGHTWHITE_EX + "100" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Exit               ")
        #print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "99" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " About \n")
        #sleep(0.2)
        #print (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "100" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Exit ")

    except :
        sleep(0.2)
        sys.exit()