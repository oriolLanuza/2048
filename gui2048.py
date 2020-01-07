import sys
import pickle

from game2048 import Game

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('2048 - The Game!')
        self.setFixedSize(150, 200)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.scoreLabel = QLabel('0')
        self.turnLabel = QLabel('0')
        self.board00 = QLabel('0')
        self.board01 = QLabel('0')
        self.board02 = QLabel('0')
        self.board03 = QLabel('0')
        self.board10 = QLabel('0')
        self.board11 = QLabel('0')
        self.board12 = QLabel('0')
        self.board13 = QLabel('0')
        self.board20 = QLabel('0')
        self.board21 = QLabel('0')
        self.board22 = QLabel('0')
        self.board23 = QLabel('0')
        self.board30 = QLabel('0')
        self.board31 = QLabel('0')
        self.board32 = QLabel('0')
        self.board33 = QLabel('0')
        self.createLayoutBase()

    def createLayoutBase(self):
        scoreLayout = QGridLayout()
        scoreLayout.addWidget(QLabel('Score:'),0,0)
        scoreLayout.addWidget(self.scoreLabel,0,1)
        scoreLayout.addWidget(QLabel('Turn:'),0,3)
        scoreLayout.addWidget(self.turnLabel,0,4)
        controlLayout = QGridLayout()
        btnNew = QPushButton('New')
        btnNew.clicked.connect(new_game)
        btnUp = QPushButton('Up')
        btnUp.clicked.connect(move_up)
        btnSave = QPushButton('Save')
        btnSave.clicked.connect(save_game)
        btnDown = QPushButton('Down')
        btnDown.clicked.connect(move_down)
        btnLeft = QPushButton('Left')
        btnLeft.clicked.connect(move_left)
        btnRight = QPushButton('Right')
        btnRight.clicked.connect(move_right)
        controlLayout.addWidget(btnNew,0,0)
        controlLayout.addWidget(btnUp,0,1)
        controlLayout.addWidget(btnSave,0,2)
        controlLayout.addWidget(btnDown,1,1)
        controlLayout.addWidget(btnLeft,1,0)
        controlLayout.addWidget(btnRight,1,2)
        mainLayout = QVBoxLayout()
        hlayout1 = QHBoxLayout()
        hlayout1.addWidget(QPushButton('Up'))
        hlayout2 = QHBoxLayout()
        hlayout2.addWidget(QPushButton('Left'))
        hlayout2.addWidget(QPushButton('Down'))
        hlayout2.addWidget(QPushButton('Right'))
        boardLayout = QGridLayout()
        boardLayout.addWidget(self.board00,0,0)
        boardLayout.addWidget(self.board01,0,1)
        boardLayout.addWidget(self.board02,0,2)
        boardLayout.addWidget(self.board03,0,3)
        boardLayout.addWidget(self.board10,1,0)
        boardLayout.addWidget(self.board11,1,1)
        boardLayout.addWidget(self.board12,1,2)
        boardLayout.addWidget(self.board13,1,3)
        boardLayout.addWidget(self.board20,2,0)
        boardLayout.addWidget(self.board21,2,1)
        boardLayout.addWidget(self.board22,2,2)
        boardLayout.addWidget(self.board23,2,3)
        boardLayout.addWidget(self.board30,3,0)
        boardLayout.addWidget(self.board31,3,1)
        boardLayout.addWidget(self.board32,3,2)
        boardLayout.addWidget(self.board33,3,3)
        mainLayout.addLayout(scoreLayout)
        mainLayout.addLayout(boardLayout)
        mainLayout.addLayout(controlLayout)
        self.centralWidget.setLayout(mainLayout)
        
def new_game():
    game.new_game()
    updateLayout()

def save_game():
    game.save_game()

def move_up():
    game.move_up_algorithm()
    updateLayout()

def move_down():
    game.move_down_algorithm()
    updateLayout()

def move_left():
    game.move_left_algorithm()
    updateLayout()

def move_right():
    game.move_right_algorithm()
    updateLayout()

def updateLayout():
    updateScoreLayout()
    updateBoardLayout()

def updateScoreLayout():
    win.scoreLabel.setText(str(game.score))
    win.turnLabel.setText(str(game.turn))

def updateBoardLayout():
    win.board00.setText(str(game.board[0]))
    win.board01.setText(str(game.board[1]))
    win.board02.setText(str(game.board[2]))
    win.board03.setText(str(game.board[3]))
    win.board10.setText(str(game.board[4]))
    win.board11.setText(str(game.board[5]))
    win.board12.setText(str(game.board[6]))
    win.board13.setText(str(game.board[7]))
    win.board20.setText(str(game.board[8]))
    win.board21.setText(str(game.board[9]))
    win.board22.setText(str(game.board[10]))
    win.board23.setText(str(game.board[11]))
    win.board30.setText(str(game.board[12]))
    win.board31.setText(str(game.board[13]))
    win.board32.setText(str(game.board[14]))
    win.board33.setText(str(game.board[15]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    game = Game()
    try:
        game.resume_game()
    except:
        pass
    updateLayout()
    win.show()
    sys.exit(app.exec_())