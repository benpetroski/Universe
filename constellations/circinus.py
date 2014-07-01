'''
@author: benpetroski

Produces: Using a checkbox widget to change the window title.
http://zetcode.com/gui/pyqt4/widgets/
'''
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        cb = QtGui.QCheckBox('Hide title', self)
        cb.move(20,20)
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QtGui.QCheckBox')
        self.show()        
        
    def changeTitle(self, state):
        if state!=QtCore.Qt.Checked:
            self.setWindowTitle('QtGui.QCheckBox')
        else:
            self.setWindowTitle('')
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    