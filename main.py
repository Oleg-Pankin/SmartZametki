import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.resize(1100, 619)
w.move(0, 0)
w.setWindowTitle('Zametki2077')
w.show()
sys.exit(app.exec_())