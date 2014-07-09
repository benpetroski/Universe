'''
@author: benpetroski

Produces: Draw different line styles using a loop and list.
http://zetcode.com/gui/pyqt4/drawing/
'''
import sys, random
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,280,270)
        self.setWindowTitle('Draw Different Line Styles')
        self.show()                
        
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self) 
        self.drawLines(qp)
        qp.end()
        
    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        lineStyles = [QtCore.Qt.SolidLine, QtCore.Qt.DashLine, QtCore.Qt.DashDotLine, QtCore.Qt.DotLine, QtCore.Qt.DashDotDotLine, QtCore.Qt.CustomDashLine]
        xPos = 20
        yPos = 40
        xSiz = 250
        ySiz = 40
        
        for line in lineStyles:   
            if line == QtCore.Qt.CustomDashLine:
                pen.setDashPattern([1, 4, 5, 4])  
            pen.setStyle(line)
            qp.setPen(pen)
            qp.drawLine(xPos,yPos,xSiz,ySiz)
            yPos+=40
            ySiz+=40
                        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    