import colorsys
from Point import Pt
import sys
import threading
import Komunikacija

def isSafe(t_x,t_y,h,w,img,visited):
	return t_x>=0 and t_x<w and t_y>=0 and t_y<h and visited[t_y][t_x]==0 and (img[t_y][t_x][0]!=0 or img[t_y][t_x][1]!=0 or img[t_y][t_x][2]!=0)
def bfs(pocetna,krajnja,h,w,img):
	q=[]
	const=2000
	found=0
	predjene = [[0 for i in range(w)]for j in range(h)]
	parent = [[Pt() for i in range(w)]for j in range(h)]
	q.append(pocetna)
	predjene[pocetna.y][pocetna.x]=1
	x_c=[0,0,1,-1]
	y_c=[1,-1,0,0]
	while len(q)>0:
		temp = q.pop(0)
		if temp==krajnja:
			found=1
			break
		for i in range(4):
			t_x=temp.x+x_c[i]
			t_y=temp.y+y_c[i]
			if isSafe(t_x,t_y,h,w,img,predjene)==True:
				predjene[t_y][t_x]=predjene[temp.y][temp.x]+1
				parent[t_y][t_x]=temp
				q.append(Pt(t_x,t_y))
				img[t_y][t_x]=[170,178,32]
				#img[t_y][t_x]=list(reversed([i * 255 for i in colorsys.hsv_to_rgb(predjene[t_y][t_x] / const, 1, 1)]))
	path=[]
	if found==1:
		i=krajnja
		while i!=pocetna:
			path.append(Pt(i.x,i.y))
			i=parent[i.y][i.x]
		path.append(pocetna)
		path.reverse()
		path.append(krajnja)
		for p in path:
			for i in range(-1,1):
				img[p.y+i][p.x+i]=[255,0,255]
				#print(p.y+i, p.x+i)
		print("Path found")
	else:
		print("Path not found")

	kom = threading.Thread()
	kom.start()
	Komunikacija.testIspis(path)
	kom.join()
