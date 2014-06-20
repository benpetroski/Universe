'''
Created on Jun 16, 2014

@author: Ben Petroski

Produces: Box with set size, position, and title.
http://zetcode.com/gui/pyqt4/firstprograms/
'''
import sys
from PyQt4 import QtCore, QtGui
 
def main():
    app = QtGui.QApplication(sys.argv)
     
    w = QtGui.QWidget()
    w.resize(250,150)
    w.move(300,300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()