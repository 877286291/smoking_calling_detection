import cv2
from ultralytics import YOLO

# load a pretrained model (recommended for training)
model = YOLO(r"E:\PycharmProjects\smoking_calling_detection\runs\detect\train\weights\best.pt")

# 打开视频文件
cap = cv2.VideoCapture(0)

# 设置视频宽度和高度
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    # 读取视频的每一帧
    ret, frame = cap.read()

    if ret:
        results = model.predict(source=frame, save=False, conf=0.3)
        for result in results:
            for box in result.boxes:
                cls = int(box.cls.data)
                if cls == 0:
                    conf = box.conf.item()
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, f"{result.names[cls]}:{conf:.2f}", (x1, y1),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                                cv2.LINE_AA)
        # 显示绘制后的图像
        cv2.imshow('frame', frame)

        # 设置时间间隔
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# 释放摄像头并销毁窗口
cap.release()
