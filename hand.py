import cv2

# 打开默认摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取一帧图像
    ret, frame = cap.read()

    # 显示图像
    cv2.imshow('Video', frame)

    # 等待按键按下，如果按下q键则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()