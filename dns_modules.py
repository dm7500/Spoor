#-------------------------------------------------------------------------------
# Name:        DNS_modules
# Purpose:
#
# Author:      dmartinez7500@gmail.com
#
# Created:     05/31/2014
#-------------------------------------------------------------------------------
import os
import sys
import tools
import module_locater
import dns.resolver
import datetime

scriptdir = module_locater.module_path()
myDate = datetime.datetime.now().strftime("%y-%m-%d")
myTime = datetime.datetime.now().strftime("%H%M")
myDateTime = datetime.datetime.now().strftime("%y-%m-%d %H%M")
resultsdir = scriptdir + '\\Results\\'
if not os.path.exists(resultsdir):
    os.makedirs(resultsdir)

def DNS(host, recordtype):
    answers = dns.resolver.query(host, recordtype)
    for rdata in answers:
        print('Host', rdata.exchange, 'has preference', rdata.preference)



def main():
    pass

if __name__ == '__main__':
    main()
