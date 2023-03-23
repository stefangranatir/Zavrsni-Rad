import cv2
import numpy as np
import threading
import time
import sys
import BFS as b
from Point import Pt
r=0.65
pocetna=0
krajnja=0
klik=0
wid=2
flag=0
#def resize_image(img):
		#h=img.shape[0]
		#w = img.shape[1]
		#return cv2.resize(img,(int(h),int(w)))

def mouse_event(event,x,y,flags,params):
		global pocetna,krajnja,img,klik,flag
		if event==cv2.EVENT_LBUTTONUP:
			if klik==0:
				cv2.rectangle(img,(x-wid,y-wid),(x+wid,y+wid),(0, 255, 0),-1)
				pocetna = Pt(x,y)
				klik+=1
			elif klik==1:
				cv2.rectangle(img,(x-wid,y-wid),(x+wid,y+wid),(204, 0, 255),-1)
				krajnja = Pt(x,y)
				klik+=1
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

img=cv2.imread("maze_hard.png", cv2.IMREAD_GRAYSCALE)
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
b.bfs(pocetna,krajnja,h,w,img)

print(time.time()-t2)
t.join()

sys.exit(1)
cv2.waitKey(0)
