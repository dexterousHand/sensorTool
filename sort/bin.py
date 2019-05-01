import sys
import cv2
tho=220
if len(sys.argv)>1:
    tho=int(sys.argv[1])
for j in range(4):
    for i in range(380):
        fileName=str(i)+".png"
        img=cv2.imread(fileName,0)
        ret,bi = cv2.threshold(img,tho,255,cv2.THRESH_TOZERO)
        cv2.imwrite(str(j)+"/bin/" + str(i) + '.png', bi)

