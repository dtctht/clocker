__author__ = 'kkk'
from tkinter import *
from time import *
##from clocker_hands import *
import math
class clocker(Canvas):
    def __init__(self,master):
        self.master = Tk()
        Canvas.__init__(self,self.master,width = 800, height = 800, bg = 'gray')
        #self.master = Tk()
        #self.w = self (master, width=800, height = 800, bg='gray')
        self.create_oval(100,100,700,700)
        self.s = [400,400,400,100]
        self.m = [400,400,400,200]
        self.h = [400,400,400,250]
        self.hour()
        self.minute()
        self.second()
    def second(self):
        #global self.s
        #master.title(strftime('%H:%M:%S'))
        x = math.pi/30
        self.s = self.setCoords(self.s,x,1)
        secHand = self.create_line(self.s)
        self.master.after(1000, self.second)
        print ('I am secHand, am I visible??\n')
    def minute(self):
        #global self.m
        x = math.pi/(30*60)
        self.m = self.setCoords(self.m,x,5)
        minHand = self.create_line(self.m,fill='white',width=5)
        self.master.after(1000,self.minute)
        print('minute displayed?\n')
    def hour(self):
        #global self.h
        x = math.pi/(30*60*12)
        self.h = self.setCoords(self.h,x,20)
        hrHand = self.create_line(self.h,fill='blue',width=20)
        self.master.after(1000, self.hour)
        print('hour hand displayed?\n')
    def setTime(self):
        self.h = self.setCoords(self.h,0,20)    #清楚初始化绘制的时针
        self.m = self.setCoords(self.m,0,5)     #清楚初始化绘制的分针
        self.s = self.setCoords(self.s,0,1)     #清楚初始化绘制的秒针
        sTime = strftime('%H:%M:%S')
        sTime = sTime.split(':')
        hh = int(sTime[0])
        mm = int(sTime[1])
        ss = int (sTime[2])
        print('Current time is: %s'% sTime)
        hha = math.pi * 2 * (hh % 12) / 12 - math.pi/2 #时针偏离基准（x轴正方向)的角度
        mma = math.pi * 2 * mm / 60 - math.pi/2 #分针偏离基准（x轴正方向)的角度
        ssa = math.pi * 2 * ss / 60 - math.pi/2 #秒针偏离基准（x轴正方向)的角度
        print (hha, mma, ssa)
        self.h = self.getCoords(self.h,hha)    #时针新坐标
        self.m = self.getCoords(self.m,mma)    #分针新坐标
        self.s = self.getCoords(self.s,ssa)    #秒针新坐标
        ##设好新坐标后，无需在调用setCoords绘制，主程序中hour(),minute(),second()会循环调用根据新的self.h|m|s值绘制表针

        return (self)

    def getCoords(self,cc,a):
        r = ( (cc[2] - cc[0]) ** 2 + (cc[3] - cc[1] ) ** 2 ) ** 0.5
        x = r * math.cos(a)
        y = r * math.sin(a)
        cc[2]=x+cc[0]
        cc[3]=y+cc[1]
        print ('get the coords of hand: %s' % cc)
        return (cc)
    def setCoords(self,cc,a, ww):
            self.create_line(cc,fill="gray",width=ww)
            r = ( (cc[2] - cc[0]) ** 2 + (cc[3] - cc[1] ) ** 2 ) ** 0.5
            print('current R is:%8.4f' % r)
            print('angle is %8f'% a)
            print (cc)
            x = cc[2] - cc[0]
            y = cc[3] - cc[1]
            print(x,y)
            sina = y / r
            cosa = x / r
            starta = float()
            if y > 0 and x > 0:
                starta=math.asin ( sina ) ## 0 ~ PI/2
                print ("q1: %f" % starta)
            else:
                if  y > 0 and x <=0:
                    starta = math.acos(cosa) ## PI/2 ~ PI
                    print ("q2: %f" % starta)
                else:
                    if y <=0 and x <=0:
                        starta = math.pi*2 - math.acos(cosa)
                        print("q3: %f" % starta)
                    else:
                        starta = math.pi * 2 + math.asin(sina)
                        print("q4: %f" % starta)
            print (starta)
            a = starta + a
            print("new a is: %f" % a)
            cc[2] = cc[0] + r * math.cos(a)
            cc[3] = cc[1] + r * math.sin(a)

            print(cc)

            print ('after spin, R is %8f\n' % r)
            #w = Canvas(master)


            return (cc)
