import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")
        #self.setWindowIcon(QIcon('icon.png'))

        self.lineEdit1 = QLineEdit()
        self.pushButton = QPushButton("Drawing Chart")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        fig = plt.Figure()
        canvas = FigureCanvas(fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(canvas)

        #Right Layout
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.lineEdit1)
        rightLayout.addWidget(self.pushButton)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        print(self.lineEdit1.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()