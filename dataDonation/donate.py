from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUidonate(self, MainWindow):
        MainWindow.resize(783, 511)
        MainWindow.setWindowIcon(QtGui.QIcon('strava.jpg'))
        MainWindow.setStyleSheet("background-color: #DD571C;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        import interview
        self.interviewWindow = QtWidgets.QMainWindow()
        self.interviewUI = interview.Ui_MainWindow()
        self.interviewUI.setupUiInterview(self.interviewWindow)
        self.interviewWindow.hide()

        import chatBot
        checked = ""
        self.chatWindow = QtWidgets.QMainWindow()
        self.chatUI = chatBot.Ui_MainWindow()
        self.chatUI.setupUichat(self.chatWindow, checked)
        self.chatWindow.hide()

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QtCore.QRect(20, 20, 741, 471))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.titleLabel = QtWidgets.QLabel(self.frame)
        self.titleLabel.setGeometry(QtCore.QRect(70, 15, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(30, 60, 681, 20))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)

        self.workoutLabel = QtWidgets.QLabel(self.frame)
        self.workoutLabel.setGeometry(QtCore.QRect(340, 90, 371, 41))
        font.setBold(True)
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.workoutLabel.setFont(font)
        self.workoutLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.workoutLine = QtWidgets.QFrame(self.frame)
        self.workoutLine.setGeometry(QtCore.QRect(330, 120, 380, 20))
        self.workoutLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.workoutLine.setLineWidth(2)
        self.workoutLine.setFrameShape(QtWidgets.QFrame.HLine)

        self.selectLabel = QtWidgets.QLabel(self.frame)
        self.selectLabel.setGeometry(QtCore.QRect(50, 90, 221, 41))
        font.setBold(True)
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.selectLabel.setFont(font)
        self.selectLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.selectLine = QtWidgets.QFrame(self.frame)
        self.selectLine.setGeometry(QtCore.QRect(30, 120, 261, 20))
        self.selectLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.selectLine.setLineWidth(2)
        self.selectLine.setFrameShape(QtWidgets.QFrame.HLine)

        self.uploadButton = QtWidgets.QPushButton(self.frame, clicked=self.upload)
        self.uploadButton.setGeometry(QtCore.QRect(592, 350, 111, 41))
        self.uploadButton.setStyleSheet("background-color: white;")
        font.setBold(True)
        font.setFamily("Times New Roman")
        font.setPointSize(9)
        self.uploadButton.setFont(font)

        self.interviewButton = QtWidgets.QPushButton(self.frame, clicked=self.interview)
        self.interviewButton.setGeometry(QtCore.QRect(640, 20, 70, 41))
        self.interviewButton.setStyleSheet("background-color: white;")
        self.interviewButton.setFont(font)

        self.submitButton = QtWidgets.QPushButton(self.frame, clicked=self.submit)
        self.submitButton.setGeometry(QtCore.QRect(342, 420, 181, 41))
        self.submitButton.setStyleSheet("background-color: white;")
        self.submitButton.setFont(font)

        self.cancelButton = QtWidgets.QPushButton(self.frame, clicked=self.close)
        self.cancelButton.setGeometry(QtCore.QRect(530, 420, 181, 41))
        self.cancelButton.setStyleSheet("background-color: white;")
        self.cancelButton.setFont(font)

        self.updatesButton = QtWidgets.QPushButton(self.frame, clicked=self.updates)
        self.updatesButton.setGeometry(QtCore.QRect(30, 420, 181, 41))
        self.updatesButton.setStyleSheet("background-color: white;")
        self.updatesButton.setFont(font)

        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(345, 150, 361, 192))
        self.textBrowser.setStyleSheet("background-color: white; border: 1px solid black;")
        self.textBrowser.setAlignment(QtCore.Qt.AlignCenter)

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: white;")
        self.frame_2.setGeometry(QtCore.QRect(30, 140, 261, 271))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.ageBox = QtWidgets.QCheckBox(self.frame_2)
        self.ageBox.setGeometry(QtCore.QRect(20, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(7)
        self.ageBox.setFont(font)
        self.ageBox.stateChanged.connect(self.check1)

        self.genderBox = QtWidgets.QCheckBox(self.frame_2)
        self.genderBox.setGeometry(QtCore.QRect(140, 10, 101, 21))
        self.genderBox.stateChanged.connect(self.check2)
        self.genderBox.setFont(font)

        self.locationBox = QtWidgets.QCheckBox(self.frame_2)
        self.locationBox.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.locationBox.stateChanged.connect(self.check3)
        self.locationBox.setFont(font)

        self.activityBox = QtWidgets.QCheckBox(self.frame_2)
        self.activityBox.setGeometry(QtCore.QRect(140, 190, 110, 30))
        self.activityBox.stateChanged.connect(self.check4)
        self.activityBox.setFont(font)

        self.conditionBox = QtWidgets.QCheckBox(self.frame_2)
        self.conditionBox.setGeometry(QtCore.QRect(140, 70, 101, 21))
        self.conditionBox.stateChanged.connect(self.check5)
        self.conditionBox.setFont(font)

        self.trafficBox = QtWidgets.QCheckBox(self.frame_2)
        self.trafficBox.setGeometry(QtCore.QRect(140, 100, 101, 21))
        self.trafficBox.stateChanged.connect(self.check6)
        self.trafficBox.setFont(font)

        self.typeBox = QtWidgets.QCheckBox(self.frame_2)
        self.typeBox.setGeometry(QtCore.QRect(140, 40, 101, 21))
        self.typeBox.stateChanged.connect(self.check7)
        self.typeBox.setFont(font)

        self.accessBox = QtWidgets.QCheckBox(self.frame_2)
        self.accessBox.setGeometry(QtCore.QRect(20, 70, 113, 21))
        self.accessBox.stateChanged.connect(self.check8)
        self.accessBox.setFont(font)

        self.safetyBox = QtWidgets.QCheckBox(self.frame_2)
        self.safetyBox.setGeometry(QtCore.QRect(20, 100, 101, 21))
        self.safetyBox.stateChanged.connect(self.check9)
        self.safetyBox.setFont(font)

        self.gearBox = QtWidgets.QCheckBox(self.frame_2)
        self.gearBox.setGeometry(QtCore.QRect(20, 160, 101, 21))
        self.gearBox.stateChanged.connect(self.check10)
        self.gearBox.setFont(font)

        self.traffic2 = QtWidgets.QCheckBox(self.frame_2)
        self.traffic2.setGeometry(QtCore.QRect(140, 160, 101, 21))
        self.traffic2.stateChanged.connect(self.check11)
        self.traffic2.setFont(font)

        self.wildlifeBox = QtWidgets.QCheckBox(self.frame_2)
        self.wildlifeBox.setGeometry(QtCore.QRect(20, 130, 101, 21))
        self.wildlifeBox.stateChanged.connect(self.check12)
        self.wildlifeBox.setFont(font)

        self.difBox = QtWidgets.QCheckBox(self.frame_2)
        self.difBox.setGeometry(QtCore.QRect(140, 130, 101, 21))
        self.difBox.stateChanged.connect(self.check13)
        self.difBox.setFont(font)

        self.emotionBox = QtWidgets.QCheckBox(self.frame_2)
        self.emotionBox.setGeometry(QtCore.QRect(20, 190, 101, 30))
        self.emotionBox.stateChanged.connect(self.check14)
        self.emotionBox.setFont(font)

        self.groupBox = QtWidgets.QCheckBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 230, 221, 30))
        self.groupBox.stateChanged.connect(self.check15)
        self.groupBox.setFont(font)

        self.runBox1 = QtWidgets.QCheckBox(self.frame)
        self.runBox1.setGeometry(QtCore.QRect(350, 350, 101, 21))
        self.runBox1.setFont(font)
        self.runBox1.stateChanged.connect(self.check16)
        self.runBox1.hide()

        self.runBox2 = QtWidgets.QCheckBox(self.frame)
        self.runBox2.setGeometry(QtCore.QRect(460, 350, 101, 21))
        self.runBox2.setFont(font)
        self.runBox2.stateChanged.connect(self.check17)
        self.runBox2.hide()

        self.langs = {'age': 0, 'gender': 0, 'location': 0, 'activity': 0, 'condition': 0, 'traffic': 0, 'type': 0,
                      'access': 0,
                      'safety': 0, 'gear': 0, 'wildlife': 0, 'dif': 0, 'emotion': 0, 'group': 0, 'traffic2': 0,
                      'Evening Run': 0,
                      'Morning Run': 0}

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def upload(self):
        f1 = "<p align=\"center\" style=\"line-height:138%;\"><span style=\" font-family:\'Times New Roman\',\'" \
             "sans-serif\'; font-size:11pt; font-weight:600; text-decoration: underline; color:#000000;\">"
        f2 = "</span></p>\n<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-right:0px; " \
             "line-height:138%;\"><span style=\" font-family:\'Times New Roman\',\'sans-serif\'; font-size:9pt; " \
             "font-weight:600; color:#000000;\">"
        f3 = "</span><span style=\" font-family:\'Times New Roman\',\'sans-serif\'; font-size:9pt; color:#000000;\"> "
        f4 = "</span></p></body></html>"
        text = f"""{f1}Evening Run 1{f2}Date:{f3}May 25, 2023 at 7:06 PM{f2}
          Location:{f3}Rochester Hills, Michigan{f2}Distance:{f3}6.62 mi{f2}Avg Pace:{f3}9:50 /mi{f2}Moving time:{f3}
          1:05:09{f2}Elevation Gain:{f3}67 ft{f2}Max Elevation:{f3}850 ft{f2}{f1}Morning Run 1{f2}Date:{f3}
          June 11, 2023 at 8:30 AM{f2}Location:{f3}Addison Township, Michigan{f2}Distance:{f3}13.45 mi{f2}Avg Pace:{f3}
          9:48 /mi{f2}Moving time:{f3}2:11:55{f2}Elevation Gain:{f3}715 ft{f2}Max Elevation:{f3}
          1,085 ft{f4}"""
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("MainWindow", text))
        self.runBox1.show()
        self.runBox2.show()

    def close(self):
        MainWindow.close()

    def updates(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QtGui.QIcon('strava.jpg'))
        msg.setWindowTitle("Recent Updated")
        msg.setText("There are no recent updates :)")
        msg.exec_()

    def check1(self, checked):
        if checked:
            self.langs['age'] = 1
        else:
            self.langs['age'] = 0

    def check2(self, checked):
        if checked:
            self.langs['gender'] = 1
        else:
            self.langs['gender'] = 0

    def check3(self, checked):
        if checked:
            self.langs['location'] = 1
        else:
            self.langs['location'] = 0

    def check4(self, checked):
        if checked:
            self.langs['activity'] = 1
        else:
            self.langs['activity'] = 0

    def check5(self, checked):
        if checked:
            self.langs['condition'] = 1
        else:
            self.langs['condition'] = 0

    def check6(self, checked):
        if checked:
            self.langs['traffic'] = 1
        else:
            self.langs['traffic'] = 0

    def check7(self, checked):
        if checked:
            self.langs['type'] = 1
        else:
            self.langs['type'] = 0

    def check8(self, checked):
        if checked:
            self.langs['access'] = 1
        else:
            self.langs['access'] = 0

    def check9(self, checked):
        if checked:
            self.langs['safety'] = 1
        else:
            self.langs['safety'] = 0

    def check10(self, checked):
        if checked:
            self.langs['gear'] = 1
        else:
            self.langs['gear'] = 0

    def check11(self, checked):
        if checked:
            self.langs['wildlife'] = 1
        else:
            self.langs['wildlife'] = 0

    def check12(self, checked):
        if checked:
            self.langs['dif'] = 1
        else:
            self.langs['dif'] = 0

    def check13(self, checked):
        if checked:
            self.langs['emotion'] = 1
        else:
            self.langs['emotion'] = 0

    def check14(self, checked):
        if checked:
            self.langs['group'] = 1
        else:
            self.langs['group'] = 0

    def check15(self, checked):
        if checked:
            self.langs['traffic2'] = 1
        else:
            self.langs['traffic2'] = 0

    def check16(self, checked):
        if checked:
            self.langs['Evening Run'] = 1
        else:
            self.langs['Evening Run'] = 0

    def check17(self, checked):
        if checked:
            self.langs['Morning Run'] = 1
        else:
            self.langs['Morning Run'] = 0

    def submit(self):
        # checked = []
        # for i in self.langs.keys():
        #     if self.langs[i] == 1:
        #         checked.append(self.langs.keys())
        checked = ', '.join([key for key in self.langs.keys()
                            if self.langs[key] == 1])
        self.chatUI.setupUichat(self.chatWindow, checked)
        self.chatWindow.show()

    def interview(self):
        self.interviewWindow.show()


    def retranslateUi(self, MainWindow):
        text = ""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Want Data Do You Want to Donate?"))
        self.uploadButton.setText(_translate("MainWindow", "Upload Data"))
        self.submitButton.setText(_translate("MainWindow", "Submit Data"))
        self.interviewButton.setText(_translate("MainWindow", "Schedule \nInterview"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel Donation"))
        self.workoutLabel.setText(_translate("MainWindow", "Your Workouts"))
        self.selectLabel.setText(_translate("MainWindow", "Select Your Data"))
        self.updatesButton.setText(_translate("MainWindow", "Recent Updates"))
        self.textBrowser.setHtml(_translate("MainWindow", text))
        self.ageBox.setText(_translate("MainWindow", "Age"))
        self.genderBox.setText(_translate("MainWindow", "Gender"))
        self.locationBox.setText(_translate("MainWindow", "Location"))
        self.activityBox.setText(_translate("MainWindow", "Typical Activity \nLevel"))
        self.conditionBox.setText(_translate("MainWindow", "Trail Conditions"))
        self.trafficBox.setText(_translate("MainWindow", "Trail Traffic"))
        self.typeBox.setText(_translate("MainWindow", "Workout Types"))
        self.accessBox.setText(_translate("MainWindow", "Trail Accessibility"))
        self.safetyBox.setText(_translate("MainWindow", "Trail Safety"))
        self.gearBox.setText(_translate("MainWindow", "Gear Used"))
        self.wildlifeBox.setText(_translate("MainWindow", "Trail wildlife"))
        self.difBox.setText(_translate("MainWindow", "Trail Difficulty"))
        self.emotionBox.setText(_translate("MainWindow", "Emotional \nHeadspace"))
        self.groupBox.setText(_translate("MainWindow", "Individual/Group Workout"))
        self.traffic2.setText(_translate("MainWindow", "Trail Traffic"))
        self.runBox1.setText(_translate("MainWindow", "Evening Run 1"))
        self.runBox2.setText(_translate("MainWindow", "Morning Run 1"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUidonate(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
