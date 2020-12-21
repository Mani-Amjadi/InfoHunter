from Modules import Banner , JustBanner , CloudFlare , Cms , AdminPageFinder , DnsLookup , FindSharedDns , HttpHeader , IpLocation , WhoIs , PortScan , WordPress , ReverseIp , DirectoryOnServer , About
from colorama import Fore , Style
from sys import exit , platform
from time import sleep
from os import system
##########################
if "win" in platform :
    Command = "cls"
elif "linux" in platform :
    Command = "clear"
###########################################
while True :
##################################
    Banner.__Start__()
##################
    try :
        sleep(0.2)
        Option = input(Fore.LIGHTGREEN_EX +"\n┌─["+Fore.LIGHTWHITE_EX+"!"+ Fore.LIGHTGREEN_EX + "]" + Fore.RED+" Select An Option" + Fore.LIGHTGREEN_EX + """
└──╼"""+Fore.LIGHTWHITE_EX+" ")
###################
        if Option == "1" or Option == "01":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            CloudFlare.__Start__()
###################
        elif Option  == "2" or Option == "02":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            Cms.__Start__()
###################
        elif Option == "3" or Option == "03":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            AdminPageFinder.__Start__()
###################
        elif Option == "4" or Option == "04":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            DnsLookup.__Start__()
###################
        elif Option == "5" or Option == "05":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            FindSharedDns.__Start__()
###################
        elif Option == "6" or Option == "06":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            HttpHeader.__Start__()
################
        elif Option == "7" or Option == "07":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            IpLocation.__Start__()
################
        elif Option == "8" or Option == "08":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            WhoIs.__Start__()
################
        elif Option == "9" or Option == "09":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            PortScan.__Start__()
###############
        elif Option == "10":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            WordPress.__Start__()
###############
        elif Option == "11":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            ReverseIp.__Start__()
###############
        elif Option == "12":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            DirectoryOnServer.__Start__()
###############
        elif Option == "100":
            sleep(0.2)
            system(Command)
            exit()
###############
        elif Option == "99":
            sleep(0.2)
            JustBanner.__Start__()
            sleep(0.2)
            About.__Start__()
###############
        else :
            sleep(0.2)
            print (Fore.LIGHTGREEN_EX + "  [" + Fore.LIGHTWHITE_EX + "!" + Fore.LIGHTGREEN_EX + "]" + Fore.LIGHTCYAN_EX + " Please Select A true Option")
            sleep(2)
###################
    except :
        system(Command)
        exit()
###################
