import sys

from PyQt4.QtGui import *

import Gui.SubtitleRenamer.SubRenamer


class XDialog(QDialog, Gui.SubtitleRenamer.SubRenamer.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.buttonBox.clicked.connect(self.saveData)

        # Suc - mouseReleaseEvent
        # self.textEdit.mouseReleaseEvent = self.MyMouseReleaseEvent

        self.textEdit.dropEvent = self.dropEvent

        # self.connect(self.textEdit, SIGNAL("textChanged()"), self.usr_enter)
        # QtCore.QObject.connect(self.textEdit, QtCore.SIGNAL("textChanged()"),
        #                        self.text_change)

        # Fail
        # QtCore.QObject.connect(self.textEdit, QtCore.SIGNAL("dropped"),
        #                        self.textDropEvent)

        # Fail
        # self.connect(self, QtCore.SIGNAL("dropped"), self.textDropEvent)

        # self.textEdit.connect(self.textEdit, SIGNAL("textChanged()"),
        #                       self.textEdit, SLOT("slotTextChanged()"))

    def saveData(self):
        print('save Data')
        text = self.textEdit.toPlainText()

        for line in text.split('\n'):
            print('line', line)

        QMessageBox.information(self, "저장", text)

    def dropEvent(self, event):
        print("DROPPED")
        if event.mimeData().hasUrls():  # if file or link is dropped
            urlcount = len(event.mimeData().urls())  # count number of drops
            url = event.mimeData().urls()[0]  # get first url

            print('url.toString()', url.toString())
            # self.textEdit.append(url.toString() + '\r')
            self.textEdit.append(url.toString() )
            # self.setText(url.toString())  # assign first url to editline
            # event.accept()  # doesnt appear to be needed

    def MyMouseReleaseEvent(self, Event):
        print("Release the mouse.")
        Pos = Event.pos()
        print("Pos = (%d, %d)" % (Pos.x(), Pos.y()))


    def text_change(self):
        print('has chaged')
        # filePath = self.textEdit.toPlainText()
        # self.textEdit.setText(filePath + "\n")
        # self.textEdit.append('\r\n')

        # filePath = filePath.replace("file:///", "")
        # print('filePath', filePath)
        # f = open(filePath, "r")
        # print('readLine', f.readline())
        # print('readLine', f.readline())
        # print('readLine', f.read())
        # f.close()
        # os.rename(filePath, filePath.replace("test.txt", "result.txt"))


    # @pyqtSlot()
    # def slotTextChanged(self):
    #     print('test')
    #     QMessageBox.information(self, "Change", "Text Chage" + self.textEdit.toPlainText())

app = QApplication(sys.argv)
dig = XDialog()
dig.show()
app.exec_()


