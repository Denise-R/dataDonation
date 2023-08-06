from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUiInterview(self, MainWindow):
        MainWindow.resize(701, 366)
        MainWindow.setWindowIcon(QtGui.QIcon('strava.jpg'))
        MainWindow.setStyleSheet("background-color: #DD571C;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 661, 326))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(5, 5, 661, 30))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 35, 601, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(230, 75, 401, 221))
        self.calendarWidget.setStyleSheet("background-color: gray; border: 1px solid black;")

        self.timeEdit = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(30, 125, 161, 51))
        font.setBold(True)
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.timeEdit.setStyleSheet("border: 1px solid black;")
        self.timeEdit.setFont(font)

        self.pushButton = QtWidgets.QPushButton(self.frame, clicked=self.book)
        self.pushButton.setGeometry(QtCore.QRect(30, 220, 161, 51))
        self.pushButton.setStyleSheet("background-color: white;")
        self.pushButton.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def book(self):
        msg = QMessageBox()
        date = self.calendarWidget.selectedDate()
        strDate = date.toString("MM-dd-yyyy")
        timeSelected = self.timeEdit.time()
        hour = timeSelected.hour()
        if hour == 0:
            hour = 12
        min = timeSelected.minute()
        if min <= 9:
            min = "0" + str(min)
        ampm = "AM"
        if hour > 12:
            ampm = "PM"
        timeSelected = str(hour) + ":" + str(min) + " " + ampm
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('strava.jpg'))
        msg.setWindowTitle("Interview Booking")
        msg.setText("Your interview date has been booked. \n\n Date: " + strDate +
                    "\n Time: " + str(timeSelected))
        msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "Select Your Interview Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUiInterview(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
