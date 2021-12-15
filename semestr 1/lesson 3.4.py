import csv
import sys
from msilib import Table
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic.properties import QtCore
from pyqt5_plugins.examplebutton import QtWidgets


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI2.ui', self)
        self.loadTable('price_1.csv')
        self.tableWidget.itemChanged.connect(self.calc_all_prices)
        self.pushButton.clicked.connect(self.top_colors)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile,
                                delimiter=';', quotechar='"')
            title = next(reader)
            data = sorted(reader, key=lambda x: int(x[1]), reverse=True)
            # self.tableWidget.setColumnCount(len(title))
            # self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(data):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                row.append(0)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()

    def calc_all_prices(self):
        count = 0
        for i in range(self.tableWidget.rowCount()):
            count += int(self.tableWidget.item(i, 1).text()) * int(self.tableWidget.item(i, 2).text())
        self.lineEdit.setText(str(count))

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def top_colors(self):
        for i in range(5):
            self.color_row(i, QColor(randint(0, 255), randint(0, 255), randint(0, 255)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())