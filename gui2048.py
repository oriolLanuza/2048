import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('2048 - The Game!')
        self.setFixedSize(150, 200)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.createLayoutBase()

    def createLayoutBase(self):
        scoreLayout = QGridLayout()
        scoreLayout.addWidget(QLabel('Score:'),0,0)
        scoreLayout.addWidget(QLabel('0'),0,1)
        scoreLayout.addWidget(QLabel('Moves:'),0,3)
        scoreLayout.addWidget(QLabel('0'),0,4)
        controlLayout = QGridLayout()
        controlLayout.addWidget(QPushButton('Up'),0,1)
        controlLayout.addWidget(QPushButton('Down'),1,1)
        controlLayout.addWidget(QPushButton('Left'),1,0)
        controlLayout.addWidget(QPushButton('Right'),1,2)
        mainLayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(QPushButton('Up'))
        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(QPushButton('Left'))
        hlayout2.addWidget(QPushButton('Down'))
        hlayout2.addWidget(QPushButton('Right'))
        boardLayout = QGridLayout()
        boardLayout.addWidget(QLabel('0'),0,0)
        boardLayout.addWidget(QLabel('0'),0,1)
        boardLayout.addWidget(QLabel('0'),0,2)
        boardLayout.addWidget(QLabel('0'),0,3)
        boardLayout.addWidget(QLabel('0'),1,0)
        boardLayout.addWidget(QLabel('0'),1,1)
        boardLayout.addWidget(QLabel('0'),1,2)
        boardLayout.addWidget(QLabel('0'),1,3)
        boardLayout.addWidget(QLabel('0'),2,0)
        boardLayout.addWidget(QLabel('0'),2,1)
        boardLayout.addWidget(QLabel('0'),2,2)
        boardLayout.addWidget(QLabel('0'),2,3)
        boardLayout.addWidget(QLabel('0'),3,0)
        boardLayout.addWidget(QLabel('0'),3,1)
        boardLayout.addWidget(QLabel('0'),3,2)
        boardLayout.addWidget(QLabel('0'),3,3)
        mainLayout.addLayout(scoreLayout)
        mainLayout.addLayout(boardLayout)
        mainLayout.addLayout(controlLayout)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(mainLayout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())