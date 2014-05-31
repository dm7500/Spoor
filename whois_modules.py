#-------------------------------------------------------------------------------
# Name:        whois_modules
# Purpose:
#
# Author:      dmartinez7500@gmail.com
#
# Created:     05/30/2014
#-------------------------------------------------------------------------------
import os
import sys
import whois
import datetime
import tools
import module_locater

scriptdir = module_locater.module_path()
myDate = datetime.datetime.now().strftime("%y-%m-%d")
myTime = datetime.datetime.now().strftime("%H%M")
myDateTime = datetime.datetime.now().strftime("%y-%m-%d %H%M")
resultsdir = scriptdir + '\\Results\\'
if not os.path.exists(resultsdir):
    os.makedirs(resultsdir)

def WHOIS(website):
    try:
        w = whois.whois(website)
        print "WHOIS options for \'%s\:"
        print "         1. Print full WHOIS results to file"
        print "         2. Print only specific information to file"
        scope = raw_input("Which option would you prefer? ")
        if scope == 1:
            resultsfile = resultsdir + 'WHOIS - ' + myDateTime + '.log'
            rf = open(resultsfile, 'w')
            rf.write(w.text)
            rf.close()
            return False
        elif scope == 2:
            resultsfile = resultsdir + 'WHOIS - ' + myDateTime + '.log'
            rf = open(resultsfile, 'w')
            print "Please choose which information you'd like to add to the results file: "
            domain_YN = tools.query_yes_no("Domain Name?")
            if domain_YN is True:
                for domain in w.domain_name:
                    rf.write("Domain Name: %s" % w.domain_name)
            create_YN = tools.query_yes_no("Creation Date?")
            if create_YN is True:
                for date in w.creation_date:
                    rf.write("Creation Date: %s" % w.creation)
            expire_YN = tools.query_yes_no("Expiration Date?")
            update_YN = tools.query_yes_no("Last Updated Date?")
            emails_YN = tools.query_yes_no("Emails?")
            nameservers_YN = tools.query_yes_no("Name Servers?")
            regis_YN = tools.query_yes_no("Registrar?")
            status_YN = tools.query_yes_no("Status?")

            rf.write ("""
            Domain Name: %s
            Creation Date: %s
            Expiration Date: %s
            Updated Date: $s
            E-Mails: %s
            Name Servers: %s
            Registrar: %s
            Status: %s
            """ % (w.domain_name, w.creation_date, w.expiration_date, w.updated_date, w.emails, w.name_servers, w.registrar, w.status))
            return False
        narrow = tools.query_yes_no("would you like to display ")
    except TypeError, e:
        print "Error: %s" % e
        return False



def main():
    pass

if __name__ == '__main__':
    main()
