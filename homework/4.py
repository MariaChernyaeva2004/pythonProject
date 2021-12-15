import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

mors = {'A': '.-', 'B': '-...',

                   'C': '-.-.', 'D': '-..', 'E': '.',

                   'F': '..-.', 'G': '--.', 'H': '....',

                   'I': '..', 'J': '.---', 'K': '-.-',

                   'L': '.-..', 'M': '--', 'N': '-.',

                   'O': '---', 'P': '.--.', 'Q': '--.-',

                   'R': '.-.', 'S': '...', 'T': '-',

                   'U': '..-', 'V': '...-', 'W': '.--',

                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}
class Morse(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 320, 100)
        self.setWindowTitle('Азбука Морзе 2')

        self.str = QLineEdit(self)
        self.str.setGeometry(5, 100, 255, 100)
        self.str.setReadOnly(True)
        b = 0

        for i, j in mors.items():
            self.btn = QPushButton(i, self)
            self.btn.setText(i)
            self.btn.resize(30, 30)
            self.btn.move(b, 0)
            b = b + 35
            self.btn.clicked.connect(self.result)

    def result(self):
        s = mors[self.sender().text()]
        d = self.str.text()
        self.str.setText(f"{d} {s} ")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    m = Morse()
    m.show()
    sys.exit(app.exec())