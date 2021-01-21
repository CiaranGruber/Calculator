# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(375, 600)
        self.centralwidget = QWidget(Calculator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_Lay = QVBoxLayout()
        self.title_Lay.setObjectName(u"title_Lay")
        self.lbl_title = QLabel(self.centralwidget)
        self.lbl_title.setObjectName(u"lbl_title")
        self.lbl_title.setStyleSheet(u"font: 30pt \"Impact\";\n"
"color: rgb(0, 0, 0)")
        self.lbl_title.setTextFormat(Qt.AutoText)
        self.lbl_title.setScaledContents(False)
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.lbl_title.setWordWrap(False)

        self.title_Lay.addWidget(self.lbl_title)

        self.lbl_past_input = QLabel(self.centralwidget)
        self.lbl_past_input.setObjectName(u"lbl_past_input")
        self.lbl_past_input.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lbl_past_input.setMargin(5)

        self.title_Lay.addWidget(self.lbl_past_input)

        self.lbl_main_input = QLabel(self.centralwidget)
        self.lbl_main_input.setObjectName(u"lbl_main_input")
        self.lbl_main_input.setStyleSheet(u"border-top: 1px solid;\n"
"border-bottom: 1px solid;\n"
"color: black;\n"
"font: 75 28pt \"Source Code Pro\";")
        self.lbl_main_input.setAlignment(Qt.AlignCenter)

        self.title_Lay.addWidget(self.lbl_main_input)

        self.title_Lay.setStretch(0, 5)
        self.title_Lay.setStretch(2, 3)

        self.verticalLayout.addLayout(self.title_Lay)

        self.horizontalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.horizontalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.btn_number_9 = QPushButton(self.centralwidget)
        self.btn_number_9.setObjectName(u"btn_number_9")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_number_9.sizePolicy().hasHeightForWidth())
        self.btn_number_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_9, 0, 2, 1, 1)

        self.btn_subtract = QPushButton(self.centralwidget)
        self.btn_subtract.setObjectName(u"btn_subtract")
        sizePolicy.setHeightForWidth(self.btn_subtract.sizePolicy().hasHeightForWidth())
        self.btn_subtract.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_subtract, 2, 3, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_plus, 5, 3, 1, 1)

        self.btn_number_7 = QPushButton(self.centralwidget)
        self.btn_number_7.setObjectName(u"btn_number_7")
        sizePolicy.setHeightForWidth(self.btn_number_7.sizePolicy().hasHeightForWidth())
        self.btn_number_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_7, 0, 0, 1, 1)

        self.btn_number_0 = QPushButton(self.centralwidget)
        self.btn_number_0.setObjectName(u"btn_number_0")
        sizePolicy.setHeightForWidth(self.btn_number_0.sizePolicy().hasHeightForWidth())
        self.btn_number_0.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_0, 5, 1, 1, 1)

        self.btn_number_5 = QPushButton(self.centralwidget)
        self.btn_number_5.setObjectName(u"btn_number_5")
        sizePolicy.setHeightForWidth(self.btn_number_5.sizePolicy().hasHeightForWidth())
        self.btn_number_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_5, 1, 1, 1, 1)

        self.btn_multiply = QPushButton(self.centralwidget)
        self.btn_multiply.setObjectName(u"btn_multiply")
        sizePolicy.setHeightForWidth(self.btn_multiply.sizePolicy().hasHeightForWidth())
        self.btn_multiply.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_multiply, 1, 3, 1, 1)

        self.btn_number_3 = QPushButton(self.centralwidget)
        self.btn_number_3.setObjectName(u"btn_number_3")
        sizePolicy.setHeightForWidth(self.btn_number_3.sizePolicy().hasHeightForWidth())
        self.btn_number_3.setSizePolicy(sizePolicy)
        self.btn_number_3.setStyleSheet(u"height: 40px;")

        self.gridLayout.addWidget(self.btn_number_3, 2, 2, 1, 1)

        self.btn_number_2 = QPushButton(self.centralwidget)
        self.btn_number_2.setObjectName(u"btn_number_2")
        sizePolicy.setHeightForWidth(self.btn_number_2.sizePolicy().hasHeightForWidth())
        self.btn_number_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_2, 2, 1, 1, 1)

        self.btn_divide = QPushButton(self.centralwidget)
        self.btn_divide.setObjectName(u"btn_divide")
        sizePolicy.setHeightForWidth(self.btn_divide.sizePolicy().hasHeightForWidth())
        self.btn_divide.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn_number_4 = QPushButton(self.centralwidget)
        self.btn_number_4.setObjectName(u"btn_number_4")
        sizePolicy.setHeightForWidth(self.btn_number_4.sizePolicy().hasHeightForWidth())
        self.btn_number_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_4, 1, 0, 1, 1)

        self.btn_number_1 = QPushButton(self.centralwidget)
        self.btn_number_1.setObjectName(u"btn_number_1")
        sizePolicy.setHeightForWidth(self.btn_number_1.sizePolicy().hasHeightForWidth())
        self.btn_number_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_1, 2, 0, 1, 1)

        self.btn_number_6 = QPushButton(self.centralwidget)
        self.btn_number_6.setObjectName(u"btn_number_6")
        sizePolicy.setHeightForWidth(self.btn_number_6.sizePolicy().hasHeightForWidth())
        self.btn_number_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_6, 1, 2, 1, 1)

        self.btn_number_8 = QPushButton(self.centralwidget)
        self.btn_number_8.setObjectName(u"btn_number_8")
        sizePolicy.setHeightForWidth(self.btn_number_8.sizePolicy().hasHeightForWidth())
        self.btn_number_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_number_8, 0, 1, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_clear, 5, 0, 1, 1)

        self.btn_period = QPushButton(self.centralwidget)
        self.btn_period.setObjectName(u"btn_period")
        sizePolicy.setHeightForWidth(self.btn_period.sizePolicy().hasHeightForWidth())
        self.btn_period.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_period, 5, 2, 1, 1)

        self.btn_equals = QPushButton(self.centralwidget)
        self.btn_equals.setObjectName(u"btn_equals")
        sizePolicy.setHeightForWidth(self.btn_equals.sizePolicy().hasHeightForWidth())
        self.btn_equals.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_equals, 6, 0, 1, 3)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.btn_backspace, 6, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 7)

        self.horizontalLayout.addLayout(self.verticalLayout)

        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Calculator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 375, 25))
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Calculator)
        self.statusbar.setObjectName(u"statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.lbl_title.setText(QCoreApplication.translate("Calculator", u"Calculator", None))
        self.lbl_past_input.setText("")
        self.lbl_main_input.setText("")
        self.btn_number_9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.btn_subtract.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.btn_plus.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.btn_number_7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.btn_number_0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.btn_number_5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.btn_multiply.setText(QCoreApplication.translate("Calculator", u"\u00d7", None))
        self.btn_number_3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.btn_number_2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.btn_divide.setText(QCoreApplication.translate("Calculator", u"\u00f7", None))
        self.btn_number_4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.btn_number_1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.btn_number_6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.btn_number_8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.btn_clear.setText(QCoreApplication.translate("Calculator", u"CE", None))
        self.btn_period.setText(QCoreApplication.translate("Calculator", u".", None))
        self.btn_equals.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.btn_backspace.setText(QCoreApplication.translate("Calculator", u"<-", None))
    # retranslateUi

