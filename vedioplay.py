import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QImage

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Player')
        self.setGeometry(300, 300, 300, 200)

        # 创建布局和控件
        layout = QVBoxLayout()
        self.label = QLabel(self)
        layout.addWidget(self.label)
        self.btn = QPushButton('开始播放', self)
        self.btn.clicked.connect(self.playVideo)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        # 初始化 OpenCV 视频捕获对象
        self.cap = None

    def playVideo(self):
        if self.cap:
            # 停止视频播放（如果正在播放）
            if self.cap.isOpened():
                self.cap.release()
            self.cap = cv2.VideoCapture(0)  # 打开默认摄像头（0索引）
            # 开始视频播放
            ret, frame = self.cap.read()  # 读取帧
            if ret:
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # OpenCV 使用 BGR，而 PyQt 使用 RGB，所以转换颜色格式
                img = QImage(img.data, img.shape[1], img.shape[0],
                             QImage.Format_RGB888)  # 将 OpenCV 的 numpy array 转换为 QImage
                self.label.setPixmap(QPixmap.fromImage(img))  # 在 QLabel 中显示视频帧
                self.label.resize(img.width(), img.height())  # 调整 QLabel 大小以适应视频帧的大小
            else:
                print("无法获取视频帧")
        else:
            print("请选择视频文件或摄像头")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())