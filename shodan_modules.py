#-------------------------------------------------------------------------------
# Name:        SHODAN
# Purpose:
#
# Author:      dmartinez7500@gmail.com
#
# Created:     05/20/2014
#-------------------------------------------------------------------------------
import shodan, os, sys, tools, datetime, module_locater, Spoor

SHODAN_API_KEY = "tENIC6XGeNrYJHt0xzGYN5NT7RaZAvq6"
scriptdir = module_locater.module_path()
myDate = datetime.datetime.now().strftime("%y-%m-%d")
myTime = datetime.datetime.now().strftime("%H%M")
myDateTime = datetime.datetime.now().strftime("%y-%m-%d %H%M")
resultsdir = scriptdir + '\\Results\\'
if not os.path.exists(resultsdir):
    os.makedirs(resultsdir)

api = shodan.Shodan(SHODAN_API_KEY)

def SHODAN_HOSTNAME(IP):
    try:
        host = api.host(IP)
        print ("""
            IP: %s
            Organization: %s
            Operating System: %s
        """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
        print()
        banners = tools.query_yes_no("Do you want to print banners for this IP to a file? ")
        if banners is True:
            for item in host['data']:
                resultsfile = resultsdir + 'HostBanners - ' + myDateTime + '.log'
                rf = open(resultsfile, 'w')
                rf.write( """
                    Port: %s
                    Banner: %s

                """ % (item['port'], item['data']))
            rf.close()
            Spoor.SHODAN_MENU()
        else:
            return False
        IP2Mem = tools.query_yes_no("Do you want to keep \'%s\' in memory for later use? " % IP)
        if IP2Mem is True:
            global IP1
            IP1 = IP
            return IP1
        else:
            return False

    except shodan.APIError, e:
        print("Error: %s" % e)
        input("Press any key to continue...")
        Spoor.SHODAN_MENU()


def SHODAN_KEYWORD(keyword):
    try:
        results = api.search(keyword)

##        print "Found " + results['total'] + " total results for %s." % keyword
        write2file = tools.query_yes_no("Do you want to write the results to a file? ")
        if write2file is True:
            resultsfile = resultsdir + 'KeywordResults - ' + myDateTime + '.log'
            rf = open(resultsfile, 'w')
            for result in results['matches']:
                rf.write('IP: %s' % result['ip_str'])
                rf.write('\n')
                rf.write(result['data'])
                rf.write('\n')
                rf.write('------------------------------------')
                rf.write('\n')
            rf.close()
        else:
            for result in results['matches']:
                print('IP: %s' % result['ip_str'])
                print(result['data'])
                print ('')
        key2mem = tools.query_yes_no("Do you want to keep \'%s\' in memory for future use? " % keyword)
        if key2mem is True:
            global key1
            key1 = keyword
            return key1

    except shodan.APIError, e:
        print ("Error: %s" % e)
        input("Press any key to continue...")
        Spoor.main_menu()

def main():
    pass

if __name__ == '__main__':
    main()
