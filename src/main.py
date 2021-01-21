# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile, QIODevice
from PySide6.QtUiTools import QUiLoader
from ui_calculator import Ui_Calculator
from operation import Operation


class Calculator(QMainWindow):
    """The calculator window"""

    def __init__(self):
        """Initialise the calculator window"""
        super(Calculator, self).__init__()
        self.current_input = ""
        self.previous_number = None
        self.operation = Operation.EQUALS
        self.load_ui()
        self.connect_buttons()
        self.reset_current = False
        self.update_input()

    def load_ui(self):
        """Load the calculator UI"""
        self.ui = Ui_Calculator()
        self.ui.setupUi(self)

    def connect_buttons(self):
        """Connect buttons from UI to methods"""
        # Connect number buttons
        self.ui.btn_number_0.clicked.connect(lambda: self.add_number(0))
        self.ui.btn_number_1.clicked.connect(lambda: self.add_number(1))
        self.ui.btn_number_2.clicked.connect(lambda: self.add_number(2))
        self.ui.btn_number_3.clicked.connect(lambda: self.add_number(3))
        self.ui.btn_number_4.clicked.connect(lambda: self.add_number(4))
        self.ui.btn_number_5.clicked.connect(lambda: self.add_number(5))
        self.ui.btn_number_6.clicked.connect(lambda: self.add_number(6))
        self.ui.btn_number_7.clicked.connect(lambda: self.add_number(7))
        self.ui.btn_number_8.clicked.connect(lambda: self.add_number(8))
        self.ui.btn_number_9.clicked.connect(lambda: self.add_number(9))
        self.ui.btn_period.clicked.connect(self.period)
        # Connect symbols
        self.ui.btn_plus.clicked.connect(lambda:
            self.perform_operation(Operation.ADD))
        self.ui.btn_subtract.clicked.connect(lambda:
            self.perform_operation(Operation.SUBTRACT))
        self.ui.btn_multiply.clicked.connect(lambda:
            self.perform_operation(Operation.MULTIPLY))
        self.ui.btn_divide.clicked.connect(lambda:
            self.perform_operation(Operation.DIVIDE))
        self.ui.btn_equals.clicked.connect(self.equals)
        # Connect Misc buttons
        self.ui.btn_clear.clicked.connect(self.clear)
        self.ui.btn_backspace.clicked.connect(self.backspace)

    def add_number(self, number):
        """Add a number to the current input"""
        if self.reset_current:
            self.current_input = ""
            self.reset_current = False
        self.current_input += str(number)
        self.update_input()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_0:
            self.add_number(0)
        elif event.key() == QtCore.Qt.Key_1:
            self.add_number(1)
        elif event.key() == QtCore.Qt.Key_2:
            self.add_number(2)
        elif event.key() == QtCore.Qt.Key_3:
            self.add_number(3)
        elif event.key() == QtCore.Qt.Key_4:
            self.add_number(4)
        elif event.key() == QtCore.Qt.Key_5:
            self.add_number(5)
        elif event.key() == QtCore.Qt.Key_6:
            self.add_number(6)
        elif event.key() == QtCore.Qt.Key_7:
            self.add_number(7)
        elif event.key() == QtCore.Qt.Key_8:
            self.add_number(8)
        elif event.key() == QtCore.Qt.Key_9:
            self.add_number(9)
        elif event.key() == QtCore.Qt.Key_Period:
            self.period()
        elif event.key() == QtCore.Qt.Key_Slash:
            self.perform_operation(Operation.DIVIDE)
        elif event.key() == QtCore.Qt.Key_Plus:
            self.perform_operation(Operation.ADD)
        elif event.key() == QtCore.Qt.Key_Asterisk:
            self.perform_operation(Operation.MULTIPLY)
        elif event.key() == QtCore.Qt.Key_Minus:
            self.perform_operation(Operation.SUBTRACT)
        elif event.key() in [QtCore.Qt.Key_Equal, QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return]:
            self.equals()
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.backspace()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.clear()

    def perform_operation(self, operation):
        """Perform a generic operation excluding equals"""
        # Perform operation when the equals button is not pressed
        if self.previous_number is not None and not self.current_input == "":
            self.previous_number = self.perform_maths(self.previous_number, self.current_input, operation)
            self.current_input = ""
        elif not self.current_input == "":
            self.previous_number = float(self.current_input)
            self.current_input = ""
        elif self.previous_number is None:
            self.previous_number = 0;
        self.operation = operation
        self.update_input()

    def perform_maths(self, previous_number, current_input, operation):
        if operation == Operation.MULTIPLY:
            return self.previous_number * float(self.current_input)
        elif operation == Operation.ADD:
            return self.previous_number + float(self.current_input)
        elif operation == Operation.SUBTRACT:
            return self.previous_number - float(self.current_input)
        elif operation == Operation.DIVIDE:
            return self.previous_number / float(self.current_input)

    def update_input(self):
        """Update the input labels"""
        operation_to_string = { Operation.MULTIPLY: "×", Operation.ADD: "+",
                                Operation.SUBTRACT: "-", Operation.DIVIDE: "÷" }
        if self.current_input == "":
            self.ui.lbl_main_input.setText("0")
        else:
            self.ui.lbl_main_input.setText(self.current_input)
        if not self.operation == Operation.EQUALS:
            self.ui.lbl_past_input.setText(self.simplify_number(self.previous_number) + operation_to_string[self.operation])
        else:
            self.ui.lbl_past_input.setText("")

    def equals(self):
        """Perform the operation for the equals button"""
        if self.previous_number is not None:
            self.current_input = self.simplify_number(self.perform_maths(self.previous_number, self.current_input, self.operation))
        elif self.current_input == "":
            self.current_input = "0"
        self.operation = Operation.EQUALS
        self.previous_number = None
        self.update_input()
        self.reset_current = True

    def simplify_number(self, floating_number):
        return str(int(float(floating_number))) if float(floating_number).is_integer() else str(floating_number)

    def clear(self):
        """Clears the calculator inputs"""
        self.operation = Operation.EQUALS
        self.previous_number = None
        self.current_input = ""
        self.update_input()

    def period(self):
        """Performs the function of the period"""
        if self.current_input == "":
            self.current_input = "0."
        elif not "." in self.current_input:
            self.current_input += "."
        self.update_input()

    def backspace(self):
        """Performs a backspace on the current input"""
        if not self.current_input == "":
            self.current_input = self.current_input[:-1]
            self.update_input()
            self.reset_current = False


if __name__ == "__main__":
    app = QApplication([])
    widget = Calculator()
    widget.show()
    sys.exit(app.exec_())
