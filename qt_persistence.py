# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 01:20:00 2017

@author: William

Module with functions to save & restore qt widget values
"""

# %%
import sys
from PyQt5 import QtWidgets, QtCore
import inspect
import distutils


# %%
def data_save(ui, settings):
    """
    Save "ui" controls and values to registry "settings"
    currently handles QComboBox, QLineEdit, QCheckBox,
    QRadioButton, QSpinBox, QSlider, & QListWidget

    Parameters
    ----------
    ui: object
        A QMainWindow object

    settings: object
        A QSettings object

    """
    # Save geometry
    settings.setValue('size', ui.size())
    settings.setValue('pos', ui.pos())

    #for child in ui.children():  # works like getmembers, but because it traverses the hierarachy, you would have to call guisave recursively to traverse down the tree

    for name, obj in inspect.getmembers(ui):
        #if type(obj) is QComboBox:  # this works similar to isinstance, but missed some field... not sure why?
        if isinstance(obj, QtWidgets.QComboBox):
            name = obj.objectName()      # get combobox name
            index = obj.currentIndex()    # get current index from combobox
            text = obj.itemText(index)   # get the text for current index
            settings.setValue(name, text)   # save combobox selection to registry

        if isinstance(obj, QtWidgets.QLineEdit):
            name = obj.objectName()
            value = obj.text()
            settings.setValue(name, value)    # save ui values, so they can be restored next time

        if isinstance(obj, QtWidgets.QCheckBox):
            name = obj.objectName()
            state = obj.isChecked()
            settings.setValue(name, state)

        if isinstance(obj, QtWidgets.QRadioButton):
            name = obj.objectName()
            value = obj.isChecked()
            settings.setValue(name,value)

        if isinstance(obj, QtWidgets.QSpinBox):
            name = obj.objectName()
            value = obj.value()
            settings.setValue(name, value)

        if isinstance(obj,QtWidgets.QSlider):
            name = obj.objectName()
            value = obj.value()
            settings.setValue(name, value)

        if isinstance(obj, QtWidgets.QListWidget):
            name = obj.objectName()
            settings.beginWriteArray(name)
            for i in range(obj.count()):
                settings.setArrayIndex(i)
                settings.setValue(name, obj.item(i).text())
            settings.endArray()

    settings.sync()


# %%
def data_load(ui, settings):
    """
    Restore "ui" controls with values stored in registry "settings"
    currently handles QComboBox, QLineEdit, QCheckBox,
    QRadioButton, QSpinBox, QSlider, & QListWidget

    Parameters
    ----------
    ui: object
        A QMainWindow object

    settings: object
        A QSettings object

    """
    # Restore Geometry
    ui.resize(settings.value('size', QtCore.QSize(293, 282))) # Set Size for first launch
    ui.move(settings.value('pos', QtCore.QPoint(100,100))) # Initial sreen position

    for name, obj in inspect.getmembers(ui):
        if isinstance(obj, QtWidgets.QComboBox):
            index = obj.currentIndex()    # get current region from combobox
            # text = obj.itemText(index)   # get the text for new selected index
            name = obj.objectName()

            value = (settings.value(name))

            if value == "":
                continue

            index = obj.findText(value)   # get the corresponding index for specified string in combobox

            if index == -1:  # add to list if not found
                obj.insertItems(0, [value])
                index = obj.findText(value)
                obj.setCurrentIndex(index)
            else:
                obj.setCurrentIndex(index)   # preselect a combobox value by index    

        if isinstance(obj, QtWidgets.QLineEdit):
            name = obj.objectName()
            value = (settings.value(name))  # get stored value from registry
            obj.setText(value)  # restore lineEditFile

        if isinstance(obj, QtWidgets.QCheckBox):
            name = obj.objectName()
            value = settings.value(name)   # get stored value from registry
            if value is not None:
                obj.setChecked(distutils.util.strtobool(value))  # restore checkbox

        if isinstance(obj, QtWidgets.QRadioButton):
            name = obj.objectName()
            value = settings.value(name)
            if value is not None:
                obj.setChecked(distutils.util.strtobool(value))

        if isinstance(obj, QtWidgets.QSlider):
            name = obj.objectName()
            value = settings.value(name)
            if value is not None:
                obj.setValue(int(value))

        if isinstance(obj, QtWidgets.QSpinBox):
            name = obj.objectName()
            value = settings.value(name)
            if value is not None:
                obj.setValue(int(value))

        if isinstance(obj, QtWidgets.QListWidget):
            name = obj.objectName()
            size = settings.beginReadArray(name)
            for i in range(size):
                settings.setArrayIndex(i)
                value = settings.value(name)
                if value is not None:
                    obj.addItem(value)
            settings.endArray()

    settings.sync()


# %%
if __name__ == "__main__":
    sys.exit()
