import cv2
from Point import Pt
import threading
import time
import sys
import numpy as np
import math

r=0.65

prvaProizvoljna=0
drugaProizvoljna=0
proUdaljenost=0

prvaKalibracijska=0
drugaKalibracijska=0

klik=0
wid=2
flag=0

cmUpx=0
cmpx=0

def empty():
	pass

cv2.namedWindow("Trackbars")
cv2.resize("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 0,179,empty)


#def resize_image(img):
		#h=img.shape[0]
		#w = img.shape[1]
		#return cv2.resize(img,(int(h),int(w)))

def mouse_event(event,x,y,flags,params):
		global prvaKalibracijska, drugaKalibracijska,img,klik,flag, cmUpx, prvaProizvoljna, drugaProizvoljna, cmpx, proUdaljenost
		if event==cv2.EVENT_LBUTTONUP:
			if klik==0:
				cv2.rectangle(img,(x-wid,y-wid),(x+wid,y+wid),(0, 255, 0),-1)
				prvaKalibracijska = Pt(x,y)
				klik+=1

			elif klik==1:
				cv2.rectangle(img,(x-wid,y-wid),(x+wid,y+wid),(204, 0, 255),-1)
				drugaKalibracijska = Pt(x,y)
				klik+=1
				cmUpx=math.sqrt(((drugaKalibracijska.x-prvaKalibracijska.x)**2)+((drugaKalibracijska.y-prvaKalibracijska.y)**2))
				cmpx=cmUpx/5

			elif klik==2:
				cv2.rectangle(img, (x - wid, y - wid), (x + wid, y + wid), (204, 0, 255), -1)
				prvaProizvoljna=Pt(x,y)
				klik+=1

			elif klik==3:
				cv2.rectangle(img, (x - wid, y - wid), (x + wid, y + wid), (204, 0, 255), -1)
				drugaProizvoljna=Pt(x,y)
				klik+=1
				proUdaljenost=math.sqrt(((drugaProizvoljna.x-prvaProizvoljna.x)**2)+((drugaProizvoljna.y-prvaProizvoljna.y)**2))


				print("udaljenost = ", proUdaljenost/cmpx)
				print(prvaProizvoljna.x, prvaProizvoljna.y)
				print(drugaProizvoljna.x, drugaProizvoljna.y)






		if event==cv2.EVENT_RBUTTONUP:
			flag=1

def disp():
		global img
		cv2.imshow("Maze_solver",img)
		cv2.setMouseCallback('Maze_solver',mouse_event)
		u=0
		while True and flag==0:
			cv2.imshow("Maze_solver",img)
			cv2.waitKey(1)

img=cv2.imread("Testkalibracija2.jpg", cv2.IMREAD_GRAYSCALE)
#img=resize_image(img)
_,img=cv2.threshold(img,120,255,cv2.THRESH_BINARY)
img=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

h=img.shape[0]
w = img.shape[1]

t= threading.Thread(target=disp, args=())
t.start()
while klik<2:
	pass
t2=time.time()
#b.bfs(pocetna,krajnja,h,w,img)

print("x1 = ",prvaKalibracijska.x,"y1= ", prvaKalibracijska.y)
print("x1 = ",drugaKalibracijska.x,"y1= ", drugaKalibracijska.y)
print("udaljenost u px", cmUpx, "1cm = ",cmpx,"piksela", "iznosi :", cmUpx/cmpx," cm")

t.join()



sys.exit(1)
cv2.waitKey(0)
