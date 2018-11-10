import os
import sys

from PyQt4.QtGui import *

import Gui.SubtitleRenamer.SubRenamer


class XDialog(QDialog, Gui.SubtitleRenamer.SubRenamer.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.fileLists_1 = [];
        self.fileLists_2 = [];

        self.buttonBox.clicked.connect(self.saveData)

        # Suc - mouseReleaseEvent
        # self.textEdit.mouseReleaseEvent = self.MyMouseReleaseEvent

        self.textEdit.dropEvent = self.dropEvent
        self.textEdit_2.dropEvent = self.dropEvent_2


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

        print('list', self.fileLists_1)

        self.fileLists_1

        for i in range(len(self.fileLists_1)):
            print('print ' , i, self.fileLists_1[i])
            print('print directoryName ' , i, os.path.dirname( self.fileLists_1[i]) )
            print('print baseName ' , i, os.path.basename( self.fileLists_1[i]) )

            videoBaseName = os.path.basename( self.fileLists_1[i])
            videoFileName,videoExtName = os.path.splitext(videoBaseName)
            # subTitleName = os.path.basename( self.fileLists_2[i])

            subTitleDirName = os.path.dirname( self.fileLists_2[i] )
            subTitleBaseName, subTitleExtName = os.path.splitext( self.fileLists_2[i] )
            print('subTitleBaseName', subTitleBaseName, 'subTitleExtName', subTitleExtName)
            print('renamed name', subTitleDirName+videoBaseName+subTitleExtName)
            os.rename(self.fileLists_2[i], subTitleDirName+ '/' + videoFileName + subTitleExtName)

            # fileName, file_extention = os.path.splitext(self.fileLists_1[i])
            # print('filename', fileName, 'file_extention', file_extention)

            # print('print directoryName ' , i, os.path.dirname(self.fileLists_1[i]) )
            # os.rename(filePath, filePath.replace("test.txt", "result.txt"))

        QMessageBox.information(self, "저장", text)

    def dropEvent(self, event):
        print("DROPPED")
        if event.mimeData().hasUrls():  # if file or link is dropped
            urlcount = len(event.mimeData().urls())  # count number of drops
            url = event.mimeData().urls()[0]  # get first url

            print('url.toString()', url.toString())
            # self.textEdit.append(url.toString() + '\r')
            filePath = url.toString()
            filePath = filePath.replace("file:///", "")
            self.textEdit.append( filePath )
            # self.setText(url.toString())  # assign first url to editline
            # event.accept()  # doesnt appear to be needed

            self.fileLists_1.append(filePath)

    def dropEvent_2(self, event):
        print("DROPPED")
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            print('url.toString()', url.toString())
            filePath = url.toString()
            filePath = filePath.replace("file:///", "")
            self.textEdit_2.append( filePath )

            self.fileLists_2.append(filePath)

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


