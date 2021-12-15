import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300, 200, 320, 60)
        self.setWindowTitle('Арифмометр')

        self.first_value = QLineEdit(self) #1 цифра
        self.first_value.move(10, 10)
        self.first_value.resize(30, 30)

        self.second_value = QLineEdit(self) #2 цифра
        self.second_value.move(130, 10)
        self.second_value.resize(30, 30)

        self.output_value = QLineEdit(self) #результат
        self.output_value.move(170, 10)
        self.output_value.resize(30, 30)
        self.output_value.setEnabled(False)

        self.sum_btn = QPushButton('+', self)
        self.sum_btn.resize(30, 30)
        self.sum_btn.move(40, 10)
        self.sum_btn.clicked.connect(self.go_sum)

        self.sub_btn = QPushButton('-', self)
        self.sub_btn.resize(30, 30)
        self.sub_btn.move(70, 10)
        self.sub_btn.clicked.connect(self.go_sub)

        self.multi_btn = QPushButton('*', self)
        self.multi_btn.resize(30, 30)
        self.multi_btn.move(100, 10)
        self.multi_btn.clicked.connect(self.go_multi)

        self.label1 = QLabel("=", self)
        self.label1.resize(30, 30)
        self.label1.move(160, 10)


    def go_sum(self):
        self.output_value.setText(str(float(self.first_value.text()) + float(self.second_value.text())))

    def go_sub(self):
        self.output_value.setText(str(float(self.first_value.text()) - float(self.second_value.text())))

    def go_multi(self):
        self.output_value.setText(str(float(self.first_value.text()) * float(self.second_value.text())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())