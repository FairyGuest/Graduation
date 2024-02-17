import sys
import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage
import mediapipe as mp
from Detect.DataClass import Point as P
from Detect.DataClass import Angle as A
from Detect.Calculate import FindAngle

PointsCoordinators = [i for i in range(1, 19)]


class VideoDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cap = cv2.VideoCapture('../Sources/2.mp4')  # 打开摄像头
        self.mp_pose = mp.solutions.pose  # 初始化姿态估计器
        self.mp_drawing = mp.solutions.drawing_utils
        # 其他MediaPipe相关的初始化...

    def initUI(self):
        self.setWindowTitle('Video Display')
        self.setGeometry(300, 300, 640, 480)
        self.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        self.show()

    def update_frame(self, frame):
        # OpenCV通常使用BGR格式，而QImage使用RGB格式，所以需要转换颜色空间
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(rgb_frame.data, rgb_frame.shape[1], rgb_frame.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(img)
        self.label.setPixmap(pixmap)
        self.label.update()
        # 在这里添加MediaPipe处理代码...
        # 例如：results = self.mp_pose.process(frame) 进行姿态估计等...
        # 根据需要更新UI...

    def run(self):
        with self.mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            while self.cap.isOpened():
                ret, frame = self.cap.read()
                print(ret)
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
                print(LeftElbow.name, ':', LeftElbow.data)
                cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
                self.update_frame(frame)
                # 按'q'键退出循环
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        self.cap.release()  # 释放摄像头资源...
        sys.exit()  # 退出程序...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    display = VideoDisplay()
    display.run()  # 运行视频显示窗口的主循环
    sys.exit()  # 退出程序...