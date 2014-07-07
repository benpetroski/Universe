'''
@author: benpetroski

Produces: Drag button around in GUI with right-mouse click.
http://zetcode.com/gui/pyqt4/dragdrop/
'''
import sys
from PyQt4 import QtGui,QtCore

class Button(QtGui.QPushButton):
    
    def __init__(self, title, parent):
        super(Button,self).__init__(title,parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != QtCore.Qt.RightButton:
            return
        
        mimeData = QtCore.QMimeData()
        
        drag = QtGui.QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        
        dropAction = drag.start(QtCore.Qt.MoveAction)
        
    def mousePressEvent(self, e):
        super(Button, self).mousePressEvent(e)
        
        if e.button() == QtCore.Qt.LeftButton:
            print 'press'

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setAcceptDrops(True)
                
        self.button=Button('Button', self)
        self.button.move(100,65)
                
        self.setGeometry(300,300,280,150)
        self.setWindowTitle('Click or Move')
        self.show()                
        
    def dragEnterEvent(self, e):
        e.accept()
    
    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        
        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
                        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    