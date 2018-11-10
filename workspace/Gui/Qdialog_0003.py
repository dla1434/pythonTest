
from PyQt4.QtGui import *

class MyDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # lblName = QLabel("Name")

        lblName = QLabel()
        # lblName.setText("Name")
        lblName.setText("<b>Name</b>")

        self.editName = QLineEdit()
        btnOk = QPushButton("OK")

        layout = QVBoxLayout()
        # layout = QHBoxLayout()
        layout.addWidget(lblName)
        layout.addWidget(self.editName)
        layout.addWidget(btnOk)

        self.contents = QTextEdit()
        layout.addWidget(self.contents)

        self.setLayout(layout)

        btnOk.clicked.connect(self.btnOnClicked)

    def btnOnClicked(self):
        name = self.editName.text()
        QMessageBox.information(self, "Info", name)

app = QApplication([])
dialog = MyDialog()
dialog.show()
app.exec_()
