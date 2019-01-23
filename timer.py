import threading
import cv2

global timer
import sys
import os

def shot_img():
    global num
    success, frame = cap.read()
    path = "./sort/7/"
    num += 1
    cv2.imwrite(path + str(num) + '.png', frame)
    print(num)
    if num == 200:
        cap.release()
        cv2.destroyAllWindows()
        os._exit(0)
    timer = threading.Timer(1, shot_img)
    timer.start()


def showImg():
    while True:
        success, img = cap.read()
        cv2.imshow("img", img)
        # 保持画面的持续。
        k = cv2.waitKey(1)
        if k == 27:
            # 通过esc键退出摄像
            cv2.destroyAllWindows()
            os._exit(0)


if __name__ == '__main__':
    num = 0
    cap = cv2.VideoCapture(1)
    timer = threading.Timer(3, shot_img)
    show = threading.Thread(target=showImg)
    show.start()
    timer.start()
    show.join()
    timer.join()
