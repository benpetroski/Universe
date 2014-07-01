'''
@author: benpetroski

Produces: Optimized widget for showing images on the window (?).
http://zetcode.com/gui/pyqt4/widgets2/
'''
import sys
from PyQt4 import QtGui,QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap('pic.png')
        
        lbl = QtGui.QLabel(self)
        lbl.setPixmap(pixmap)
        
        hbox.addWidget(lbl)
        self.setLayout(hbox)
                
        self.setGeometry(300,300,350,300)
        self.setWindowTitle('pic')
        self.show()        
                
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    