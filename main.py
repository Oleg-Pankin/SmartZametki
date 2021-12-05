from PyQt5 import QtWidgets, QtCore
import ui_main
import sys
import json


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)
    def add_note():
        with open('note.json', 'r') as file:
            data = json.load(data,file)
            print(data)
    def show_note():
        name = list_notes.selectedItems()[0].text()
        field_text.setText(notes[name]['текст'])
        list_tags.clear()
        list_tags.addItems(notes[name]['теги'])
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = mywindow()
    window.show()
    sys.exit(app.exec())