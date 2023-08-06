import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QApplication, QDesktopWidget,
                             QDialog, QTextEdit, QGridLayout, QPushButton, QWidget, QSizePolicy)
from PyQt5.QtGui import QIcon

class Chat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        Chat.setFixedHeight(
            (Chat.fontMetrics().lineSpacing() * 3) +
            (Chat.document().documentMargin() * 2) +
            (Chat.frameWidth() * 2) - 1
        )

    def initUI(self):
        self.populateUI()

        self.resize(400, 400)
        self.center()
        self.setWindowTitle('Simple Chat')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def populateUI(self):
        self.createMenu()
        self.statusBar()
        centralWidget = CentralWidget()
        self.setCentralWidget(centralWidget)

    def createMenu(self):
        menuBar = self.menuBar()

        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(self.createExitAction())

        helpMenu = menuBar.addMenu('&Help')
        helpMenu.addAction(self.createAboutAction())

    def createExitAction(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        return exitAction

    def createAboutAction(self):
        aboutAction = QAction(QIcon('info.png'), '&About', self)
        aboutAction.setShortcut('Ctrl+H')
        aboutAction.setStatusTip('Information about the program')
        aboutAction.triggered.connect(self.createAboutDialog)
        return aboutAction

    def createAboutDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('About')
        dialog.setWindowIcon(QIcon('info.png'))
        dialog.resize(200, 200)
        dialog.exec_()

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ribbon = QTextEdit()
        chat = QTextEdit()
        sendBtn = QPushButton('Send')
        policy = sendBtn.sizePolicy()
        policy.setVerticalPolicy(QSizePolicy.MinimumExpanding)
        sendBtn.setSizePolicy(policy)

        grid = QGridLayout()
        grid.setSpacing(3)
        grid.addWidget(ribbon, 0, 0, 1, 3)
        grid.addWidget(chat, 1, 0, 1, 1)
        grid.addWidget(sendBtn, 1, 2)
        grid.setRowStretch(0, 1)
        grid.setColumnStretch(0, 1)

        self.setLayout(grid)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat = Chat()
    sys.exit(app.exec_())