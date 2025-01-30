import cv2
img=cv2.imread("ironman.webp")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##dst=cv2.threshold(src,threshold,maxValueForThreshold,binary,type)[1]
gaussianImg=cv2.GaussianBlur(img,(41,41),50)
##thresholdImg=cv2.threshold(grayImg,150,255,cv2.THRESH_BINARY)[1]
##cv2.imshow("original",img)
cv2.imshow("threshold.jpg",gaussianImg)
##cv2.imshow("threshold.jpg",thresholdImg)
