"""
:param
    无
:return
    无
功能：调用笔记本摄像头获取视频图片
"""""
import numpy as np
import cv2
from test3 import GetPoint
# from sort.classify_pytorch import initNet, guitest
# initNet()
# 调用笔记本内置摄像头，所以参数为0，如果有其他的摄像头可以调整参数为1，2
cap = cv2.VideoCapture(0)
g = GetPoint()
def cameraTest():
    i0=0
    i1 = 0
    i2 = 0
    i3 = 0

    i4 = 1
    i5 = 0
    i6 = 0
    i7 = 0
    i8 = 0
    # t = tempdiscern.Tempdiscern()
    while True:
        # 从摄像头读取图片
        sucess, img = cap.read()
        # t.discern(img)
        # print(sucess)
        # 转为灰度图片
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #print("hh")
        # 显示摄像头，背景是灰度。
        cv2.imshow("img", img)
        # 保持画面的持续。
        k = cv2.waitKey(1)
        if k == 27:
            # 通过esc键退出摄像
            cv2.destroyAllWindows()
            break
        elif k == ord("s"):
            # 通过s键保存图片，并退出。
            print("sort:")
            cv2.imwrite("sort.jpg", img)
            cv2.imwrite("./testimg/" + str(i4) + ".png", img)
            return guitest("sort.jpg")
        elif k == ord("1"):
            # 通过1键保存第一类图片
            i1 += 1
            print("保存第 一 类图片，第 " + str(i1) + " 张图片")
            cv2.imwrite("./sort/1/" + str(i1) + ".png", img)
            # cv2.imwrite("./sort"+str(i1)+".png",img)
        elif k == ord("0"):
            # 通过1键保存第一类图片
            i0 += 1   #右旋，顺时针
            print("保存第 0 类图片，第 " + str(i0) + " 张图片")
            cv2.imwrite("./sort/0/" + str(i0) + ".png", img)
            # cv2.imwrite("./sort"+str(i1)+".png",img)
        elif k == ord("2"):
            # 通过2键保存第二类图片
            i2 += 1 #左旋
            print("保存第 二 类图片，第 " + str(i2) + " 张图片")
            cv2.imwrite("./sort/2/" + str(i2) + ".png", img)
        elif k == ord("3"):
            # 通过3键保存第三类图片
            i3 += 1
            print("保存第 三 类图片，第 " + str(i3) + " 张图片")
            cv2.imwrite("./sort/3/" + str(i3) + ".png", img)
        elif k == ord("p"):
            # 通过3键保存第三类图片
            i8 += 1
            print("保存待拼接图片，第 " + str(i8) + " 张图片")
            cv2.imwrite("./merge/" + str(i8) + ".png", img)
        elif (k == ord("t")):
            print("temperature")
            cv2.imwrite("temporature.jpg", img)

            # img = cv2.imread(r'/home/robot/Desktop/sensortool/sort/purple/26.png',0)
            img_t = cv2.medianBlur(gray, 5)

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
                return tem[t[0] - 1]
            except AttributeError:
                pass



        elif k == ord("4"):
            i4 += 1
            print("save purple img")
            cv2.imwrite("./sort/purple/" + str(i4) + ".png", img)
        elif k == ord("w"):
            i5 += 1
            cv2.imwrite("./sort/blue/" + str(i5) + ".png", img)
        elif k == ord("e"):
            i6 += 1
            cv2.imwrite("./sort/black/" + str(i6) + ".png", img)
        elif k == ord("r"):
            i7 += 1
            cv2.imwrite("./sort/white/" + str(i7) + ".png", img)

    # 关闭摄像头
    cap.release()


def main():
    cameraTest()


if __name__ == '__main__':
    main()
