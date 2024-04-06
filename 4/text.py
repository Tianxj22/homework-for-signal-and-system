import cv2

img = cv2.imread('/home/tianxj/myCode/homework/xinhaoyuxitong/4/exp1/source img.jpg')
print(img)
cv2.imshow('test', img)
cv2.waitKey()