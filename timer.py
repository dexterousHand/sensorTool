import threading
import cv2
import time
global timer
import sys
import os

def shot_img():
    global num
    success, frame = cap.read()
    path = "./sort/2/"
    num += 1
    cv2.imwrite(path + str(num) + '.png', frame)
    print(num)
    if num == 400:
        cap.release()
        cv2.destroyAllWindows()
        os._exit(0)
    threading.Timer(2, shot_img).start()


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
    num = 320
    cap = cv2.VideoCapture(0)
    shot_img()
    threading.Thread(target=showImg).start()
    # shot_img()
    # show.join()
    # timer.join()
