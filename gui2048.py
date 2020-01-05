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
        self.createLayoutBase()

    def createLayoutBase(self):
        vlayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(QPushButton('Up'))
        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(QPushButton('Left'))
        hlayout2.addWidget(QPushButton('Down'))
        hlayout2.addWidget(QPushButton('Right'))
        board = QGridLayout()
        board.addWidget(QLabel('0'),0,0)
        board.addWidget(QLabel('0'),0,1)
        board.addWidget(QLabel('0'),0,2)
        board.addWidget(QLabel('0'),0,3)
        board.addWidget(QLabel('0'),1,0)
        board.addWidget(QLabel('0'),1,1)
        board.addWidget(QLabel('0'),1,2)
        board.addWidget(QLabel('0'),1,3)
        board.addWidget(QLabel('0'),2,0)
        board.addWidget(QLabel('0'),2,1)
        board.addWidget(QLabel('0'),2,2)
        board.addWidget(QLabel('0'),2,3)
        board.addWidget(QLabel('0'),3,0)
        board.addWidget(QLabel('0'),3,1)
        board.addWidget(QLabel('0'),3,2)
        board.addWidget(QLabel('0'),3,3)
        vlayout.addLayout(board)
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)
        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(vlayout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())