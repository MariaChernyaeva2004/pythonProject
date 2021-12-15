import sys
import pickle
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from list_zadach import Ui_MainWindow
from task_create import Ui_Form_task_create
from task_edit import Ui_Form_task_edit


class TaskSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        try:
            with open('data.txt', 'rb') as f:
                self.data = pickle.load(f)
        except EOFError:
                self.data = []
        self.calendarWidget.clicked.connect(self.calendar_clicked)
        self.pushButton_create.clicked.connect(self.click_create)
        self.pushButton_delete.clicked.connect(self.click_delete)
        self.pushButton_edit.clicked.connect(self.click_edit)

    def calendar_clicked(self, date):
        date = date.toPyDate()
        date_list_task = list(map(lambda x: f'{x[0]}: {x[1]}', filter(lambda t: t[0] == date, self.data)))
        print(date_list_task)
        self.listWidget.clear()
        self.listWidget.addItems(date_list_task)

    def click_create(self):
        self.wnd_create = CreateTaskWindow(self.data)
        self.wnd_create.show()

    def click_delete(self):
        for i in self.data:
            stroka = self.listWidget.currentItem().text().split(': ')
            if str(i[0]) == str(stroka[0]) and str(i[1]) == str(stroka[1]):
                del self.data[self.data.index(i)]
        self.listWidget.clear()
        with open('data.txt', 'wb') as f:
            pickle.dump(self.data, f)

    def click_edit(self):
        self.wnd_edit = EditTaskWindow(self.data, self.listWidget)
        self.wnd_edit.show()



class CreateTaskWindow(QWidget, Ui_Form_task_create):
    def __init__(self, list_tasks):
        super().__init__()
        self.setupUi(self)
        self.pushButton_create.clicked.connect(self.ok)
        self.data = list_tasks
        self.pushButton_cancel.clicked.connect(lambda: self.hide())

    def ok(self):
        description = self.lineEdit_task.text()
        datetime = self.dateTimeEdit.date().toPyDate()
        self.data.append((datetime, description))
        with open('data.txt', 'wb') as f:
            pickle.dump(self.data, f)
        self.hide()

class EditTaskWindow(QWidget, Ui_Form_task_edit):
    def __init__(self, list_tasks, list_widget):
        super().__init__()
        self.setupUi(self)
        self.data = list_tasks
        self.listWidget = list_widget
        self.pushButton_ok.clicked.connect(self.ok)

    def ok(self):
        for i in self.data:
            stroka = self.listWidget.currentItem().text().split(': ')
            if str(i[0]) == str(stroka[0]) and str(i[1]) == str(stroka[1]):
                del self.data[self.data.index(i)]
        self.listWidget.clear()
        with open('data.txt', 'wb') as f:
            pickle.dump(self.data, f)
        description = self.lineEdit_task.text()
        datetime = self.dateTimeEdit.date().toPyDate()
        self.data.append((datetime, description))
        with open('data.txt', 'wb') as f:
            pickle.dump(self.data, f)
        self.hide()


def except_hook(clc, exception, traceback):
    sys.__excepthook__(clc, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    wnd = TaskSystem()
    wnd.show()
    sys.exit(app.exec())

