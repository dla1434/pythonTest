
from PyQt4.QtGui import *

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        lblName = QLabel("Name")
        editName = QLineEdit()
        btnOk = QPushButton("OK")

        layout = QVBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(editName)
        layout.addWidget(btnOk)

        self.setLayout(layout)

app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()
