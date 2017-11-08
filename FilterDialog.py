# -*- coding: utf-8 -*-
__author__ = 'user'

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from FilterFrm import Ui_FilterDialog




class FilterDialog(QDialog,Ui_FilterDialog):
    def __init__(self,parent=None):
        super(QDialog,self).__init__(parent)
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = FilterDialog()
    win.show()
    sys.exit(app.exec_())
