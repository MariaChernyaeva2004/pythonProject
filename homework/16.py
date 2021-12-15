import sys
import csv
from for_16 import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QApplication

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lst = []
        self.loadTable('rez.csv')


        school = []
        classes = []
        for i in self.lst:
            school.append(i[0])
            classes.append(i[1])
        school = sorted(list(set(school)))
        classes = sorted(list(set(classes)))
        school.insert(0, 'Все')
        classes.insert(0, 'Все')
        self.comboBox.insertItems(0, school)
        self.comboBox_2.insertItems(0, classes)
        for i in range(len(self.reader)):
            self.lst[i].append(self.reader[i][1])
        self.pushButton.clicked.connect(self.results)
        self.comboBox.currentTextChanged.connect(self.combo)


    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            self.reader = list(csv.reader(csvfile,
                                delimiter=',', quotechar='"'))
            del self.reader[0]
            self.reader = list(map(lambda x: [x[1], x[7]], self.reader))
            self.lst = list(map(lambda x: x[0].split(' '), self.reader))
            self.lst = list(map(lambda x: [x[1], x[2], x[3]], self.lst))
            self.reader = list(map(lambda x: [x[0][8:-2], x[1]], self.reader))
            for i, row in enumerate(self.reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        # print(self.reader)
        self.tableWidget.resizeColumnsToContents()

        # print(self.lst)

    def combo(self, text):
        if text == 'Все':
            return
        new_combo = []
        for i in range(len(self.lst)):
            if self.lst[i][0] == text:
                new_combo.append(self.lst[i][1])
                print(new_combo)
        new_combo = sorted(list(set(new_combo)))
        self.comboBox_2.clear()
        self.comboBox_2.insertItem(0, 'Все')
        self.comboBox_2.addItems(new_combo)

    def results(self):
        self.tableWidget.setRowCount(0)
        res = []

        for i in range(len(self.lst)):

            if self.comboBox.currentText() == 'Все' and self.comboBox_2.currentText() == 'Все':
                res.append([self.lst[i][2], self.lst[i][3]])
                # print(res)
            elif self.comboBox.currentText() == 'Все':
                if self.lst[i][1] == self.comboBox_2.currentText():
                    res.append([self.lst[i][2], self.lst[i][3]])

            elif self.comboBox_2.currentText() == 'Все':

                if self.lst[i][0] == self.comboBox.currentText():
                    res.append([self.lst[i][2], self.lst[i][3]])


            elif self.lst[i][0] == self.comboBox.currentText() and self.lst[i][1] == self.comboBox_2.currentText():
                res.append([self.lst[i][2], self.lst[i][3]])
        #print(res)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())

