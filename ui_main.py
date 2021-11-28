# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainODxpHX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 791, 593))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.note = QTextEdit(self.layoutWidget)
        self.note.setObjectName(u"note")

        self.gridLayout.addWidget(self.note, 0, 0, 10, 1)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setLayoutDirection(Qt.LeftToRight)
        self.line.setAutoFillBackground(False)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 10, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 3)

        self.notes = QListWidget(self.layoutWidget)
        self.notes.setObjectName(u"notes")

        self.gridLayout.addWidget(self.notes, 1, 2, 1, 4)

        self.create_note = QPushButton(self.layoutWidget)
        self.create_note.setObjectName(u"create_note")

        self.gridLayout.addWidget(self.create_note, 2, 2, 1, 3)

        self.delete_note = QPushButton(self.layoutWidget)
        self.delete_note.setObjectName(u"delete_note")

        self.gridLayout.addWidget(self.delete_note, 2, 5, 1, 1)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 4, 2, 1, 3)

        self.tegs = QListWidget(self.layoutWidget)
        self.tegs.setObjectName(u"tegs")

        self.gridLayout.addWidget(self.tegs, 5, 2, 1, 4)

        self.add_to_note = QPushButton(self.layoutWidget)
        self.add_to_note.setObjectName(u"add_to_note")

        self.gridLayout.addWidget(self.add_to_note, 8, 2, 1, 3)

        self.unpin_from_note = QPushButton(self.layoutWidget)
        self.unpin_from_note.setObjectName(u"unpin_from_note")

        self.gridLayout.addWidget(self.unpin_from_note, 8, 5, 1, 1)

        self.find_teg = QPushButton(self.layoutWidget)
        self.find_teg.setObjectName(u"find_teg")

        self.gridLayout.addWidget(self.find_teg, 9, 2, 1, 4)

        self.save_note = QPushButton(self.layoutWidget)
        self.save_note.setObjectName(u"save_note")

        self.gridLayout.addWidget(self.save_note, 3, 2, 1, 4)

        self.teg_input = QLineEdit(self.layoutWidget)
        self.teg_input.setObjectName(u"teg_input")

        self.gridLayout.addWidget(self.teg_input, 7, 2, 1, 4)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.note.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0437\u0430\u043c\u0435\u0442\u043e\u043a", None))
        self.create_note.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.delete_note.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0435\u0433\u043e\u0432", None))
        self.add_to_note.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a \u0437\u0430\u043c\u0435\u0442\u043a\u0435", None))
        self.unpin_from_note.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u0435\u043f\u0438\u0442\u044c \u043e\u0442 \u0437\u0430\u043c\u0435\u0442\u043a\u0438", None))
        self.find_teg.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043a\u0430\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0443 \u043f\u043e \u0442\u0435\u0433\u0443", None))
        self.save_note.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u0430\u043c\u0435\u0442\u043a\u0443", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u0433:", None))
    # retranslateUi

