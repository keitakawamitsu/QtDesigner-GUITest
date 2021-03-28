# -*- coding: utf-8 -*-
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from mainWindow import Ui_Dialog

class Test(QDialog):
    def __init__(self,parent=None):
        super(Test, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Test()
    window.show()
    sys.exit(app.exec_())
