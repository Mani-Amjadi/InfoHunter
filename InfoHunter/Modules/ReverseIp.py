from colorama import Fore , Style
from sys import exit , platform
import requests
import json
from time import sleep
from socket import gethostbyname
from os import system
########################
def __Start__():
########################
    sleep(0.2)
    print (Fore.LIGHTGREEN_EX + " \n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Wellcome To Reverse Ip Part")
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
        try:
            data = {"remoteAddress":Domain}

            link = requests.post("https://domains.yougetsignal.com/domains.php" , data )

            source = json.loads(link.content)
#########################
            Ip = (gethostbyname(Domain))
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX  + "ip" + Fore.RED + " : " + Fore.LIGHTGREEN_EX + Ip)
#########################
            for info in source["domainArray"]:
                sleep(0.2)
                print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + info[0] + Fore.RED + " -")
##########################
        except :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " You Didn't Enter A True Domain Or You Pressed Ctr + C")
            sleep(2)
##########################
        input (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.RED + " Press Enter To Exit ")
##########################
    except :
        return 

        
