"""
:param
    无
:return
    无
功能：调用笔记本摄像头获取视频图片
"""""
import numpy as np
import cv2
import time
# import tempdiscern
from sort.classify_pytorch import initNet, guitest
initNet()
# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap = cv2.VideoCapture(1)


def cameraTest():
    i0 = 80  # 空的
    # 3类钥匙
    i1 = 80
    i2 = 80
    i3 = 80
    # 4类勺子
    j1 = 20
    j2 = 0
    j3 = 0
    j4 = 0
    while True:
        # 从摄像头读取图片
        sucess, img = cap.read()
        # t.discern(img)
        # print(sucess)
        # 转为灰度图片
        k = cv2.waitKey(1)
        if k == 27:
            # 通过esc键退出摄像
            cv2.destroyAllWindows()
            break
        elif k == ord("s"):
            # 通过s键保存图片，并退出。
            print("sort:")
            cv2.imwrite("sort.jpg", img)
            return guitest("sort.jpg")
        elif k == ord("0"):
            # 通过1键保存第一类图片
            i0 += 1
            print("保存空图片，第 " + str(i0) + " 张图片")
            cv2.imwrite("./sort/0/" + str(i0) + ".png", img)
        elif k == ord("1"):
            # 通过1键保存第一类图片
            i1 += 1
            print("保存第 一 类钥匙图片，第 " + str(i1) + " 张图片")
            cv2.imwrite("./sort/1/" + str(i1) + ".png", img)

        elif k == ord("2"):
            # 通过2键保存第二类图片
            i2 += 1
            print("保存第 二 类钥匙图片，第 " + str(i2) + " 张图片")
            cv2.imwrite("./sort/2/" + str(i2) + ".png", img)
        elif k == ord("3"):
            # 通过3键保存第三类图片
            i3 += 1
            print("保存第 三 类钥匙图片，第 " + str(i3) + " 张图片")
            cv2.imwrite("./sort/3/" + str(i3) + ".png", img)
        elif k == ord("q"):
            # 通过q键保存第一类勺子图片
            j1 += 1
            print("保存第 一 类勺子图片，第 " + str(j1) + " 张图片")
            cv2.imwrite("./sort/4/" + str(i3) + ".png", img)
        elif k == ord("w"):
            # 通过w键保存保存第 二 类勺子图片
            j2 += 1
            print("保存第 二 类勺子图片，第 " + str(j2) + " 张图片")
            cv2.imwrite("./sort/5/" + str(i3) + ".png", img)
        elif k == ord("e"):
            # 通过e键保存第三类勺子图片
            j3 += 1
            print("保存第 三 类勺子图片，第 " + str(j1) + " 张图片")
            cv2.imwrite("./sort/6/" + str(i3) + ".png", img)
        elif k == ord("r"):
            # 通过r键保存第 四 类勺子图片
            j4 += 1
            print("保存第 四 类勺子图片，第 " + str(j4) + " 张图片")
            cv2.imwrite("./sort/7/" + str(j4) + ".png", img)
            # cv2.imwrite("./sort"+str(i1)+".png",img)
        elif k == ord("v"):
            # 通过r键保存第 四 类勺子图片
            for i in range(100):
                cv2.imwrite("./sort/video/" + str(i) + ".png", img)
                time.sleep(100)
        gray = cv2.cvtColor(img, 1)
        # 显示摄像头，背景是灰度。
        # cv2.imshow("img", gray)
        cv2.imshow("img", img)
        # 保持画面的持续。
        k = cv2.waitKey(1)

    # 关闭摄像头
    cap.release()


def main():
    cameraTest()


if __name__ == '__main__':
    main()
