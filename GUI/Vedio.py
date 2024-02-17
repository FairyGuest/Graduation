# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import cv2
import mediapipe as mp
from Detect.DataClass import Point as P
from Detect.DataClass import Angle as A
from Detect.Calculate import FindAngle
import numpy as np

PointsCoordinators = [i for i in range(1, 19)]

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.t = Worker(0)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 650)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 640, 360))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 30, 40, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(760, 30, 55, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(815, 29, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(760, 50, 55, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(815, 49, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(710, 50, 40, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(760, 70, 55, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(815, 69, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(760, 90, 55, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(815, 89, 16, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(710, 70, 40, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(710, 90, 40, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(760, 130, 55, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(815, 129, 16, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(760, 170, 55, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(815, 169, 16, 16))
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(760, 110, 55, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(815, 109, 16, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(760, 150, 55, 20))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(815, 149, 16, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(710, 110, 40, 20))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(710, 130, 40, 20))
        self.label_25.setObjectName("label_25")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(710, 150, 40, 20))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(710, 170, 40, 20))
        self.label_31.setObjectName("label_31")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.clicked.connect(self.Play)
        self.pushButton.setGeometry(QtCore.QRect(30, 450, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(30, 10, 54, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(710, 10, 54, 20))
        self.label_19.setObjectName("label_19")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "左肘:"))
        self.label_3.setText(_translate("Form", "999"))
        self.label_4.setText(_translate("Form", "°"))
        self.label_5.setText(_translate("Form", "999"))
        self.label_6.setText(_translate("Form", "°"))
        self.label_7.setText(_translate("Form", "左肩:"))
        self.label_8.setText(_translate("Form", "999"))
        self.label_9.setText(_translate("Form", "°"))
        self.label_10.setText(_translate("Form", "999"))
        self.label_11.setText(_translate("Form", "°"))
        self.label_12.setText(_translate("Form", "左腿:"))
        self.label_13.setText(_translate("Form", "左膝:"))
        self.label_14.setText(_translate("Form", "999"))
        self.label_15.setText(_translate("Form", "°"))
        self.label_16.setText(_translate("Form", "999"))
        self.label_17.setText(_translate("Form", "°"))
        self.label_20.setText(_translate("Form", "999"))
        self.label_21.setText(_translate("Form", "°"))
        self.label_22.setText(_translate("Form", "999"))
        self.label_23.setText(_translate("Form", "°"))
        self.label_24.setText(_translate("Form", "右肘:"))
        self.label_25.setText(_translate("Form", "右肩:"))
        self.label_30.setText(_translate("Form", "右腿:"))
        self.label_31.setText(_translate("Form", "右膝:"))
        self.pushButton.setText(_translate("Form", "开始"))
        self.label_18.setText(_translate("Form", "视频"))
        self.label_19.setText(_translate("Form", "角度"))

    def Play(self):
        self.t.finished.connect(self.update_frame)
        self.t.start()

    def update_frame(self, frame):

        # OpenCV通常使用BGR格式，而QImage使用RGB格式，所以需要转换颜色空间
        rgb_frame = cv2.cvtColor(frame[0], cv2.COLOR_BGR2RGB)
        img = QImage(rgb_frame.data, rgb_frame.shape[1], rgb_frame.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(img)
        self.label.setPixmap(pixmap)
        self.label.update()
        self.label_3.setText(str(frame[1]))
        self.label_3.update()
        self.label_5.setText(str(frame[2]))
        self.label_5.update()
        self.label_8.setText(str(frame[3]))
        self.label_8.update()
        self.label_10.setText(str(frame[4]))
        self.label_10.update()
        self.label_14.setText(str(frame[5]))
        self.label_14.update()
        self.label_16.setText(str(frame[6]))
        self.label_16.update()
        self.label_20.setText(str(frame[7]))
        self.label_20.update()
        self.label_22.setText(str(frame[8]))
        self.label_22.update()


class Ui_Form2(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 650)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 640, 360))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(710, 30, 40, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(760, 30, 55, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(815, 29, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(760, 50, 55, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(815, 49, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(710, 50, 40, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(760, 70, 55, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(815, 69, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(760, 90, 55, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(815, 89, 16, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(710, 70, 40, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(710, 90, 40, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(760, 130, 55, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(815, 129, 16, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(760, 170, 55, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(815, 169, 16, 16))
        self.label_17.setObjectName("label_17")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(760, 110, 55, 20))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(815, 109, 16, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(760, 150, 55, 20))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(815, 149, 16, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(710, 110, 40, 20))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(710, 130, 40, 20))
        self.label_25.setObjectName("label_25")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(710, 150, 40, 20))
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(710, 170, 40, 20))
        self.label_31.setObjectName("label_31")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.clicked.connect(self.FilePath)
        self.pushButton.setGeometry(QtCore.QRect(30, 450, 100, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.clicked.connect(self.Play)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 480, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.hide()
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(30, 10, 54, 20))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(710, 10, 54, 20))
        self.label_19.setObjectName("label_19")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(250, 450, 200, 23))
        self.label_32.setObjectName('filepath')

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def FilePath(self):
        self.Filepath = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', './', 'Vedio Files (*.mp4);;ALL Files(*)')
        self.label_32.setText(self.Filepath[0])
        self.t = Worker(self.Filepath[0])
        self.pushButton_2.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "左肘:"))
        self.label_3.setText(_translate("Form", "999"))
        self.label_4.setText(_translate("Form", "°"))
        self.label_5.setText(_translate("Form", "999"))
        self.label_6.setText(_translate("Form", "°"))
        self.label_7.setText(_translate("Form", "左肩:"))
        self.label_8.setText(_translate("Form", "999"))
        self.label_9.setText(_translate("Form", "°"))
        self.label_10.setText(_translate("Form", "999"))
        self.label_11.setText(_translate("Form", "°"))
        self.label_12.setText(_translate("Form", "左腿:"))
        self.label_13.setText(_translate("Form", "左膝:"))
        self.label_14.setText(_translate("Form", "999"))
        self.label_15.setText(_translate("Form", "°"))
        self.label_16.setText(_translate("Form", "999"))
        self.label_17.setText(_translate("Form", "°"))
        self.label_20.setText(_translate("Form", "999"))
        self.label_21.setText(_translate("Form", "°"))
        self.label_22.setText(_translate("Form", "999"))
        self.label_23.setText(_translate("Form", "°"))
        self.label_24.setText(_translate("Form", "右肘:"))
        self.label_25.setText(_translate("Form", "右肩:"))
        self.label_30.setText(_translate("Form", "右腿:"))
        self.label_31.setText(_translate("Form", "右膝:"))
        self.pushButton.setText(_translate("Form", "请选择文件"))
        self.pushButton_2.setText(_translate("Form", "开始"))
        self.label_18.setText(_translate("Form", "视频"))
        self.label_19.setText(_translate("Form", "角度"))
        self.label_32.setText(_translate("Form", "文件路径选择"))

    def Play(self):
        self.t.finished.connect(self.update_frame)
        self.t.start()

    def update_frame(self, frame):

        # OpenCV通常使用BGR格式，而QImage使用RGB格式，所以需要转换颜色空间
        rgb_frame = cv2.cvtColor(frame[0], cv2.COLOR_BGR2RGB)
        img = QImage(rgb_frame.data, rgb_frame.shape[1], rgb_frame.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(img)
        self.label.setPixmap(pixmap)
        self.label.update()
        self.label_3.setText(str(frame[1]))
        self.label_3.update()
        self.label_5.setText(str(frame[2]))
        self.label_5.update()
        self.label_8.setText(str(frame[3]))
        self.label_8.update()
        self.label_10.setText(str(frame[4]))
        self.label_10.update()
        self.label_14.setText(str(frame[5]))
        self.label_14.update()
        self.label_16.setText(str(frame[6]))
        self.label_16.update()
        self.label_20.setText(str(frame[7]))
        self.label_20.update()
        self.label_22.setText(str(frame[8]))
        self.label_22.update()

class Worker(QtCore.QThread):
    # finished = QtCore.pyqtSignal(np.ndarray)
    finished = QtCore.pyqtSignal(list)
    def __init__(self, VedioPath):
        super().__init__()
        self.cap = cv2.VideoCapture(VedioPath)
        # self.cap = cv2.VideoCapture(0)
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils

    def run(self):
        with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break

                    # opencv默认的是bgr格式
                    # 将图像转换为RGB格式，因为MediaPipe需要RGB格式的图像
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # 在图像上检测姿态关键点
                results = pose.process(frame)
                landmarks = results.pose_landmarks
                LandmarksPose = self.mp_pose.PoseLandmark
                # 将图像转换回BGR格式，因为OpenCV显示函数需要BGR格式的图像
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                # 在图像上绘制关键点
                self.mp_drawing.draw_landmarks(frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

                # 帧率
                fps = int(self.cap.get(cv2.CAP_PROP_FPS))
                width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                frame_size = (width, height)
                if landmarks is not None:
                    for i in range(11, 29):
                        PointsCoordinators[i - 11] = P(landmarks.landmark[i].x, landmarks.landmark[i].y,
                                                       frame_size)  # 坐标引入
                else:
                    pass
                # 左半身主要角度指标
                LeftElbow = A('LeftElbow',
                              FindAngle(PointsCoordinators[0], PointsCoordinators[4], PointsCoordinators[2]))
                LeftShoulder = A('LeftShoulder',
                                 FindAngle(PointsCoordinators[2], PointsCoordinators[12], PointsCoordinators[0]))
                LeftHip = A('LeftHip', FindAngle(PointsCoordinators[0], PointsCoordinators[14], PointsCoordinators[12]))
                LeftKnee = A('LeftKnee',
                             FindAngle(PointsCoordinators[12], PointsCoordinators[16], PointsCoordinators[14]))
                # 右半身主要角度指标
                RightElbow = A('RightElbow',
                               FindAngle(PointsCoordinators[1], PointsCoordinators[5], PointsCoordinators[3]))
                RightShoulder = A('RightShoulder',
                                  FindAngle(PointsCoordinators[3], PointsCoordinators[13], PointsCoordinators[1]))
                RightHip = A('RightHip',
                             FindAngle(PointsCoordinators[1], PointsCoordinators[15], PointsCoordinators[13]))
                RightKnee = A('RightKnee',
                              FindAngle(PointsCoordinators[13], PointsCoordinators[17], PointsCoordinators[15]))
                # print(LeftElbow.name, ':', LeftElbow.data)
                # cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                data = [frame, LeftElbow.data, LeftShoulder.data, LeftHip.data, LeftKnee.data, RightElbow.data, RightShoulder.data, RightHip.data, RightKnee.data]
                self.finished.emit(data)
                # 按'q'键退出循环
                # if cv2.waitKey(5) == ord('p'):
                #     cv2.waitKey()
                #     continue
        self.cap.release()  # 释放摄像头资源...

class CameraPage(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(CameraPage, self).__init__()
        self.setupUi(self)

class VedioPage(QtWidgets.QMainWindow, Ui_Form2):
    def __init__(self):
        super(VedioPage, self).__init__()
        self.setupUi(self)