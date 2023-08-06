import re

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUichat(self, MainWindow, checked):
        MainWindow.resize(619, 589)
        print(checked)
        MainWindow.setWindowIcon(QtGui.QIcon('strava.jpg'))
        MainWindow.setStyleSheet("background-color: #DD571C;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(29, 29, 561, 531))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(30, 20, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 60, 501, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.submitButton = QtWidgets.QPushButton(self.frame, clicked=lambda: self.chatFill(checked))
        self.submitButton.setGeometry(QtCore.QRect(300, 470, 181, 41))
        font.setBold(True)
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.submitButton.setStyleSheet("background-color: white;")
        self.submitButton.setFont(font)

        self.skipButton = QtWidgets.QPushButton(self.frame, clicked=self.skip)
        self.skipButton.setGeometry(QtCore.QRect(80, 470, 181, 41))
        self.skipButton.setStyleSheet("background-color: white;")
        self.skipButton.setFont(font)

        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(50, 100, 461, 251))
        self.textBrowser.setStyleSheet("background-color: white; border: 1px solid black;")
        self.textBrowser.setFont(font)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(50, 360, 461, 87))
        self.textEdit.setStyleSheet("background-color: white; border: 1px solid black;")
        self.textEdit.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def submit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Data Donation")
        msg.setWindowIcon(QtGui.QIcon('strava.jpg'))
        msg.setText("Your data has been successfully donated. :)\n "
                    "You can choose to remove your data from our system at any time.")
        msg.exec_()

    def skip(self):
        print("go to next")

    def chatFill(self, checked):
        if re.search(checked, "age"):
            print("Do you still want to provide demographic information?")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Contextualize Your Data"))
        self.submitButton.setText(_translate("MainWindow", "Submit Data"))
        self.skipButton.setText(_translate("MainWindow", "Skip Question"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:transparent;\">Strava:</span><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:9pt; color:#000000; background-color:transparent;\"> Hello.</span></p>\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:138%;\"><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:9pt; font-weight:600; color:#000000; background-color:transparent;\">Me:</span><span style=\" font-family:\'Arial\',\'sans-serif\'; font-size:9pt; color:#000000; background-color:transparent;\"> Hi   </span></p></body></html>"))

        self.textEdit.setHtml(_translate("MainWindow", "*Enter Message Here*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUichat(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
