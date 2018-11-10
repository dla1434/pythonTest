from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT
import sys


class myTextEdit(QtGui.QTextEdit):
    @pyqtSlot()
    def slotTextChanged(self):
        QtGui.QMessageBox.information(self, "QTextEdit Text Changed!!", "Current Text is:" + self.toPlainText());


def main():
    app = QtGui.QApplication(sys.argv)
    textEdit = myTextEdit()

    # Resize width and height
    textEdit.resize(250, 250)
    textEdit.setWindowTitle('PyQt QTextEdit Text Change Example')

    textEdit.connect(textEdit, SIGNAL("textChanged()"),
                     textEdit, SLOT("slotTextChanged()"))
    textEdit.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()