from colorama import Fore , Style
from sys import exit , platform
import requests
from time import sleep
from os import system
########################
def __Start__():
########################
    SomeUrl = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']
########################
    sleep(0.2)
    print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Wellcome To Directory On Page Finder Part")
    sleep(0.2)
    print (Fore.LIGHTGREEN_EX + " \n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Ctrl + C To Exit")
#####################
    try :
        sleep(0.2)
        Domain = input(Fore.LIGHTGREEN_EX +"\n┌─["+Fore.LIGHTWHITE_EX+"!"+ Fore.LIGHTGREEN_EX + "]" + Fore.RED+" Enter Your Domain" + Fore.LIGHTGREEN_EX + """
└──╼"""+Fore.LIGHTWHITE_EX+" ")
#####################
        if not Domain :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " You Didn't Enter Anything")
            sleep(2)
            return 
#####################
        elif "http" in Domain :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Please Enter A Domain")
            sleep(2)
            return 
#####################
        Domain = "http://" + Domain + "/"
#####################
        for Url in SomeUrl :
            try :
                Site = requests.get(Domain+Url)
                if Site.status_code == 200 or Site.status_code == 405:
                    sleep(0.2)
                    print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "+" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "Directory" + Fore.RED + " | " + Fore.LIGHTGREEN_EX + Domain+Url + Fore.RED + " | " + Fore.LIGHTCYAN_EX + "Found")
                else :
                    print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "-" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "Directory" + Fore.RED + " | " + Fore.LIGHTGREEN_EX + Domain+Url + Fore.RED + " | " + Fore.LIGHTCYAN_EX + "Not Found")
            except :
                sleep(0.2)
                print (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " You Didn't Enter A True Domain Or You Pressed Ctr + C")
                sleep(2)     
                return 
#####################
        input (Fore.LIGHTGREEN_EX + "\n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.RED + " Press Enter To Exit ")
#####################
    except :
        return 
