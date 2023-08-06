from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# C:\Users\denis\AppData\Local\Programs\Python\Python38
# pyqt5-tools designer
# pyuic5 -x window.ui -o window.py

class Ui_MainWindow(object):
    def setupUiHome(self, MainWindow):
        MainWindow.resize(850, 400)
        MainWindow.setWindowIcon(QtGui.QIcon('strava.jpg'))
        MainWindow.setStyleSheet("background-color: #DD571C;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setStyleSheet("background-color: white;")
        self.frame1.setGeometry(QtCore.QRect(20, 20, 810, 530))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)

        self.titleLabel = QtWidgets.QLabel(self.frame1)
        self.titleLabel.setGeometry(QtCore.QRect(30, 30, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.donate = QtWidgets.QPushButton(self.frame1, clicked=self.donate)
        self.donate.setGeometry(QtCore.QRect(65, 170, 290, 111))
        self.donate.setStyleSheet("background-image : url(shoes3.png);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.donate.setFont(font)

        self.cancel = QtWidgets.QPushButton(self.frame1, clicked=self.close)
        self.cancel.setGeometry(QtCore.QRect(444, 170, 290, 111))
        self.cancel.setStyleSheet("background-image : url(cancel.png);")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.cancel.setFont(font)

        self.info = QtWidgets.QPushButton(self.frame1, clicked=self.info)
        self.info.setGeometry(QtCore.QRect(65, 100, 70, 25))
        self.info.setStyleSheet("background-color: #779ecb;")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        font.setBold(True)
        self.info.setFont(font)

        self.line = QtWidgets.QFrame(self.frame1)
        self.line.setGeometry(QtCore.QRect(90, 80, 621, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.namesLabel = QtWidgets.QLabel(self.frame1)
        self.namesLabel.setGeometry(QtCore.QRect(30, 290, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        self.namesLabel.setFont(font)
        self.namesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.namesLabel.setObjectName("namesLabel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def info(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon(':/pictures/question.png'))
        msg.setWindowTitle("Info: What is Data Donation")
        msg.setText("\n\nHere at Strava, we want to match our users to nearby trail systems for running/hiking "
                    "by training a machine learning model on the popularity, difficulty, and train of trail."
                    " With your help, we hope to make it easier for new runners and hikers to find nearby "
                    "trail systems that are best suited for their workout needs.\n\nWe are hoping to collect data on "
                    "user demographics, workout experience, gear used, and trail conditions. \n\nDonors will have the "
                    "ability to select exactly what types of data they want to donate, the freedom to donate as much "
                    "or as little data they want, and the ability to remove their data from our system at any time. "
                    "\n\nIf you choose to donate, all of your data will be stored on Strava's private, protected "
                    "server. \n\nThis process is 100% anonymous! \n\nFor all your help, please enjoy a 1 month free "
                    "premium Strava subscription :) \n\n\nPromo Code 🏃: 'donation'\n\n\nFor additional information "
                    "please contact us at: starva@gamil.com")
        msg.exec_()

    def donate(self):
        import donate
        self.donateWindow = QtWidgets.QMainWindow()
        self.donateUI = donate.Ui_MainWindow()
        self.donateUI.setupUidonate(self.donateWindow)
        MainWindow.close()
        self.donateWindow.show()



    def close(self):
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Strava Data Donation"))
        self.titleLabel.setText(_translate("MainWindow", "Strava Data Donation"))
        self.info.setText(_translate("MainWindow", "Info"))
        self.donate.setText(_translate("MainWindow", "Donate My Data"))
        self.cancel.setText(_translate("MainWindow", "Cancel Donation"))
        self.namesLabel.setText(_translate("MainWindow", "Created by: Denise Rauschendorfer, Andrea Macklem-Zabel "
                                                         "& David Kosakowski"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiHome(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
