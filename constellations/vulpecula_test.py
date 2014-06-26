'''
@author: bpetroski
'''
import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        # title of the window
        self.setWindowTitle('Segmentation Accuracy')
        # fix window size
        self.setFixedSize(400,200)
        # status bar with initial message
        self.statusBar().showMessage('ready')
        
        
        # Layout
        # contiene gli altri widget
        cWidget = QtGui.QWidget(self)
        grid = QtGui.QGridLayout(cWidget)
        
        # Box Left
        vBox_left = QtGui.QVBoxLayout()
        vBox_left.setSpacing(2) #set spacing
        
        Button_input1 = QtGui.QPushButton("Reference Polygons")
        vBox_left.addWidget(Button_input1)
        
        Button_input2 = QtGui.QPushButton("Segmented Polygons")
        vBox_left.addWidget(Button_input2)
        
        Button_output = QtGui.QPushButton("Save")
        vBox_left.addWidget(Button_output)
        
        Button_start = QtGui.QPushButton("Start")
        Button_start.setCheckable(True)
        
        # vBox_left.addWidget(Button_input1)
        # vBox_left.addWidget(Button_input2)
        # vBox_left.addWidget(Button_output)
        vBox_left.addWidget(Button_start)
        
        # Box right
        vBox_right = QtGui.QVBoxLayout()
        vBox_right.setSpacing(10) #set spacing
        
        ke = QtGui.QRadioButton("", cWidget)
        pu = QtGui.QRadioButton("", cWidget)
        clinton = QtGui.QRadioButton("", cWidget)
        ke.setChecked(True)
        
        ke_label = QtGui.QLabel("Ke <i>et al</i>.", cWidget)
        pu_label = QtGui.QLabel("Pu et al.", cWidget)
        clinton_label = QtGui.QLabel("Clinton et al.", cWidget)
        
        grid_right = QtGui.QGridLayout()
        
        grid_right.addWidget(ke, 0, 0)
        grid_right.addWidget(pu, 1, 0)
        grid_right.addWidget(clinton, 2, 0)
        grid_right.addWidget(ke_label, 0, 1)
        grid_right.addWidget(pu_label, 1, 1)
        grid_right.addWidget(clinton_label, 2, 1)
        grid.addLayout(grid_right, 0, 1)
        
        grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1, 1)
        grid_right.setColumnStretch(1, 1)
        
        ke.setStatusTip("Ke et al., 2010. Remote Sensing of Environment, 114, pp. 1141-1154")
        pu.setStatusTip("Pu et al., 2012. Remote Sensing of Environment, 124, pp. 516-533")
        clinton.setStatusTip("Clinton et al., 2012. Remote Sensing of Environment, 124, pp. 516-533")
        
        
        ke_label.setStatusTip("Ke et al., 2010. Remote Sensing of Environment, 114, pp. 1141-1154")
        pu_label.setStatusTip("Pu et al., 2012. Remote Sensing of Environment, 124, pp. 516-533")
        clinton_label.setStatusTip("Clinton et al., 2012. Remote Sensing of Environment, 124, pp. 516-533")
        
        # grid.addWidget(Button_input1, 0, 0)
        # grid.addWidget(Button_input2, 1, 0)
        # grid.addWidget(Button_output, 2, 0)
        # grid.addWidget(Button_start, 3, 0)
        grid.addLayout(vBox_left, 0, 0)
        #grid.addLayout(vBox_right, 0, 1)
        
        
        # cWidget.setLayout(grid)
        self.setCentralWidget(cWidget)
        
def main():
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
        
if __name__ == '__main__':
    main()