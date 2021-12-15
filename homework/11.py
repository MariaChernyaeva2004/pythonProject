import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 210, 300)
        self.setWindowTitle('Перемешать строки')
        self.btn = QPushButton('Загрузить строки', self)
        self.btn.move(0, 0)
        self.btn.resize(110, 30)
        self.btn.clicked.connect(self.load)
        self.txted = QPlainTextEdit(self)
        self.txted.move(0, 30)
        self.txted.resize(200, 250)

    def load(self):
        with open('str.txt', encoding='utf-8') as f:
            lines = f.read().split('\n')
            for j in range(0, len(lines), 2):
                self.txted.appendPlainText(lines[j])
            for k in range(1, len(lines), 2):
                self.txted.appendPlainText(lines[k])
            f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
