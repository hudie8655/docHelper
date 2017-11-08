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
        FilterDialog.resize(400, 300)
        FilterDialog.setModal(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(FilterDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.typelistWidget = QtWidgets.QListWidget(FilterDialog)
        self.typelistWidget.setGeometry(QtCore.QRect(50, 10, 256, 192))
        self.typelistWidget.setObjectName("typelistWidget")

        self.retranslateUi(FilterDialog)
        self.buttonBox.accepted.connect(FilterDialog.accept)
        self.buttonBox.rejected.connect(FilterDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)

    def retranslateUi(self, FilterDialog):
        _translate = QtCore.QCoreApplication.translate
        FilterDialog.setWindowTitle(_translate("FilterDialog", "Dialog"))

