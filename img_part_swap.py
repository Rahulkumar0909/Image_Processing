import cv2
import numpy

p1=cv2.imread('p1.jpg')
p2=cv2.imread('p2.jpg')
temp=cv2.imread('p1.jpg')

p1=cv2.resize(p1,(300,500))
p2=cv2.resize(p2,(300,500))

cv2.imshow("p1",p1)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("p2",p2)
cv2.waitKey()
cv2.destroyAllWindows()

for i in range(20,170):
    for j in range(70,210):
        temp[i,j]=p2[i,j]
        p2[i,j]=p1[i,j]
        p1[i,j]=temp[i,j]
        
cv2.imshow("p1",p1)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imshow("p2",p2)
cv2.waitKey()
cv2.destroyAllWindows()        
