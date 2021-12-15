import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QButtonGroup, QRadioButton, QGridLayout, QVBoxLayout, \
    QApplication


class Window(QWidget):
    def __init__(self):
        super().__init__(None)

        self.setWindowTitle('Крестики-нолики')
        self.setGeometry(300, 300, 300, 70)
        self.button = QPushButton("Новая игра")
        self.button.clicked.connect(self.start)
        self.label = QLabel("")

        self.switcher = QButtonGroup()
        button0 = QRadioButton("0")
        buttonX = QRadioButton("X")
        self.switcher.addButton(button0, 0)
        self.switcher.addButton(buttonX, 1)

        self.buttons = []
        layoutB = QGridLayout()
        layoutB.setSpacing(0)
        x, y = 0, 0
        for i in range(9):
            button = QPushButton()
            self.buttons.append(button)
            button.setObjectName(str(i))
            button.clicked.connect(self.process)
            layoutB.addWidget(button, y, x)
            if (x == 2):
                x = 0
                y = y + 1
            else:
                x = x + 1

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(button0)
        layout.addWidget(buttonX)
        layout.addLayout(layoutB)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.start()

    def start(self):
        self.switcher.button(0).setEnabled(True)
        self.switcher.button(1).setEnabled(True)
        self.switcher.button(1).setChecked(True)
        for i in range(9):
            self.buttons[i].setEnabled(True)
            self.buttons[i].setText("")


    def process(self):
        self.sender().setText(self.switcher.button(self.switcher.checkedId()).text())
        self.sender().setEnabled(False)

        self.switcher.button(0).setEnabled(False)
        self.switcher.button(1).setEnabled(False)
        if self.switcher.checkedId() == 0:
            self.switcher.button(1).setChecked(True)
        else:
            self.switcher.button(0).setChecked(True)

        winner = self.checkWinner()
        if winner != -1:
            self.finish(winner)
            return

        if not self.checkEnabled():
            self.finish()


    def checkWinner(self):
        winPos = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for pos in winPos:
            if self.buttons[pos[0]].text() == self.buttons[pos[1]].text() == self.buttons[pos[2]].text() == "0":
                return 0
            if self.buttons[pos[0]].text() == self.buttons[pos[1]].text() == self.buttons[pos[2]].text() == "X":
                return 1
        return -1


    def checkEnabled(self):
        for i in range(9):
            if self.buttons[i].isEnabled():
                return True
        return False


    def finish(self, winner=-1):
        for i in range(9):
            self.buttons[i].setEnabled(False)
        if winner == 0:
            self.label.setText("Выиграл 0!")
        elif winner == 1:
            self.label.setText("Выиграл X!")
        else:
            self.label.setText("Ничья!")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
