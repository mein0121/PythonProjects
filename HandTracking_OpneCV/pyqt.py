import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import AutopyClass
p = ['a','b','c','d','e']


class MyApp(QWidget):



    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)	# 푸시버튼 생성, 'Alt+b' 단축키 생성
        btn1.setCheckable(True)	# 누른 상태와 아닌 상태 구분
        btn1.toggle()	# 상태 변경, 프로그램이 시작될 때 선택되어 있음

        btn2 = QPushButton(self)
        btn2.setText('Button&2')	# 'Alt+2' 단축키 생성

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(True)	# 버튼을 사용할 수 없음
        btn3.clicked.connect(self.button_clicked)



        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def button_clicked(self):
        AutopyClass.enterCommand(p)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())