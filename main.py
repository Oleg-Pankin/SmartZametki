from PyQt5 import QtWidgets, QtCore
import ui_main
import sys
import json


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        with open("note.json", "r") as file:
            json.load(data, read_file)
        with open('note.json', 'a') as file:
            json.dumbs


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = mywindow()
    window.show()
    sys.exit(app.exec())