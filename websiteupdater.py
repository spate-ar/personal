# Python code to illustrate Sending mail to multiple users from your Gmail account when a website changes 
import smtplib
import time
import requests
from bs4 import BeautifulSoup

  
# list of email_id to send the mail
li = ["xxxxx@gmail.com", "yyyyy@gmail.com"] #addresses redacted
change=False

URL = "https://www.brindleybeach.com/outer-banks-vacation-rentals/126-newmania"
r = requests.get(URL)
htmlcontent=r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
initsoup=soup.prettify

while True:
    r= requests.get(URL)
    htmlcontent= r.content
    soup= BeautifulSoup(htmlcontent, 'html.parser')
    if ((soup != initsoup) and (change==True)):
        print ("Changed")
        for dest in li:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login("wwwww@gmail.com", "password") #info Redacted
            message = "Change in the house, check www.brindleybeach.com/outer-banks-vacation-rentals/126-newmania"
            s.sendmail("wwwww@gmail.com", dest, message) #info redacted
            s.quit()
        initsoup=soup
    print ("loop")
    change=True
    time.sleep(30)
