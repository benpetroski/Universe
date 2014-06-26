'''
@author: benpetroski

Produces: Click in window closes GUI, will show which keyboard character is pushed in statusbar.
http://zetcode.com/gui/pyqt4/eventsandsignals/
'''
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QMainWindow):
    closeApp = QtCore.pyqtSignal()
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.closeApp.connect(self.close)
        
        self.statusBar()
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event Sender')
        self.show()        
        
    def mousePressEvent(self,e):
        self.closeApp.emit()
    def keyPressEvent(self,e):
        print chr(e.key())
        if e.key() != QtCore.Qt.Key_Escape:
            self.statusBar().showMessage(chr(e.key()))
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    