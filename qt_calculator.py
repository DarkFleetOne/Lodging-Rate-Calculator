# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 02:38:30 2017

@author: William
"""

# %%
import sys
from PyQt5 import uic, QtWidgets


# %%
window_creator = "C:\\Users\\Will\\Anaconda3\\Library\\bin\\lodging_calculator_qt.ui"
dialog_creator = "C:\\Users\\Will\\Anaconda3\\Library\\bin\\constants_dialog.ui"


# %%
"""
Load QtDesigner file for the main window
Use to create a Rate_Calculator class
QtBaseClass is thrown out, contains QMainWindow without path
"""

Ui_main_window, QtBaseClass = uic.loadUiType(window_creator)


class Rate_Calculator(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_main_window.__init__(self)
        self.setupUi(self)


# %%
"""
Load QtDesigner file for Configuration Dialog
Use to create a Constants_Dialog class
QTBaseClass is thrown out, contains QDialog without path
"""

Ui_dialog, QtBaseClass = uic.loadUiType(dialog_creator)


class Constants_Dialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)


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
