'''
@author: benpetroski

Produces: Box containing statusbar message.
http://zetcode.com/gui/pyqt4/menusandtoolbars/
'''
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):        
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Statusbar')        
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()