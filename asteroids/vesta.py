'''
@author: bpetroski
'''
import smtplib, sys
from PyQt4 import QtCore, QtGui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class sendMessage(object):
    me=''
    you=''
    msg=''
    html=''
    s=None
    
    def __init__(self, pw):
        self.me = "@gmail.com"
        self.you = "@vtext.com"
        self.html = 'Hello Dave.'
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = ""
        self.msg['From'] = self.me
        self.msg['To'] = self.you 
        self.s = smtplib.SMTP('smtp.gmail.com:587')
        self.s.starttls()        
        self.s.login(self.me.replace('@gmail.com',''),pw)
    
    def message(self, string):
        # htmlHead = """\<html><head></head><body>"""
        # htmlTail = """\</body></html>"""
        self.html = string
    
    def send(self):
        self.msg.attach(MIMEText(self.html, 'html') )
        self.s.sendmail(self.me, self.you, self.msg.as_string())
        
    def close(self):
        self.s.quit()

class createGUI(QtGui.QWidget):
    def __init__(self):
        super(createGUI,self).__init__()
        self.initUI()
        
    def initUI(self):
        print 'Enter email password: '
        self.pw = str(raw_input())
        sendButton = QtGui.QPushButton('Send', self)
        sendButton.move(20,20)
        sendButton.clicked.connect(self.send)
        
        self.setWindowTitle('Send text message')
        self.setGeometry(100,100,100,100)
        self.show()
        
    def send(self):
        sm = sendMessage(self.pw)
        sm.send()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = createGUI()
    sys.exit(app.exec_())