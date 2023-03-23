from Point import Pt
import time
import threading

def pretvorba(path):
    ins=[]
    f=0#forward
    l=0#left
    r=0#right
    b=0#back
    Xval=path[0].x
    Yval=path[0].y
    print(path[0].x, path[0].y)
    for p in range(len(path)-1):

        #ide napred
        if(path[p+1].x==Xval)and(path[p+1].y == Yval+1):
            if(l!=0):
                ins.append("l"+str(l))
                print("l1", l)
                l=0
            if (r != 0):
                ins.append("r" + str(r))
                print("r1", r)
                r = 0
            if (b != 0):
                ins.append("b" + str(b))
                print("b1", b)
                b = 0
            f+=1
            print("Y se povecava", path[p+1].x, path[p+1].y, " Yval= ", Yval, " Xval= ", Xval, "točka= ",p, "f= ", f, "l=",l ,"r= ", r, "b", b)

        #ide iza
        if (path[p+1].x==Xval)and(path[p+1].y==Yval-1):
            if (l != 0):
                ins.append("l" + str(l))
                print("l2", l)
                l = 0
            if (r != 0):
                ins.append("r" + str(r))
                print("r2", r)
                r = 0
            if(f!=0):
                ins.append("f"+str(f))
                print("f2", f)
                f=0
            b+=1
            print("Y se smanjuje", path[p+1].x, path[p+1].y, " Yval= ", Yval, " Xval= ", Xval, "točka= ",p, "f= ", f, "l=",l ,"r= ", r, "b", b)

        #ide levo
        elif(path[p+1].x==Xval+1)and(path[p+1].y == Yval):
            if(f!=0):
                ins.append("f"+str(f))
                print("f3",f)
                f=0
            if(r!=0):
                ins.append("r"+str(r))
                print("r3", r)
                r=0
            if (b != 0):
                ins.append("b" + str(b))
                print("b3", b)
                b = 0
            l+=1
            print("X se povecava",path[p + 1].x, path[p + 1].y, " Yval= ", Yval, " Xval= ", Xval, "točka= ",p, "f= ", f, "l=",l ,"r= ", r, "b", b)


        #ide desno
        elif(path[p+1].x==Xval-1)and(path[p+1].y==Yval):
            if (f != 0):
                ins.append("f" + str(f))
                print("f4", f)
                f = 0
            if (l != 0):
                ins.append("l" + str(l))
                print("l4", l)
                l = 0
            if (b != 0):
                ins.append("b" + str(b))
                print("b4", b)
                b = 0
            r += 1
            print("X se smanjuje", path[p + 1].x, path[p + 1].y, " Yval= ", Yval, " Xval= ", Xval, "točka= ", p, "f= ",f, "l=", l, "r= ", r, "b", b)

        elif(p==len(path)-2):

            if(f!=0):
                ins.append("f"+str(f))
                print("f5", f)
                f=0
            if (l != 0):
                ins.append("l" + str(l))
                print("l5",l)
                l = 0
            if (r != 0):
                ins.append("r" + str(r))
                print("r5", r)
                r = 0
            if (b != 0):
                ins.append("b" + str(b))
                print("b5", b)
                b = 0

        Yval=path[p+1].y
        Xval=path[p+1].x

    for n in range(len(ins)):
        print(ins[n])

    konvertano=[]