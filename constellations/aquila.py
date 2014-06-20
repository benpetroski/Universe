'''
@author: benpetroski

Produces: Box that has confirmation pop-up message upon exit.
'''
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Message Box')        
        self.show()
        
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', 'Are you sure you want to quit?', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()