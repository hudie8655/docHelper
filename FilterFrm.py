# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FilterFrm.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FilterDialog(object):
    def setupUi(self, FilterDialog):
        FilterDialog.setObjectName("FilterDialog")
        FilterDialog.resize(400, 564)
        FilterDialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(FilterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.typelistWidget = QtWidgets.QListWidget(FilterDialog)
        self.typelistWidget.setGeometry(QtCore.QRect(10, 10, 256, 192))
        self.typelistWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.typelistWidget.setObjectName("typelistWidget")
        self.banListWidget = QtWidgets.QListWidget(FilterDialog)
        self.banListWidget.setGeometry(QtCore.QRect(270, 10, 91, 192))
        self.banListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.banListWidget.setObjectName("banListWidget")
        self.fsdateEdit = QtWidgets.QDateEdit(FilterDialog)
        self.fsdateEdit.setGeometry(QtCore.QRect(10, 210, 118, 22))
        self.fsdateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 11, 12), QtCore.QTime(0, 0, 0)))
        self.fsdateEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 14), QtCore.QTime(0, 0, 0)))
        self.fsdateEdit.setMaximumDate(QtCore.QDate(7999, 12, 31))
        self.fsdateEdit.setCalendarPopup(True)
        self.fsdateEdit.setObjectName("fsdateEdit")
        self.fedateEdit = QtWidgets.QDateEdit(FilterDialog)
        self.fedateEdit.setGeometry(QtCore.QRect(150, 210, 118, 22))
        self.fedateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2017, 11, 12), QtCore.QTime(0, 0, 0)))
        self.fedateEdit.setCalendarPopup(True)
        self.fedateEdit.setObjectName("fedateEdit")
        self.pretitlelistWidget = QtWidgets.QListWidget(FilterDialog)
        self.pretitlelistWidget.setGeometry(QtCore.QRect(10, 330, 351, 192))
        self.pretitlelistWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.pretitlelistWidget.setObjectName("pretitlelistWidget")

        self.retranslateUi(FilterDialog)
        self.banListWidget.setCurrentRow(-1)
        self.buttonBox.accepted.connect(FilterDialog.accept)
        self.buttonBox.rejected.connect(FilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)

    def retranslateUi(self, FilterDialog):
        _translate = QtCore.QCoreApplication.translate
        FilterDialog.setWindowTitle(_translate("FilterDialog", "Dialog"))
        self.pretitlelistWidget.setSortingEnabled(True)

