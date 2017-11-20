# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 02:38:30 2017

@author: William

"""


# %%
import sys
import lodging_functions
import qt_persistence
from PyQt5 import uic, QtWidgets, QtCore


# %%
QtCore.QCoreApplication.setOrganizationName("Ataraxian")
QtCore.QCoreApplication.setApplicationName("Lodging Calculator")
data = QtCore.QSettings('data.ini', QtCore.QSettings.IniFormat)


# %%
window_creator = "Qt_plugins\\lodging_calculator_qt.ui"
dialog_creator = "Qt_plugins\\constants_dialog.ui"


# %%
Ui_main_window, QtBaseClass = uic.loadUiType(window_creator)
Ui_dialog, QtBaseClass = uic.loadUiType(dialog_creator)


# %%
"""
Load QtDesigner file for the main window
Use to create a Rate_Calculator class
QtBaseClass is thrown out, contains QMainWindow without path

"""


class Rate_Calculator(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_main_window.__init__(self)
        self.setupUi(self)
        self.dialog = Constants_Dialog(self)
        self.constants_action.triggered.connect(self.show_constants_dialog)
        self.calculate_button.clicked.connect(self.calculate_rates)
        qt_persistence.data_load(self, data)

    def show_constants_dialog(self):
        self.dialog.show()

    def calculate_rates(self):
        qt_persistence.data_save(self, data)

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


# %%
"""
Load QtDesigner file for Configuration Dialog
Use to create a Constants_Dialog class
QTBaseClass is thrown out, contains QDialog without path

"""


class Constants_Dialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)
        self.close_button.clicked.connect(self.close_clicked)
        self.save_button.clicked.connect(self.save_clicked)
        qt_persistence.data_load(self, data)

    def close_clicked(self):
        self.close()

    def save_clicked(self):
        qt_persistence.data_save(self, data)
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

    window = Rate_Calculator()
    window.show()
    sys.exit(app.exec_())
