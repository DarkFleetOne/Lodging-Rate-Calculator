# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 18:57:53 2017

@author: William
"""

# %%
import sys

from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGridLayout, QApplication, QPushButton)


# %%
# noinspection SpellCheckingInspection
class RateCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    # noinspection PyPep8Naming,SpellCheckingInspection
    def initUI(self):
        rate_label = QLabel('Rate')
        total_label = QLabel('Total')
        rack_label = QLabel('RACK')
        aaa_label = QLabel('AAA')
        lbms_label = QLabel('LBMS')
        soe_label = QLabel('SOE')

        rack_rate_edit = QLineEdit()
        rack_total_edit = QLineEdit()

        aaa_rate_edit = QLineEdit()
        aaa_total_edit = QLineEdit()

        # noinspection SpellCheckingInspection
        lbms_rate_edit = QLineEdit()
        lbms_total_edit = QLineEdit()

        soe_rate_edit = QLineEdit()
        soe_total_edit = QLineEdit()

        clear_button = QPushButton('Clear')
        calculate_button = QPushButton('Calculate')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(rate_label, 1, 2)
        grid.addWidget(total_label, 1, 3)
        grid.addWidget(rack_label, 2, 1)
        grid.addWidget(aaa_label, 3, 1)
        grid.addWidget(lbms_label, 4, 1)
        grid.addWidget(soe_label, 5, 1)

        grid.addWidget(rack_rate_edit, 2, 2)
        grid.addWidget(rack_total_edit, 2, 3)

        grid.addWidget(aaa_rate_edit, 3, 2)
        grid.addWidget(aaa_total_edit, 3, 3)

        grid.addWidget(lbms_rate_edit, 4, 2)
        grid.addWidget(lbms_total_edit, 4, 3)

        grid.addWidget(soe_rate_edit, 5, 2)
        grid.addWidget(soe_total_edit, 5, 3)

        grid.addWidget(clear_button, 6, 3)
        grid.addWidget(calculate_button, 6, 4)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Rate Calculator')
        self.show()


# %%
if __name__ == '__main__':
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    window = RateCalculator()
    window.show()
    sys.exit(app.exec_())
