'''
@author: bpetroski
'''
import smtplib, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "benjaminpetroski@gmail.com" # me == my email address
you = "3153081639@vtext.com" # you == recipient's email address
msg = MIMEMultipart('alternative')
msg['Subject'] = ""
msg['From'] = me
msg['To'] = you

# htmlHead = """\<html><head></head><body>"""
# htmlTail = """\</body></html>"""
html = "We hope we have expanded your vocabulary today! :)" #htmlHead + words + htmlTail# 
part = MIMEText(html, 'html') 
msg.attach(part)
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
print 'Enter your password'
pw=getpass.getpass()
s.login('benjaminpetroski', pw)
s.sendmail(me, you, msg.as_string())
s.quit()