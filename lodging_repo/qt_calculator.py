# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 02:38:30 2017

@author: William

"""

# %%
import inspect
import sys

from PyQt5 import uic, QtWidgets, QtCore

import lodging_functions
import qt_persistence

# %%
# noinspection SpellCheckingInspection
QtCore.QCoreApplication.setOrganizationName("Ataraxian")
QtCore.QCoreApplication.setApplicationName("Lodging Calculator")
data = QtCore.QSettings('data.ini', QtCore.QSettings.IniFormat)

# %%
window_creator = "Qt_plugins\\lodging_calculator_qt.ui"
dialog_creator = "Qt_plugins\\constants_dialog.ui"

# %%
Ui_main_window, QtBaseClass = uic.loadUiType(window_creator)
# noinspection PyRedeclaration
Ui_dialog, QtBaseClass = uic.loadUiType(dialog_creator)


# %%
def calculate_values(name, settings):
    value = settings.value(name, type=float)
    sales = settings.value('sales_tax_edit', type=float) / 100
    lodging = settings.value('lodging_tax_edit', type=float)
    # noinspection PyUnusedLocal
    aaa_discount = settings.value('aaa_discount_edit', type=float) / 100
    if name == "rack_rate_edit":
        # noinspection PyPep8
        settings.setValue('rack_total_edit', lodging_functions.make_currency_pretty(
                lodging_functions.add_tax(rate=value, sales_tax=sales, lodging_tax=lodging)))


# %%
"""
Load QtDesigner file for the main window
Use to create a Rate_Calculator class
QtBaseClass is thrown out, contains QMainWindow without path

"""


class RateCalculator(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_main_window.__init__(self)
        self.setupUi(self)
        self.dialog = ConstantsDialog(self)
        self.calculate_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.constants_action.triggered.connect(self.show_constants_dialog)
        self.calculate_button.clicked.connect(self.calculate_clicked)
        self.clear_button.clicked.connect(self.clear_line_edits)
        qt_persistence.gui_load(self, data)

    def show_constants_dialog(self):
        self.dialog.show()

    def calculate_clicked(self):
        qt_persistence.gui_save(self, data)
        if isinstance(QtWidgets.QApplication.focusWidget(), QtWidgets.QLineEdit):
            name = QtWidgets.QApplication.focusWidget().objectName()
            calculate_values(name, data)
            qt_persistence.gui_load(self, data)

    def clear_line_edits(self):
        for name, obj in inspect.getmembers(self):
            if isinstance(obj, QtWidgets.QLineEdit):
                obj.clear()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()

        if e.key() == QtCore.Qt.Key_Delete:
            self.clear_line_edits()

        if e.key() == QtCore.Qt.Key_Enter:
            self.calculate_clicked()


# %%
"""
Load QtDesigner file for Configuration Dialog
Use to create a Constants_Dialog class
QTBaseClass is thrown out, contains QDialog without path

"""


# noinspection PyUnusedLocal
class ConstantsDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)
        self.close_button.clicked.connect(self.close_clicked)
        self.save_button.clicked.connect(self.save_clicked)
        qt_persistence.gui_load(self, data)

    def close_clicked(self):
        self.close()

    def save_clicked(self):
        qt_persistence.gui_save(self, data)
        self.close()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


# %%
# Workaround Qt main loop for Spyder development
# Prevent segfault from running 2 instances of PyQt at once
if __name__ == "__main__":

    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)

    else:
        app = QtWidgets.QApplication.instance()

    window = RateCalculator()
    window.show()
    sys.exit(app.exec_())
