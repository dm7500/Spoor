# --------------------------------------------------
# Project: Spoor
# Name:    Spoor 
# Created: 6/7/2014
# Author: David.Martinez
#
# Created using PyCharm Community Edition
#--------------------------------------------------

#Import of Python Modules
import os
import sys
import shodan
import tools
import module_locater
import logging
import datetime
import getopt
import shodan_modules
import optparse
import whois_modules
import time
import dns.resolver
import dns_modules

SHODAN_API_KEY = "tENIC6XGeNrYJHt0xzGYN5NT7RaZAvq6"
scriptdir = module_locater.module_path()
myDate = datetime.datetime.now().strftime("%y-%m-%d")
myTime = datetime.datetime.now().strftime("%H:%M")
myDateTime = datetime.datetime.now().strftime("%y-%m-%d %H:%M")

###Logging Setup
##logger = logging.getLogger('Spoor')
##logdate = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
##logfile = scriptdir + '\\Logs\\Spoor-' + logdate + '.log'
##hdlr = logging.FileHandler(logfile)
##formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
##hdlr.setFormatter(formatter)
##logger.addHandler(hdlr)
##logger.setLevel(logging.INFO)

header = """
***************************************
*                                     *
*    Spoor Network Enumeration Tool   *
*                                     *
***************************************
\n"""

#Main Menu function
def main_menu():
    os.system('cls')
    print header
    print
    print "Main Menu:"
    print "         1. SHODAN"
    print "         2. WHOIS"
    print "         3. NSLOOKUP/DNS Queries"
    print "         4. Exit Spoor"
    function = int(input("Please choose a function: "))
    if function == 1:
        SHODAN_MENU()
        return True
    elif function == 2:
        WHOIS_MENU()
        return True
    elif function == 3:
        DNS_MENU()
        return True
    elif function == 4:
        print "Thanks for using Spoor."
        sys.exit()
    else:
        print "Unknown option."
        return False
        #TODO: Find a way to use these False and True returns

def WHOIS_MENU():
    os.system('cls')
    print header
    print
    print "WHOIS Menu:"
    print "         1. Search by site"
    print "         2. Return to Main Menu"
    function = int(input("Please enter a WHOIS option: "))
    if function == 1:
        host = raw_input('Please enter the site address to search: ')
        host_check = tools.query_yes_no("You entered \'%s\'. Is this correct? " % host)
        if host_check is True:
            whois_modules.WHOIS(host)
            return False
        else:
            host = raw_input("Sorry about that. Please enter the correct site address to search on: ")
            whois_modules.WHOIS(host)
            return False
    if function == 2:
        main_menu
        return False

def DNS_MENU():
    os.system('cls')
    print header
    print
    print "DNS Menu:"
    print "     1. Search by host and record type"
    print "     2. Return to Main Menu"
    function = int(input("Please enter a DNS option:"))
    if function == 1:
        host = raw_input("Please enter a host name to search for: ")
        #TODO: Do I need a new function for each record type?
        print "Please choose a DNS record type from the list below: "
        print "     1. NS - Basic Name Server Lookup"
        print "     2. MX - Mail record lookup"
        print "     3. A - Basic reverse lookup, providing an IPv4 address"
        print "     4. AAAA - Basic reverse lookup, providing an IPv6 address"
        print "     5. TXT - Search for a text-only record."
        rec_choice = int(input("Please enter the record type to search for: "))
        if rec_choice == 1:
            recordtype = 'NS'
        if rec_choice == 2:
            recordtype = 'MX'
        if rec_choice == 3:
            recordtype = 'A'
        if rec_choice == 4:
            recordtype = 'AAAA'
        if rec_choice == 5:
            recordtype = 'TXT'
        print "Searching for \'%s\' with a record type of \'%s\'..." % (host, recordtype)
        dns_modules.DNS(host, recordtype)
        raw_input("Press <ENTER> to continue...")
        DNS_MENU()
        return False
    else:
        main_menu()
        return False


def SHODAN_MENU():
    os.system('cls')
    print header
    print
    print "SHODAN Menu:"
    print "         1. Search by host"
    print "         2. Search by keyword"
    print "         3. Return to Main Menu"
    function = int(input("Please enter a SHODAN search mode: "))
    if function == 1:
        keyword = raw_input('Please enter the host IP to search: ')
        kw_correct = tools.query_yes_no("You entered %s. Is this corect? " % keyword)
        if kw_correct is True:
            shodan_modules.SHODAN_HOSTNAME(keyword)
            return False
        else:
            keyword = raw_input('Sorry about that. Please enter the correct host IP to search: ')
            shodan_modules.SHODAN_HOSTNAME(keyword)
            return False
    elif function == 2:
        keyword = raw_input("Please enter a search term: ")
        kw_correct = tools.query_yes_no("You entered %s. Is this corect? " % keyword)
        if kw_correct is True:
            shodan_modules.SHODAN_KEYWORD(keyword)
            return False
        else:
            keyword = raw_input('Sorry about that. Please enter the correct host IP to search: ')
            shodan_modules.SHODAN_KEYWORD(keyword)
            return False
    elif function == 3:
        main_menu()
        return False
    else:
        print "Unknown option"
        return False

def main():
    main_menu()
##    if shodan_modules.key1:
##        print shodan_modules.key1
##    else:
##        pass
##    if shodan_modules.IP1:
##        print shodan_modules.IP1
##    else:
##        pass




if __name__ == '__main__':
    main()

