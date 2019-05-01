import cv2
import numpy as np
import sklearn
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.covariance import  EllipticEnvelope
from sklearn.neighbors import LocalOutlierFactor

class GetPoint():
    def __init__(self):

        c = cv2.imread(r"../sort/black/1.png")
        d = cv2.imread(r"../sort/black/2.png")
        e = cv2.imread(r"../sort/black/3.png")
        f = cv2.imread(r"../sort/black/4.png")
        g = cv2.imread(r"../sort/black/5.png")

        b1 = cv2.imread(r"../sort/blue/1.png")
        b2 = cv2.imread(r"../sort/blue/2.png")
        b3 = cv2.imread(r"../sort/blue/3.png")
        b4 = cv2.imread(r"../sort/blue/2nd/9.png")
        b5 = cv2.imread(r"../sort/blue/3nd/18.png")

        w1= cv2.imread(r"../sort/white/4.png")
        w2 = cv2.imread(r"../sort/white/5.png")
        w3 = cv2.imread(r"../sort/white/6.png")
        w4 = cv2.imread(r"../sort/white/2nd/8.png")
        w5 = cv2.imread(r"../sort/white/3rd/23.png")

        p1= cv2.imread(r"../sort/purple/12.png")
        p2= cv2.imread(r"../sort/purple/13.png")
        p3= cv2.imread(r"../sort/purple/14.png")


        blacks = []
        blues = []
        whites = []
        purples = []
        backgrounds = []
        for i in range(4):
            for j in range(4):
                backgrounds.append(c[106 + 3*i,189 + 3*j])
                backgrounds.append(c[243 + 3*i,255 + 3*j])
                backgrounds.append(c[138 + 3*i,120 + 3*j])
                backgrounds.append(c[274 + 3*i,186 + 3*j])

                backgrounds.append(b1[165 + 3*i,81 + 3*j])
                backgrounds.append(b1[278 + 3*i,392 + 3*j])

                backgrounds.append(b5[108 + 3*i,264 + 3*j])
                backgrounds.append(b5[240 + 3*i,123 + 3*j])

                backgrounds.append(b4[229 + 3*i,257 + 3*j])
                backgrounds.append(b4[330 + 3*i,388 + 3*j])
                backgrounds.append(b4[258 + 3*i,194 + 3*j])
                backgrounds.append(b4[324 + 3*i,192 + 3*j])

        for i in range(6):
            for j in range(6):
                blacks.append(c[128 + 34*i,175 + 34*j])
                blacks.append(d[131 + 34*i,170 + 34*j])
                blacks.append(e[131 + 34*i,170 + 34*j])
                blacks.append(f[131 + 34*i,170 + 34*j])
                blacks.append(g[130 + 34*i,175 + 34*j])

                blues.append(b1[128 + 34*i,175 + 34*j])
                blues.append(b2[125 + 34*i,175 + 34*j])
                blues.append(b3[125 + 34*i,174 + 34*j])
                blues.append(b4[154+ 32*i,186 + 32*j])
                blues.append(b5[162+ 34*i,183 + 34*j])

                whites.append(w1[189 + 35*i,213 + 35*j])
                whites.append(w2[125 + 34*i,175 + 34*j])
                whites.append(w3[125 + 34*i,174 + 34*j])
                whites.append(w4[167+ 32*i,194 + 32*j])
                whites.append(w5[174+ 35*i,196 + 35*j])

        for i in range(6):
            for j in range(9):
               purples.append(p1[157 + 32*i,186 + 32*j])
               purples.append(p2[186 + 32*i,152 + 32*j])
               purples.append(p3[187 + 32*i,149 + 32*j])

        #cv2.imshow("black",c)#34 35
        #cv2.waitKey(0)

        blacks = np.array(blacks)
        blues = np.array(blues)
        whites = np.array(whites)
        purples = np.array(purples)
        Y = [1 for _  in range(blacks.shape[0])] +\
            [2 for _  in range(blues.shape[0])] + \
            [3 for _  in range(whites.shape[0])] + \
            [4 for _  in range(purples.shape[0])]
        Y = np.array(Y)
        backgrounds = np.array(backgrounds)
        all = np.concatenate((blacks, blues, whites, purples), axis=0)
        #print("all shape", all.shape)
        #print("y", Y.shape)

        self.svc=svm.SVC(kernel='poly',degree=2,gamma=1,coef0=0.05)

        self.svc.fit(all,Y)

        pre=self.svc.predict(all)
        #print(pre)
        print("temperature initialization is ok")


if __name__ == "__main__":
    g = GetPoint()
    cap=cv2.VideoCapture(0)
    while(True):
        sucess,cimg=cap.read()
        #转为灰度图片
        img=cv2.cvtColor(cimg,cv2.COLOR_BGR2GRAY)
        #cv2.imshow("hh", img)
        #cv2.waitKey(500)


        #img = cv2.imread(r'/home/robot/Desktop/sensortool/sort/purple/26.png',0)
        img = cv2.medianBlur(img,5)

        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                    param1=50,param2=30,minRadius=5,maxRadius=15)
        try:
            circles = np.uint16(np.around(circles))
            colors = []
            #print(circles[0,:])
            for i in circles[0,:]:
                colors.append(cimg[i[1], i[0]])
                pass
            #print(colors)
            color = np.mean(colors, axis=0)
            #print(color)
            print(g.svc.predict([color]))
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

            cv2.imshow('detected circles',cimg)
            cv2.waitKey(200)
        except AttributeError:
            pass