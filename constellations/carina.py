'''
@author: benpetroski

Produces: Making two buttons that send a signal to the statusbar when pushed.
http://zetcode.com/gui/pyqt4/eventsandsignals/
'''
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        widg = QtGui.QWidget()
        vbox = QtGui.QVBoxLayout()
        
        btn1 = QtGui.QPushButton('Button 1', self)
        vbox.addWidget(btn1)
        
        btn2 = QtGui.QPushButton('Button 2', self)
        vbox.addWidget(btn2)
        
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        
        widg.setLayout(vbox)
        self.setCentralWidget(widg)        
        self.statusBar()
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event Sender')
        self.show()        
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+' was pressed!')
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    