from PyQt4.QtGui import *
import sys

# MyDiag.py 모듈 import
# import MyDiag

import show


# MyDiag 모듈 안의 Ui_MyDialog 클래스로부터 파생
class XDialog(QMainWindow, show.Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        # setupUi() 메서드는 화면에 다이얼로그 보여줌

        # 윈도우 화면에 표시
        self.show()


app = QApplication(sys.argv)
dlg = XDialog()
sys.exit(app.exec_())