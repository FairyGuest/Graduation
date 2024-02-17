import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import *

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)

        self.timer_camera = QtCore.QTimer()
        self.cap = cv2.VideoCapture(0)
        self.CAM_NUM = 0
        self.set_ui()
        self.slot_init()
        self.__flag_work = 0
        self.x = 0
        self.count = 0


    def set_ui(self):
        font = QtGui.QFont()
        font.setFamily('kaiti')
        font.setPointSize(18)
        self.textBrowser = QtWidgets.QLabel('人体姿态检测系统')
        self.textBrowser.setAlignment(Qt.AlignCenter)
        self.textBrowser.setFont(font)

        self.mm_layout = QVBoxLayout()
        self.l_down_widget = QtWidgets.QWidget()
        self.__layout_main = QtWidgets.QHBoxLayout()
        self.__layout_fun_button = QtWidgets.QVBoxLayout()
        self.__layout_data_show = QtWidgets.QPushButton(u'打开相机')

        self.move(500, 500)
        #  信息显示
        self.label_show_camera = QtWidgets.QLabel()
        self.label_move = QtWidgets.QLabel()
        