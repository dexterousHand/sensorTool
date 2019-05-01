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
from sort.classify_pytorch import initNet, guitest
from getAngle import getA
# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap = cv2.VideoCapture(1)
from sort.test3 import GetPoint
initNet()
g = GetPoint()

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
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # t.discern(img)
        # print(sucess)
        # 转为灰度图片
        cv2.imshow("img", img)
        k = cv2.waitKey(1)
        if k == 27:
            # 通过esc键退出摄像
            cv2.destroyAllWindows()
            break
        elif k == ord("s"):
            # 通过s键保存图片，并退出。
            print("sort:")
            cv2.imwrite("sort.jpg", img)
            return (guitest("sort.jpg"),"sort")
        elif k == ord("0"):
            # 通过1键保存第一类图片
            i0 += 1
            print("保存第 0 类图片，第 " + str(i0) + " 张图片")
            cv2.imwrite("./sort/0/" + str(i0) + ".png", img)
        elif k == ord("1"):
            return (1,"sort")

        elif k == ord("2"):
            return (2,"sort")

        elif k == ord("3"):
            return (3,"sort")

        elif k == ord("4"):
            return (4,"sort")
        
        elif k == ord("a"):
            print("measure angle")
            cv2.imwrite("angle.jpg", img)
            img0=cv2.imread("angle.jpg",0)
            print(img0)
            return (getA(img0),"angle")
        elif k == ord("q"):
            # 通过q键保存第一类勺子图片
            j1 += 1
            print("保存第 一 类勺子图片，第 " + str(j1) + " 张图片")
            cv2.imwrite("./sort/4/" + str(i3) + ".png", img)
        elif (k == ord("t")):
            print("temperature")
            cv2.imwrite("temporature.jpg", img)

            # img = cv2.imread(r'/home/robot/Desktop/sensortool/sort/purple/26.png',0)
            img_t = cv2.medianBlur(gray, 5)
            print(img_t.shape)


            circles = cv2.HoughCircles(img_t, cv2.HOUGH_GRADIENT, 1, 20,
                                       param1=50, param2=30, minRadius=5, maxRadius=15)
            try:
                circles = np.uint16(np.around(circles))
                colors = []
                # print(circles[0,:])
                for i in circles[0, :]:
                    colors.append(img[i[1], i[0]])
                    pass
                # print(colors)
                color = np.mean(colors, axis=0)
                # print(color)
                t = g.svc.predict([color]) # t = 1,2,3,4
                print(t[0])
                tem = ["black", "blue", "white", "purple"]
                print(tem[t[0] - 1])
                return (t[0],"color")
            except AttributeError:
                pass

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
        # 显示摄像头，背景是灰度。
        cv2.imshow("img", img)
        # 保持画面的持续。
        k = cv2.waitKey(1)

    # 关闭摄像头
    cap.release()


def main():
    cameraTest()


if __name__ == '__main__':
    main()
