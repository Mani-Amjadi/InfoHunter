from colorama import Fore , Style
from sys import exit , platform
from socket import gethostbyname
from time import sleep
from os import system
########################
def __Start__():
########################
    Subdomains = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']
    sleep(0.2)
    print (Fore.LIGHTGREEN_EX + " \n  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Wellcome to Cloudflare Bypass Part")
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
        for Subdomain in Subdomains:
            try :
                Host = Subdomain + "." + Domain
                Bypass = gethostbyname(Host)
                print (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "*" + Fore.LIGHTGREEN_EX + "] " + Fore.LIGHTCYAN_EX + "Bypass Cloudflare" + Fore.RED + " | " + Fore.LIGHTGREEN_EX + Host + Fore.RED + " | " + Fore.LIGHTCYAN_EX + Bypass + "\n")
            except :
                pass
##########################
        input (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.RED + " Press Enter To Exit ")
##########################
    except :
        return 
        


        
