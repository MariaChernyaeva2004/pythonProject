import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 390, 50)
        self.setWindowTitle('Случайная строка')

        self.btn = QPushButton('Получить', self)
        self.btn.move(0, 0)
        self.btn.resize(70, 20)
        self.btn.clicked.connect(self.choice)
        self.lined = QLineEdit(self)
        self.lined.move(70, 0)
        self.lined.resize(150, 20)

    def choice(self):
        with open('input.txt', encoding='utf-8') as f:
            lines = f.readlines()
            self.lined.setText(lines[randint(0, len(lines)-1)])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
