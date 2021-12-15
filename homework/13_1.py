import sys
from for_13 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.run)
        self.do_paint = False

    def run(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def xs(self, x):
        return x + 350

    def ys(self, y):
        return 350 - y

    def draw(self, qp):
        for i in range(int(self.lineEdit_n.text())):
            current_x = round(-int(self.lineEdit_side.text()) // 2 * float(self.lineEdit_coeff.text()) ** i)
            current_y = round(-int(self.lineEdit_side.text()) // 2 * float(self.lineEdit_coeff.text()) ** i)
            qp.drawLine(self.xs(current_x), self.ys(current_y), self.xs(current_x), self.ys(-current_y))
            qp.drawLine(self.xs(current_x), self.ys(-current_y), self.xs(-current_x), self.ys(-current_y))
            qp.drawLine(self.xs(-current_x), self.ys(-current_y), self.xs(-current_x), self.ys(current_y))
            qp.drawLine(self.xs(-current_x), self.ys(current_y), self.xs(current_x), self.ys(current_y))


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())









