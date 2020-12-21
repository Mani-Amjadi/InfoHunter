from colorama import Fore , Style
from sys import exit , platform
import requests
from socket import gethostbyname
import ipapi
from time import sleep
from os import system
########################
def __Start__():
########################
    sleep(0.2)
    print (Fore.LIGHTGREEN_EX + " \n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Wellcome To Ip Location Part")
    sleep(0.2)
    print (Fore.LIGHTGREEN_EX + " \n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Ctrl + C To Exit")
########################
    try :
        sleep(0.2)
        Domain = input(Fore.LIGHTGREEN_EX +"\n┌─["+Fore.LIGHTWHITE_EX+"!"+ Fore.LIGHTGREEN_EX + "]" + Fore.RED+" Enter Your Domain" + Fore.LIGHTGREEN_EX + """
└──╼"""+Fore.LIGHTWHITE_EX+" ")
        if not Domain :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " You Didn't Enter Anything")
            sleep(2)
            return 
########################
        elif "http" in Domain :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Please Enter A Domain")
            sleep(2)
            return
########################
        Ip = gethostbyname(Domain)
########################
        Info = ipapi.location(ip=Ip)
#########################
        try :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "+" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "ip" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["ip"])
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "+" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "city" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["city"])
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "region" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["region"])
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "id country" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["country"])
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "country" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["country_name"])
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "calling code" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["country_calling_code"])
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "languages" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["languages"])
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "org" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Info["org"])
        except :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " You Didn't Enter A True Domain Or You Pressed Ctr + C")
            sleep(2)
            return
#########################
        input (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "]" + Fore.RED + " Press Enter To Exit ")
######################### 
    except :
        return
#########################


        
