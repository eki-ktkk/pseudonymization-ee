import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot
from mspresidio import anonymize, hide_names, hide_dates

#Basic GUI for anonymizer that was created for demo
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Anonymizer'
        self.left = 10
        self.top = 10
        self.width = 720
        self.height = 1080
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.textbox = QTextEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(680, 400)

        self.lable = QLabel(self)
        self.lable.move(20, 500)
        self.lable.resize(680, 500)
        self.lable.setFont(QFont('Arial', 20))
        self.lable.setWordWrap(True)
        self.lable.setStyleSheet("border: 1px solid black;")

        self.button = QPushButton('Start', self)
        self.button.move(260, 440)

        self.button2 = QPushButton('Clear', self)
        self.button2.move(400, 440)

        self.button.clicked.connect(self.on_click_start)
        self.button2.clicked.connect(self.on_click_clear)
        self.show()


    @pyqtSlot()
    def on_click_start(self):
        textboxValue = self.textbox.toPlainText()
        if textboxValue == '':
            self.lable.setText('Please insert text for anonymization')
        else:
            textboxValue = hide_dates(textboxValue, '<DATE>')
            textboxValue = hide_names(textboxValue, '<PERSON>')
            textboxValue = anonymize(textboxValue)
            self.lable.setText(textboxValue.text)

    @pyqtSlot()
    def on_click_clear(self):
        self.lable.setText('')
        self.textbox.setPlainText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())