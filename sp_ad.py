
import threading
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QGraphicsScene
from job_list import job
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QIcon, QPixmap, QImage

class Ranking(QWidget):
    def __init__(self, parent=None):
        super(Ranking, self).__init__(parent)
        self.aa = QLabel()
        lay = QGridLayout()
        self.setLayout(lay)


class SutdaGame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.user_info = []



        self.get_paeButton = QToolButton()
        self.get_paeButton.setText("패 받기")
        self.get_paeButton.clicked.connect(self.Get_card)

        left_Layout = QGridLayout()
        left_Layout.addWidget(self.get_paeButton,1,0)
        self.computer_pae = QLabel(self)
        pixma = QPixmap('2.png')
        self.computer_pae.setPixmap(pixma)
        left_Layout.addWidget(self.computer_pae,0,0)
        
        self.user_pae = QLabel(self)
        pixmap = QPixmap('1.png')
        self.user_pae.setPixmap(pixmap)
        left_Layout.addWidget(self.user_pae,2,0)





        #left_money
        self.left_money = QLineEdit()
        self.left_money.setReadOnly(True)
        self.left_money.setAlignment(Qt.AlignRight)
        self.lefted_money = 500
        self.left_money.setText(str(self.lefted_money))

        self.name_edit = QLineEdit()
        self.name_edit.setAlignment(Qt.AlignRight)


        centerLayout = QGridLayout()
        centerLayout.addWidget(self.left_money, 0,0,5,5)
        centerLayout.addWidget(self.name_edit, 1,0,5,5)

        self.btn_Betting = QToolButton()
        self.btn_Betting.setText("BETTING")

        self.btn_Betting = QToolButton()
        self.btn_Betting.setText("BETTING")
        #self.start_btn.clicked.connect()

        self.btn_Die = QToolButton()
        self.btn_Die.setText("DIE")
        #self.btn_Die.clicked.connect()

        self.btn_Save = QToolButton()
        self.btn_Save.setText("SAVE")
        self.btn_Save.clicked.connect(self.save)

        self.btn_Login = QToolButton()
        self.btn_Login.setText("Login")
        self.btn_Login.clicked.connect(self.start_game)

        self.btn_Ranking = QToolButton()
        self.btn_Ranking.setText("rank")
        self.btn_Ranking.clicked.connect(self.ranking)

        right_laydout = QGridLayout()
        right_laydout.addWidget(self.btn_Betting, 0, 0)
        right_laydout.addWidget(self.btn_Die, 1, 0)
        right_laydout.addWidget(self.btn_Save, 2, 0)
        right_laydout.addWidget(self.btn_Login, 3, 0)
        right_laydout.addWidget(self.btn_Ranking, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        self.setWindowTitle("Sutda")
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(left_Layout,0,0)
        mainLayout.addLayout(centerLayout, 0, 1)
        mainLayout.addLayout(right_laydout,0,2)
        self.setLayout(mainLayout)
    def Get_card(self):
        pass

    def start_game(self):
        self.name_edit.setReadOnly(True)


    def save(self):
        f = open('user_info.txt', 'r')
        lines = f.readlines()
        f.close()
        self.count = 0
        for line in lines:
            information = line.rstrip()
            self.user_info.append(information)
        self.user_info.append(self.left_money.text() + " " +self.name_edit.text())
        f = open('user_info.txt', 'w')

        for info in self.user_info:
            f.write(info + "\n")






    def ranking(self):
        rank = Ranking(self)
        rank.show()

        # 타임아웃 이벤트가 발생하면 호출되는 메서드
        # 어떤 타이머에 의해서 호출되었는지 확인




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = SutdaGame()
    game.show()
    sys.exit(app.exec_())

