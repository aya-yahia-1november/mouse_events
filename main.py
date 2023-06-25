import cv2
import numpy as np
"""event=[i for i in dir(cv2) if "EVENT" in i]
print(event)
"""

def click_event (event,x,y,flag,param):
    #  for left button event
    if event==cv2.EVENT_LBUTTONDOWN:
        font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text=str(x)+","+str(y)
        cv2.putText(img,text,(x,y),font,1,(253,245,230),2)
        cv2.imshow("frame",img)
# for right button event
    if event==cv2.EVENT_RBUTTONDOWN:
        blue=img[x,y,0]#blue
        green=img[x,y,1]
        red=img[x,y,2]
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text=str(blue)+","+str(green)+","+str(red)
        cv2.putText(img,text,(x,y),font,1,	(139,0,139),2)
        cv2.imshow("frame",img)

img=cv2.imread("people_set.jpg")
cv2.imshow("frame",img)
cv2.setMouseCallback("frame",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()