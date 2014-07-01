'''
@author: bpetroski
'''
import smtplib, sys
from PyQt4 import QtCore, QtGui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class sendMessage(object):    
    def __init__(self, pw, msgto, msgfrom, msgmessage):
        self.you = msgto
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
        self.msg.attach(MIMEText(self.html, 'plain'))
        self.s.sendmail(self.me, self.you, self.msg.as_string())
        
    def close(self):
        self.s.quit()

class createGUI(QtGui.QWidget):
    msgcarrier='Verizon'
    msgto='[fillinnumber]@vtext.com'
    msgfrom='[fillinemail]@gmail.com'
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
        
        self.pw = '[fillinemailpass]' 
        sendButton = QtGui.QPushButton('Send', self)
        sendButton.clicked.connect(self.send)
        cancelButton = QtGui.QPushButton('Cancel', self)
        cancelButton.clicked.connect(self.cancel)
        hboxSend.addWidget(sendButton)
        hboxSend.addWidget(cancelButton)
        vbox.addLayout(hboxSend)

        self.setLayout(vbox)
        self.setWindowTitle('Send message')
        self.setGeometry(1000,500,300,200)
        self.show()
        
    def setCarrier(self, text):
        if text=='Verizon':
            self.msgcarrier='@vtext.com'
            print self.msgcarrier
        elif text=='AT&T':
            self.msgcarrier='@txt.att.net'
            print self.msgcarrier
        elif text=='T-Mobile':
            self.msgcarrier='@tmomail.net'
            print self.msgcarrier
        elif text=='Sprint':
            self.msgcarrier='@pm.sprint.com'
            print self.msgcarrier
        else:
            print 'Error: carrier'
        
    def setTo(self, text):
        self.msgto=text+self.msgcarrier
        print self.msgto
        
    def setFrom(self, text):
        self.msgfrom=text+'@gmail.com'
        print self.msgfrom
        
    def setMessage(self):
        self.msgmessage=self.editMessage.toPlainText()
        print self.msgmessage
        
    def send(self):
        sm = sendMessage(self.pw, self.msgto, self.msgfrom, self.msgmessage)
        sm.send()
        
    def cancel(self):
        sys.exit(app.exec_())
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    c = createGUI()
    sys.exit(app.exec_())