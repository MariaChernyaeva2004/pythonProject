import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QCheckBox, QPlainTextEdit
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 300, 420, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        menu = ['Чизбургер', "Гамбургер", 'Кока-кола', 'Нагетсы']
        x = 0
        for v in menu:
            self.btn = QCheckBox(self)
            self.btn.setText(v)
            self.btn.resize(100, 20)
            self.btn.move(0, x)
            x = x + 20
            self.btn.stateChanged.connect(self.run)
        self.out = []

        self.knop = QPushButton(self)
        self.knop.setText('Заказать')
        self.knop.resize(70, 30)
        self.knop.move(50, 100)
        self.knop.clicked.connect(self.prt)

        self.b = QPlainTextEdit(self)
        self.b.insertPlainText(' ')
        self.b.setEnabled(False)
        self.b.move(10, 150)
        self.b.resize(400, 200)

    def run(self, state):
        if state == Qt.Checked:
            self.out.append(self.sender().text())
        else:
            self.out.remove(self.sender().text())

    def prt(self):
        sp = self.out
        lst = 'Ваш заказ:'
        for i in sp:
            lst += ' \n' + str(i)
        self.b.setPlainText(lst)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
