import cv2
import numpy

p1=cv2.imread('p1.jpg')
p2=cv2.imread('p2.jpg')

r1=cv2.rectangle(p1,(0,0),(255,500),[200,255,100],20)
r2=cv2.rectangle(p2,(0,0),(255,500),[100,250,200],20)

p3=numpy.append(r1,r2,axis=1)

cv2.imshow("p3",p3)
cv2.waitKey()
cv2.destroyAllWindows()
