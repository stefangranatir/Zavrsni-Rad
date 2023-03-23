from Point import Pt
import serial
import time
import threading
import PretvorbaUInstrukcije


def testIspis(path):
    #bool promjena=false;
    ser = serial.Serial("COM4", 38400, timeout=1)
    #ser.reset_input_buffer()

    xPrije=0
    xTrenutno=0
    yPrije=0
    yTrenutno=0

    print(path[0].x,path[0].y,path[1].x,path[1].y)
    x=len(path)
    print(x)
    #b=0

    PretIns=threading.Thread()
    PretIns.start()
    PretvorbaUInstrukcije.pretvorba(path)
    PretIns.join()

    for p in range(len(path)):

        #for d in path:
            #if(d==p+1):
                #print(p.x, p.y, d.x, d.y)
        #print(bytes(str(f'{p.x},{p.y}'), 'utf_8'))
        #print(path[p].x, path[p].y, path[p+1].x, path[p+1].y)
        ##print(len(path))
        #print(p.x, p.y)
        #print(path[p].x, path[p].y, path[p+1].x, path[p+1].y)

        ser.write(bytes(str(f'{p.x},{p.y}'), 'utf_8'))
        input_data=ser.readline()
        print(input_data.decode())
        #j,k =path[p+1]
        ##print(p.x, p.y,'f {j}, {k}')
        time.sleep(1)
    ser.close()

