from PyQt5 import QtWidgets, QtCore
import ui_main
import sys
import json


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.list_notes()
        self.ui.notes.itemClicked.connect(self.show_note)
        self.ui.create_note.clicked.connect(self.add_note)
        self.ui.delete_note.clicked.connect(self.del_note)
        #self.ui.save_note.clicked.connect(self.save_note)
    def add_note(self):
        with open('note.json', 'a') as file:
            data = json.dump(file)
    def show_note(self):
        with open('note.json', 'r') as file:
            data = json.load(file)
            self.ui.note.setPlainText(data["Text"])
    def del_note(self):
        with open('note.json', 'a') as file:
            data = json.dump(file)
    def list_notes(self):
        with open('note.json', 'r') as file:
            data = json.load(file)
            print(data)
            self.ui.notes.addItem(data["Name"])
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = mywindow()
    window.show()
    sys.exit(app.exec())