import mechanize
from bs4 import BeautifulSoup
import urllib3 
import http.cookiejar
import time
import hashlib
import requests
import os
import sys
import smtplib
from os.path import exists

def firstTimer():
    print("Remember to get into bit.ly/googleSecurityL and turn less secure apps on")
    mail = input("Write the gmail account address (new throwaway acc is preferred): ")
    passwd = input("Write its password: ")
    persmail = input("Write your personal email: ")
    with open('private.py', 'w') as f:
        original_stdout = sys.stdout
        sys.stdout = f
        print('gmail_user = \'' + mail + '\'')
        print('gmail_password = \'' + passwd + '\'')
        print('personal_mail = \'' + persmail + '\'')
        sys.stdout = original_stdout
    TITLE = input("What is the title of the course you wanna track? ")
    isWanted = input("Do you want a specific section, or I shall send you updates for all of them? (Write yes or no)")
    if isWanted == 'yes':
        TIMEQUER = True
        TTIME = input("What hour does the needed section starts in? (Example: 11)")
        TIME = [TTIME]
    RATE = input("At what rate do you want me to check? Recommended is 20-30 ")
        

    
## EXAMPLE FOR private FILE
## Remember turning on less secure apps from gmail security settings if you're using it
# gmail_user = 'email@gmail.com'
# gmail_password = 'passw@rd'

# Course details
TITLE = 'Differential Equations'

# Add department letters
DEPT = "MACT"

# get your semester's value from inspect element and add it here
SEMS = ['202220']

# Starting time of the desired section, if not make it false
TIMEQUER = False 
TIME = ['11']

# Rate for checking, 30 seconds to 1 min is recommended, in registeration day it's okay to go higher :V
RATE = 30


if not exists('./private.py'):
    firstTimer()

try:
    from private import *
except ImportError:
    print("Remember adding your email and password in a file named private")
    pass


def sendEmail():
    sent_from = gmail_user
    to = [personal_mail]
    subject = 'THERE IS A SPOT IN ' + TITLE.capitalize() + '!'
    body = "Hurry up and register! For any inquiries contact me at eltokhy@aucegypt.edu"
    email_text = """\
    %s
    \n\n
    %s
    """ % (subject, body)

    try: 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.connect('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print("Email Sent!")
    except Exception as e:
        print('Error sending the email')
        
def doIt():
    cj = http.cookiejar.CookieJar()
    br = mechanize.Browser()
    br.set_cookiejar(cj)
    br.open("https://ssb-prod.ec.aucegypt.edu/PROD/bwckschd.p_disp_dyn_sched")
    br.select_form(nr=0)
    br.form['p_term'] = SEMS
    br.submit()
    br.select_form(nr=0)
    sel_subj = br.find_control("sel_subj",type="select", nr=0).get(DEPT)
    sel_subj.selected = True
    br.form['sel_title'] = TITLE
    if TIMEQUER:
        br.form['begin_hh'] = TIME
    #for f in br.forms():
    #   print(f)
    br.submit()
    #print(br.response().read())
    response = br.response().read()
    currentHash = hashlib.sha224(response).hexdigest()
    return currentHash

# get an initial hash for the first state
currentHash = doIt()

print("LAUNCHED SUCCESSFULLY")
print('8',end='')

while True:
    try:
    
        # create a new hash
        newHash = doIt()
    
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            print('=',end='',flush=True)
            time.sleep(RATE)
            continue
         
        # if something changed in the hashes
        else:
            # notify
            print(">\nsomething changed\n8",end='')
            currentHash = newHash

            # Using notify-send utility to send myself a notification
            cmd = 'notify-send "A change happened in ' + str(TITLE) + ' HURRY!" -t 20000'

            # If you want to recieve updates by email uncomment next line
            # sendEmail()
            os.system(cmd)
            time.sleep(RATE*5)
            continue

    except Exception as e:
        print("Error in scraping the website")
