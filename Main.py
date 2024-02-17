from GUI import first_page
from GUI import Vedio
from GUI import Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


app = QtWidgets.QApplication(sys.argv)
controller = Controller.Controller()
controller.show_login()
sys.exit(app.exec_())