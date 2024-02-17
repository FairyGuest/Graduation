# This is a sample example of Mediapipe--live stream
import cv2
import mediapipe as mp
import time
from Detect.DataClass import Point as P
from Detect.DataClass import Angle as A
from Detect.Calculate import FindAngle

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

PointsCoordinators = [i for i in range(1, 19)]

# 加载视频文件或打开摄像头
  # cap = cv2.VideoCapture(0)  # real-time : 29fps
cap = cv2.VideoCapture('./Sources/2.mp4')  # video : 30fps
frame_count = 0

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    start_time = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        if not ret:
            break

            # opencv默认的是bgr格式
            # 将图像转换为RGB格式，因为MediaPipe需要RGB格式的图像
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 在图像上检测姿态关键点
        results = pose.process(frame)
        landmarks = results.pose_landmarks
        LandmarksPose = mp_pose.PoseLandmark
        # 将图像转换回BGR格式，因为OpenCV显示函数需要BGR格式的图像
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # 在图像上绘制关键点
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # 帧率
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        frame_size = (width, height)
        if landmarks is not None:
            for i in range(11,29):
                PointsCoordinators[i-11]=P(landmarks.landmark[i].x, landmarks.landmark[i].y, frame_size)  # 坐标引入
        else:
            pass
        # 左半身主要角度指标
        LeftElbow = A('LeftElbow', FindAngle(PointsCoordinators[0], PointsCoordinators[4], PointsCoordinators[2]))
        LeftShoulder = A('LeftShoulder', FindAngle(PointsCoordinators[2], PointsCoordinators[12], PointsCoordinators[0]))
        LeftHip = A('LeftHip', FindAngle(PointsCoordinators[0], PointsCoordinators[14], PointsCoordinators[12]))
        LeftKnee = A('LeftKnee', FindAngle(PointsCoordinators[12], PointsCoordinators[16], PointsCoordinators[14]))
        # 右半身主要角度指标
        RightElbow = A('RightElbow', FindAngle(PointsCoordinators[1], PointsCoordinators[5], PointsCoordinators[3]))
        RightShoulder = A('RightShoulder',
                         FindAngle(PointsCoordinators[3], PointsCoordinators[13], PointsCoordinators[1]))
        RightHip = A('RightHip', FindAngle(PointsCoordinators[1], PointsCoordinators[15], PointsCoordinators[13]))
        RightKnee = A('RightKnee', FindAngle(PointsCoordinators[13], PointsCoordinators[17], PointsCoordinators[15]))
        print(LeftElbow.name, ':', LeftElbow.data)
        cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        cv2.imshow('MediaPipe Pose', frame)
        # 按'q'键退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # 释放资源和关闭窗口
cap.release()
cv2.destroyAllWindows()