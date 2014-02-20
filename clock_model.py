__author__ = 'kkk'
from tkinter import *
from time import *
##from clocker_hands import *
import math
class clocker(Canvas):
    def __init__(self):
        self.master = Tk()
        Canvas.__init__(self,self.master,width = 800, height = 800, bg = 'gray')
        #self.master = Tk()
        #self.w = self (master, width=800, height = 800, bg='gray')
        self.create_oval(100,100,700,700)
        self.s = [400,400,400,100]
        self.m = [400,400,400,200]
        self.h = [400,400,400,250]

        self.sm = StringVar()
        #self.sm.set('waht\'s up!\n')
        self.lm = Label(self.master,text= 'what\'s up', textvariable = self.sm)
        #self.text = Text(self.master)
        #self.text.pack()
        self.lm.pack(side =BOTTOM)
        self.setNumber()
        self.hour()
        self.minute()
        self.second()
    #def setMonitor(self):
     #   self.sm.set ('----------------------- object view --------------------------')

    def setNumber(self):
        print (self.s)
        ns = self.s #获得基准坐标，秒针最长，取得表针坐标用以绘制刻度
        sms = ('ns is initiated to: %s' % ns)
        self.sm.set(sms)
        ws = float(30)
        nsCut =[ns[0],ns[1],ns[2],ns[3]+ws]
        na = math.pi/6
        ns = self.getCoords(ns,na)
        nsCut = self.getCoords(nsCut,na)
        nsNew = [nsCut[2],nsCut[3],ns[2],ns[3]]
        self.create_line(nsNew,fill='black',width= 25)


    def second(self):
        #global self.s
        #master.title(strftime('%H:%M:%S'))
        x = math.pi/30
        self.s = self.setCoords(self.s,x,1)
        secHand = self.create_line(self.s)
        self.master.after(1000, self.second)
        #self.sm.set('secHand displayed?')
        #self.setMonitor()

    def minute(self):
        #global self.m
        x = math.pi/(30*60)
        self.m = self.setCoords(self.m,x,5)
        minHand = self.create_line(self.m,fill='white',width=5)
        self.master.after(1000,self.minute)
        #self.sm.set('minute displayed?\n')

    def hour(self):
        #global self.h
        x = math.pi/(30*60*12)
        self.h = self.setCoords(self.h,x,20)
        hrHand = self.create_line(self.h,fill='white',width=20)
        self.master.after(1000, self.hour)
        print('hour hand displayed?\n')
    def setTime(self):
        self.h = self.setCoords(self.h,0,20)    #清除初始化绘制的时针
        self.m = self.setCoords(self.m,0,5)     #清除初始化绘制的分针
        self.s = self.setCoords(self.s,0,1)     #清除初始化绘制的秒针
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
##输入当前线段（表针）的当前坐标（x1,y1,x2,y2),以及偏转角，返回旋转后表针的坐标
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
    def tick(self):
        self.master.title(strftime('%H:%M:%S'))
        self.master.after(1000,self.tick)
