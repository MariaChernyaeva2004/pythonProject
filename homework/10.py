import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 390, 180)
        self.setWindowTitle('Случайная строка')
        self.labels = ['Название файла', 'Максимальное значение:', 'Минимальное значение:', 'Среднее значение:']
        self.btn = QPushButton('Рассчитать', self)
        self.btn.move(300, 0)
        self.btn.resize(80, 30)
        self.btn.clicked.connect(self.run)
        self.edits = []
        self.lst = []
        self.label1 = QLabel('', self)
        self.label1.move(0, 160)
        self.label1.resize(290, 15)

        x = 0
        y = 0
        for i in range(4):
            self.label = QLabel(self.labels[i], self)
            self.label.move(x, y)
            self.label.resize(190, 20)
            if i > 0:
                self.edit = QLineEdit('0', self)
                self.edit.move(x + 180, y)
                self.edit.resize(100, 30)
                self.edits.append(self.edit)
                y += 40
            else:
                self.edit = QLineEdit('', self)
                self.edit.move(x + 180, y)
                self.edit.resize(100, 30)
                self.edits.append(self.edit)
                y += 40

    def run(self):
        self.label1.setText('')
        file = self.edits[0].text()
        try:
            lst = []
            f = open(file)
            lines = f.read().split()
            for elem in lines:
                lst.append(int(elem))
            self.edits[1].setText(str(max(lst)))
            self.edits[2].setText(str(min(lst)))
            self.edits[3].setText(str(sum(lst) / len(lst)))
            f.close()
            with open("output.txt", "w", encoding='utf-8') as f1:
                for i in range(1, 4):
                    f1.write(self.labels[i] + self.edits[i].text() + '\n')
            f1.close()

        except FileNotFoundError:
            self.label1.setText("Файл '{}'не наден".format(file))
        except ValueError:
            self.label1.setText('Файл {} имеет неверный формат данных'.format(file))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
