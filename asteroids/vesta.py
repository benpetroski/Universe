'''
@author: bpetroski
'''
import smtplib, sys
from PyQt4 import QtCore, QtGui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class sendMessage(object):    
    def __init__(self, pw, msgcarrier, msgto, msgfrom, msgmessage):
        self.you = str(msgto+msgcarrier)
        self.me = msgfrom       
        self.html = msgmessage
        self.msg = MIMEMultipart('alternative')
        self.msg['Subject'] = ''
        self.msg['From'] = self.me
        self.msg['To'] = self.you 
        self.s = smtplib.SMTP('smtp.gmail.com:587')
        self.s.starttls()        
        self.s.login(self.me.replace('@gmail.com',''),pw)
        
    def send(self):
        self.msg.attach(MIMEText(str(self.html), 'plain'))        
        self.s.sendmail(self.me, self.you, self.msg.as_string())
        
    def close(self):
        self.s.quit()

class createGUI(QtGui.QWidget):
    msgcarrier='@vtext.com'
    msgto=''
    msgfrom='@gmail.com'
    msgmessage='Hello World!!'
    
    def __init__(self):
        super(createGUI,self).__init__()
        self.initUI()
        
    def initUI(self):        
        hboxCarrier = QtGui.QHBoxLayout()
        hboxTo = QtGui.QHBoxLayout()
        hboxFrom = QtGui.QHBoxLayout()
        hboxMessage = QtGui.QHBoxLayout()
        hboxSend = QtGui.QHBoxLayout()        
        vbox = QtGui.QVBoxLayout()
        
        labelCarrier = QtGui.QLabel('Carrier:', self)
        editCarrier = QtGui.QComboBox(self)
        editCarrier.addItem('Verizon')
        editCarrier.addItem('AT&T')
        editCarrier.addItem('T-Mobile')
        editCarrier.addItem('Sprint')
        editCarrier.setCurrentIndex(0)
        editCarrier.activated[str].connect(self.setCarrier)
        hboxCarrier.addWidget(labelCarrier)
        hboxCarrier.addWidget(editCarrier)
        vbox.addLayout(hboxCarrier)
        
        labelTo = QtGui.QLabel('To:', self)
        editTo = QtGui.QLineEdit(self)
        editTo.setText(self.msgto)
        editTo.textChanged[str].connect(self.setTo)
        hboxTo.addWidget(labelTo)
        hboxTo.addWidget(editTo)
        vbox.addLayout(hboxTo)
        
        labelFrom = QtGui.QLabel('From:', self)
        editFrom = QtGui.QLineEdit(self)
        editFrom.setText(self.msgfrom)
        editFrom.textChanged[str].connect(self.setFrom)
        hboxFrom.addWidget(labelFrom)
        hboxFrom.addWidget(editFrom)
        vbox.addLayout(hboxFrom)
        
        labelMessage = QtGui.QLabel('Message:', self)
        self.editMessage = QtGui.QTextEdit(self)
        self.editMessage.setText(self.msgmessage)
        self.editMessage.textChanged.connect(self.setMessage)
        hboxMessage.addWidget(labelMessage)
        hboxMessage.addWidget(self.editMessage)
        vbox.addLayout(hboxMessage)
        vbox.addSpacing(5)      
        
        self.pw = '' 
        sendButton = QtGui.QPushButton('Send', self)
        sendButton.clicked.connect(self.send)
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.cancel)
        hboxSend.addWidget(sendButton)
        hboxSend.addWidget(cancelButton)
        vbox.addLayout(hboxSend)

        self.setLayout(vbox)
        self.setWindowTitle('Send message')
        self.setGeometry(1000,500,230,200)
        self.show()
        
    def setCarrier(self, text):
        if text=='Verizon':
            self.msgcarrier='@vtext.com'
        elif text=='AT&T':
            self.msgcarrier='@txt.att.net'
        elif text=='T-Mobile':
            self.msgcarrier='@tmomail.net'
        elif text=='Sprint':
            self.msgcarrier='@pm.sprint.com'
        else:
            print 'Error: carrier'
        
    def setTo(self, text):
        self.msgto=text
        
    def setFrom(self, text):
        self.msgfrom=text+'@gmail.com'
        
    def setMessage(self):
        self.msgmessage=self.editMessage.toPlainText()
        
    def send(self):
        sm = sendMessage(self.pw, self.msgcarrier, self.msgto, self.msgfrom, self.msgmessage)
        sm.send()
        
    def cancel(self):
        sys.exit()
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = createGUI()
    sys.exit(app.exec_())