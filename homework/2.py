import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QCheckBox

class Hide(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 200, 150)
        self.setWindowTitle('Прятки для виджетов')

        self.checkbox_1 = QCheckBox('edit1', self)
        self.checkbox_1.move(10, 15)
        self.checkbox_1.clicked.connect(self.hiding)

        self.checkbox_2 = QCheckBox('edit2', self)
        self.checkbox_2.move(10, 50)
        self.checkbox_2.clicked.connect(self.hiding)

        self.checkbox_3 = QCheckBox('edit3', self)
        self.checkbox_3.move(10, 85)
        self.checkbox_3.clicked.connect(self.hiding)

        self.checkbox_4 = QCheckBox('edit4', self)
        self.checkbox_4.move(10, 120)
        self.checkbox_4.clicked.connect(self.hiding)

        self.widg1 = QLineEdit('Поле edit1', self)
        self.widg1.move(60, 15)

        self.widg2 = QLineEdit('Поле edit2', self)
        self.widg2.move(60, 50)

        self.widg3 = QLineEdit('Поле edit3', self)
        self.widg3.move(60, 85)

        self.widg4 = QLineEdit('Поле edit4', self)
        self.widg4.move(60, 120)

    def hiding(self):
        if self.checkbox_1.isChecked():
            self.widg1.show()
        else:
            self.widg1.hide()

        if self.checkbox_2.isChecked():
            self.widg2.show()
        else:
            self.widg2.hide()

        if self.checkbox_3.isChecked():
            self.widg3.show()
        else:
            self.widg3.hide()

        if self.checkbox_4.isChecked():
            self.widg4.show()
        else:
            self.widg4.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Hide()
    ex.show()
    sys.exit(app.exec())