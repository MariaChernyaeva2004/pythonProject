import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 390, 300)
        self.setWindowTitle('Файловый редактор')
        self.btn = QPushButton('Создать новый', self)

        self.btn.move(5, 50)
        self.btn.resize(150, 30)
        self.btn.clicked.connect(self.new)

        self.btn1 = QPushButton('Сохранить файл', self)
        self.btn1.move(5, 100)
        self.btn1.resize(150, 30)
        self.btn1.clicked.connect(self.save)

        self.edit = QLineEdit(self)
        self.edit.move(5, 0)
        self.edit.resize(150, 30)

        self.btn3 = QPushButton('Открыть файл', self)
        self.btn3.move(3, 150)
        self.btn3.resize(150, 30)
        self.btn3.clicked.connect(self.open)

        self.ed = QPlainTextEdit(self)
        self.ed.move(170, 0)
        self.ed.resize(200, 270)

    def open(self):

        with open(self.edit.text(), 'r', encoding='utf-8') as f:
            self.ed.setPlainText(f.read())

    def save(self):
        text = self.ed.toPlainText()
        with open(self.edit.text(), 'w', encoding='utf-8') as f:
            f.write(text)

    def new(self):
        self.ed.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
