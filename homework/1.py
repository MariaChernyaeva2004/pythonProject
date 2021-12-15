import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Focus(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 320, 60)
        self.setWindowTitle('Фокус со словами')

        self.le1 = QLineEdit(self)
        self.le1.move(130, 90)
        self.le1.setGeometry(10, 20, 125, 30)

        self.le2 = QLineEdit(self)
        self.le2.setGeometry(175, 20, 125, 30)

        self.btn = QPushButton('->', self)
        self.btn.setGeometry(140, 20, 30, 30)
        self.btn.clicked.connect(self.word)

    def word(self):
        if self.btn.text() == '->':
            self.btn.setText('<-')
            self.le2.setText(self.untr.text())
            self.le1.setText('')

        else:
            self.btn.setText('->')
            self.le1.setText(self.tr.text())
            self.le2.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec())