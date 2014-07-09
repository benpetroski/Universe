'''
@author: benpetroski

Produces: Draw different brush styles using a loop and list.
http://zetcode.com/gui/pyqt4/drawing/
'''
import sys, random
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,355,280)
        self.setWindowTitle('Draw with Brushes')
        self.show()                
        
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self) 
        self.drawBrushes(qp)
        qp.end()
        
    def drawBrushes(self, qp):
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        brushStyles = [QtCore.Qt.SolidPattern, QtCore.Qt.Dense1Pattern, QtCore.Qt.Dense2Pattern, QtCore.Qt.DiagCrossPattern, QtCore.Qt.Dense5Pattern, QtCore.Qt.Dense6Pattern, QtCore.Qt.HorPattern, QtCore.Qt.VerPattern, QtCore.Qt.BDiagPattern]
        xP = 10
        yP = 15
        xS = 90
        yS = 60
        
        for b in brushStyles:
            if xP > 250:
                xP = 10
                yP += 90
            brush.setStyle(b)
            qp.setBrush(b)
            qp.drawRect(xP, yP, xS, yS)
            xP += 120
                        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    
    
if __name__ == '__main__':
    main()
    