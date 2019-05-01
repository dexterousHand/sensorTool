import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

def detectLine(img):

    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thre = cv2.threshold(img,180,255,cv2.THRESH_BINARY)
    lines = cv2.HoughLines(thre,1,np.pi/180,100)

    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    print(lines[0][0][1]*180/np.pi - 90)
    
    return lines[0][0],img

def getA(img):
    ret, thre = cv2.threshold(img, 180, 255, cv2.THRESH_BINARY)
    lines = cv2.HoughLines(thre, 1, np.pi / 180, 100)
    try:
        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        return lines[0][0][1] * 180 / np.pi - 90
    except TypeError:
        return 0

def getMask(img):
    (l, img0)  = detectLine(img)

    p, c =l
    mask = np.zeros([img.shape[0], img.shape[1]])

    if img.shape[1]*np.cos(c)/2 + img.shape[0]/2*np.sin(c) > p:
        jp = np.array([[x * np.cos(c) + (y - 60) * np.sin(c)
                        for x in range(img.shape[1])] for y in range(img.shape[0])])
        mask[jp > p] = 1
    else:
        jp = np.array([[x * np.cos(c) + (y + 60) * np.sin(c)
                        for x in range(img.shape[1])] for y in range(img.shape[0])])
        mask[jp < p] = 1

    return mask,img0

if __name__ == "__main__":


    for i in range(1,121):
        print(i,":")
        path=str(i)+'.png'
        img=cv2.imread(path,0)
        (mask,img0)=getMask(img)
        path0="mask/"+path
        path1="mask/"+path+"_"
        path2="mask/"+path+"__"
        # prehandle
        ret, img = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO )
        kernel1 = np.ones((3,3),np.uint8)  
        kernel2 = np.ones((2,2),np.uint8)  
        erosion = cv2.erode(img,kernel2,iterations = 1)
        dilated = cv2.dilate(erosion,kernel1)
        # 边缘检测
        Blur = cv2.GaussianBlur(dilated, (3, 3), 0)
        Canny = cv2.Canny(Blur, 50, 150)
        # _______
        img= mask * Canny
        cv2.imwrite(path0,mask*255)

        # cv2.imwrite(path1,img)
        # cv2.imwrite(path2,mask*255)
    
