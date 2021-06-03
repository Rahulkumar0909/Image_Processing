import cv2
import numpy

cn = numpy.zeros((500,700))

#pocket=cv2.rectangle(cn,(305,300),(395,360),[200,255,100],5)
face=cv2.circle(cn, (350,150), 60, [255,255,250],5)
body=cv2.circle(cn, (350,305), 95, [255,255,255],5)
ear_r=cv2.circle(cn, (280,100), 20, [255,255,255],5)
ear_l=cv2.circle(cn, (420,100), 20, [255,255,255],5)
hand_r=cv2.circle(cn, (250,230), 30, [255,255,255],5)
hand_l=cv2.circle(cn, (450,230), 30, [255,255,255],5)
leg_r=cv2.circle(cn, (238,360), 30, [255,255,255],5)
leg_l=cv2.circle(cn, (462,360), 30, [255,255,255],5)
eye_r=cv2.circle(cn, (325,135), 3, [255,255,255],10)
eye_l=cv2.circle(cn, (375,135), 3, [255,255,255],10)
nose=cv2.circle(cn, (350,160), 2, [255,255,255],10)

cv2.imshow("Teddy",cn)
cv2.waitKey()
cv2.destroyAllWindows()

#Save Digital Teady
cv2.imwrite("Digital_teddy.jpg",cn)
