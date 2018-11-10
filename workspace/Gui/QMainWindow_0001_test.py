
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("MyWindow")
        self.setGeometry(600, 600, 400, 400)
        self.setWindowIcon(QIcon('umbrella.png'))
        self.statusBar().showMessage('준비')

        btn1 = QPushButton('메시지 버튼', self)
        btn1.setToolTip('이 버튼을 누르면 <b>메시지 박스</b>가 나옴')
        btn1.resize(btn1.sizeHint())
        btn1.move(50, 50)
        btn1.clicked.connect(self.btnClicked)

        btnQuit = QPushButton('종료', self)
        btnQuit.move(50, 100)
        btnQuit.clicked.connect(QCoreApplication.instance().quit)

        self.show()

    def btnClicked(self):
        QMessageBox.information(self, "버튼1", "버튼 클릭!")


app = QApplication([])
ex = MyWindow()
app.exec_()