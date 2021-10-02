from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('ScoreKeeper.ui', self)

        #define the widgets
        self.score1_label = self.findChild(QLabel, 'score1_label')
        self.score2_label = self.findChild(QLabel, 'score2_label')
        self.delete5_team1_pushButton = self.findChild(QPushButton, 'delete5_team1_pushButton')
        self.add10_team1_pushButton = self.findChild(QPushButton, 'add10_team1_pushButton')
        self.delete5_team2_pushButton = self.findChild(QPushButton, 'delete5_team2_pushButton')
        self.add10_team2_pushButton = self.findChild(QPushButton, 'add10_team2_pushButton')
        self.clear_score_pushButton = self.findChild(QPushButton, 'clear_score_pushButton')
        self.clear_all_pushButton = self.findChild(QPushButton, 'clear_all_pushButton')

        self.score_team_1 = 0
        self.score_team_2 = 0
        self.show()

        self.delete5_team1_pushButton.clicked.connect(self.delete5_t1)
        self.delete5_team2_pushButton.clicked.connect(self.delete5_t2)
        self.add10_team1_pushButton.clicked.connect(self.add10_t1)
        self.add10_team2_pushButton.clicked.connect(self.add10_t2)
        self.clear_all_pushButton.clicked.connect(self.clear_all)
        self.clear_score_pushButton.clicked.connect(self.clear_score)

    def add10_t1(self):
        self.score_team_1 += 10
        self.score1_label.setText(str(self.score_team_1))
    def delete5_t1(self):
        self.score_team_1 += -5
        self.score1_label.setText(str(self.score_team_1))
    def add10_t2(self):
        self.score_team_2 += 10
        self.score2_label.setText(str(self.score_team_2))
    def delete5_t2(self):
        self.score_team_2 += -5
        self.score2_label.setText(str(self.score_team_2))
    def clear_all(self):
        self.score1_label.setText('0')
        self.score2_label.setText('0')
        self.score_team_2 = 0
        self.score_team_1 = 0
    def clear_score(self):
        self.score1_label.setText('0')
        self.score2_label.setText('0')
        self.score_team_2 = 0
        self.score_team_1 = 0


# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()