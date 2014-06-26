'''
@author: benpetroski

Produces: GUI with button, button click produces dialog that will take input and set GUI editor to that input.
http://zetcode.com/gui/pyqt4/dialogs/
'''
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20,20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130,22)

        self.setGeometry(300,300,290,150)
        self.setWindowTitle('Input Dialog')
        self.show()        
        
    def showDialog(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    