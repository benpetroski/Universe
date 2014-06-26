'''
@author: benpetroski

Produces: Reimplementation of event handler.
http://zetcode.com/gui/pyqt4/eventsandsignals/
'''
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event Handler')
        self.show()        
        
    def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    