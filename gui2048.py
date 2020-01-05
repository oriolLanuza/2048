""" # Filename: main_window.py



import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QGridLayout

class Window(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.setWindowTitle('2048 - The Game!')
        self._createBoard()
        #self._createMovementBtns()
        #self.setCentralWidget(QLabel("I'm the Central Widget"))
        #self._createMenu()
        #self._createToolBar()
        #self._createStatusBar()

    def _createBoard(self):
        board = QGridLayout()
        board.addWidget(QLabel('0ydrtftyu'),0,0)
        board.addWidget(QLabel('0fyui'),0,1)
        board.addWidget(QLabel('0ryuiyrui'),0,2)
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
        self.setLayout(board)

    def _createMenu(self):
        self.menu = self.menuBar().addMenu("&Menu")
        self.menu.addAction('&Exit', self.close)

    def _createToolBar(self):
        tools = QToolBar()
        self.addToolBar(tools)
        tools.addAction('Exit', self.close)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
 """
# Filename: g_layout.py

"""Grid layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('2048 - The Game!')
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
window.setLayout(vlayout)
window.show()
sys.exit(app.exec_())