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
import generated_dialog_qt
import generated_window_qt


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
"""
Load QtDesigner file for the main window
Use to create a Rate_Calculator class
QtBaseClass is thrown out, contains QMainWindow without path

"""


class RateCalculator(QtWidgets.QMainWindow, generated_window_qt.Ui_Rate_Calculator):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        generated_window_qt.Ui_Rate_Calculator.__init__(self)
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

    @staticmethod
    def calculate(key, rack, sales, lodge, aaa, man, soe_dis, soe_com):
        """
        Auxiliary function for set_values.
        Given a key, a default rate, and discount amounts
        Returns a string using the appropriate function from lodging_functions
        in this module, keys are assigned per QLineEdit

        :param key: string
            A string representing the name of the value in the database
        :param rack: number
            The default rate
        :param sales: number
            a percentage sales tax
        :param lodge: number
            a flat rate lodging tax
        :param aaa: number
            a percentage discount
        :param man: number
            another percentage discount
        :param soe_dis: number
            another percentage discount
        :param soe_com: number
            another percentage discount
        :return: string
            a string of pretty printed local currency
        """

        if key == "rack_rate_edit":
            entry = rack

        if key == "rack_total_edit":
            entry = lodging_functions.add_tax(rack, sales, lodge)

        if key == "aaa_rate_edit":
            entry = lodging_functions.apply_discount(rack, aaa)

        if key == "aaa_total_edit":
            entry = lodging_functions.add_tax(lodging_functions.apply_discount(rack, aaa), sales, lodge)

        if key == "lbms_rate_edit":
            entry = lodging_functions.apply_discount(rack, man)

        if key == "lbms_total_edit":
            entry = lodging_functions.add_tax(lodging_functions.apply_discount(rack, man), sales, lodge)

        if key == "soe_rate_edit":
            entry = lodging_functions.expedia_price(rack, soe_dis, soe_com)

        if key == "soe_total_edit":
            entry = lodging_functions.add_tax(lodging_functions.expedia_price(rack, soe_dis, soe_com), sales, lodge)

        return lodging_functions.make_currency_pretty(entry)

    def set_values(self, name, settings):
        """
        Defines a set of constants for the calculate function from the given database,
        Determines the default rate depending on the name of the QLineEdit using lodging_functions,
        For each QLineEdit of the parent class, sets its value in the database to the value returned by calculate
            when given its key-name.

        :param name: string
            The name of a QWidget object of the parent class

        :param settings: QSettings object
            A database managed by QSettings in the operating system's persistent memory

        :return: void

        """
        value = float(settings.value(name, type=str).replace("$", ""))
        sales = float(settings.value('sales_tax_edit', type=str).replace("$", "")) / 100
        lodge = float(settings.value('lodging_tax_edit', type=str).replace("$", ""))
        aaa = float(settings.value('aaa_discount_edit', type=str).replace("$", "")) / 100
        man = float(settings.value('lbms_discount_edit', type=str).replace("$", "")) / 100
        soe_dis = float(settings.value('soe_discount_edit', type=str).replace("$", "")) / 100
        soe_com = float(settings.value('soe_commission_edit', type=str).replace("$", "")) / 100

        if name == "rack_rate_edit":
            rack = value

        if name == "rack_total_edit":
            rack = lodging_functions.remove_tax(value, sales, lodge)

        if name == "aaa_rate_edit":
            rack = lodging_functions.remove_discount(value, aaa)

        if name == "aaa_total_edit":
            rack = lodging_functions.remove_discount(lodging_functions.remove_tax(value, sales, lodge), aaa)

        if name == "lbms_rate_edit":
            rack = lodging_functions.remove_discount(value, man)

        if name == "lbms_total_edit":
            rack = lodging_functions.remove_discount(lodging_functions.remove_tax(value, sales, lodge), man)

        if name == "soe_rate_edit":
            rack = lodging_functions.rate_from_expedia(value, soe_dis, soe_com)

        if name == "soe_total_edit":
            # noinspection PyPep8
            rack = lodging_functions.rate_from_expedia(lodging_functions.remove_tax(value, sales, lodge), soe_dis, soe_com)

        else:
            print("Error! Focus object not known QLineEdit!")

        for key, obj in inspect.getmembers(self):
            if isinstance(obj, QtWidgets.QLineEdit):
                settings.setValue(key, self.calculate(key, rack, sales, lodge, aaa, man, soe_dis, soe_com))

    def calculate_clicked(self):
        qt_persistence.gui_save(self, data)
        if isinstance(QtWidgets.QApplication.focusWidget(), QtWidgets.QLineEdit):
            name = QtWidgets.QApplication.focusWidget().objectName()
            self.set_values(name, data)
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
class ConstantsDialog(QtWidgets.QDialog, generated_dialog_qt.Ui_Constants_Dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        generated_dialog_qt.Ui_Constants_Dialog.__init__(self)
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


# Workaround Qt main loop for Spyder development
# Prevent segfault from running 2 instances of PyQt at once
def main():
    global app
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)

    else:
        app = QtWidgets.QApplication.instance()

    window = RateCalculator()
    window.show()
    sys.exit(app.exec_())


# %%

if __name__ == "__main__":
    main()
