import sys

from PyQt4 import QtGui, QtCore



class testDialog(QtGui.QDialog):

    def __init__(self, parent=None):

        super(testDialog, self).__init__(parent)



        form = QtGui.QFormLayout()

        form.setHorizontalSpacing(0)



        self.myedit = QtGui.QLineEdit()

        self.myedit.setDragEnabled(True)

        self.myedit.setAcceptDrops(True)

        self.myedit.installEventFilter(self)



        form.addWidget(self.myedit)



        self.setLayout(form)

        self.setGeometry(300, 300, 400, 0)

        self.setWindowTitle('drop test')



        self.myedit.textChanged.connect(self.editchange)   # new style signal slot connections



    @QtCore.pyqtSlot(str)   # int represent the column value

    def editchange(self,data):

        # print('editchange:', unicode(data))
        print('editchange:', data)



    def eventFilter(self, object, event):

        if (object is self.myedit):

            if (event.type() == QtCore.QEvent.DragEnter):

                if event.mimeData().hasUrls():

                    event.accept()   # must accept the dragEnterEvent or else the dropEvent can't occur !!!

                    print('accept')

                else:

                    event.ignore()

                    print('ignore')

            if (event.type() == QtCore.QEvent.Drop):

                if event.mimeData().hasUrls():   # if file or link is dropped

                    urlcount = len(event.mimeData().urls())  # count number of drops

                    url = event.mimeData().urls()[0]   # get first url

                    object.setText(unicode(url.toLocalFile()))   # assign first url to editline

                    #event.accept()  # doesnt appear to be needed

            return False # lets the event continue to the edit

        return False



if __name__ == "__main__":



    app = QtGui.QApplication([])

    dl = testDialog()

    dl.exec_()

    sys.exit(app.closeAllWindows())