#-------------------------------------------------------------------------------
# Name:        tools
# Purpose:      Utility functions for application.
#
# Author:      dmartinez7500@gmail.com
#
# Created:     05/19/2014
#-------------------------------------------------------------------------------
import sys

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

def pushover(message, app_token):
    """Provide an API call to Pushover for mobile notifications of events in the script.

    "message" is a string that will display on the Pushover notification.
    "app_token" is a string for the app token provided by Pushover.
    """
    import urllib, httplib
    conn = httplib.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.urlencode({
    "token": app_token,
    "user": "uU95W9hYqeW3b24uyPaT1skT1SG35N",
	"message": message,
	}), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

def make_zipfile(output_filename, source_dir):
    """Creates a compressed ZIP file. ZIP64 is enabled, which will allow for files larger then 4GB.

    "output_filename" is a path you'd like the ZIP created in. Example: C:\Temp\NewZip.zip
    "source_dir is the path to the folder you'd like to create a ZIP file from. Example: C:\Temp
    """
    import zipfile, zlib
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED, allowZip64) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)

def is_64_bit():
    return platform.machine().endswith('64')
