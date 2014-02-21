__author__ = 'kkk'
from tkinter import *
from time import *
##from clocker_hands import *
import math
class clocker(Canvas):
    def __init__(self):
        self.master = Tk()
        Canvas.__init__(self,self.master,width = 800, height = 800, bg = 'white')
        #self.master = Tk()
        #self.w = self (master, width=800, height = 800, bg='gray')
        self.r = (400,400,400,100)
        self.create_oval(100,100,700,700)
        #self.create_oval(self.r)
        self.s = [400,400,400,120]
        self.m = [400,400,400,200]
        self.h = [400,400,400,250]
        gTime = strftime('%H:%M:%S')
        gTime = gTime.split(':')
        self.curs = gTime[2]
        self.bt=[]
        self.sm = StringVar()
        #self.sm.set('waht\'s up!\n')
        self.lm = Label(self.master,text= 'what\'s up', textvariable = self.sm)
        #self.text = Text(self.master)
        #self.text.pack()
        self.lm.pack(side =BOTTOM)
    #model one, spin the hand by angle a (e.g pi/30 for second hand) every second
        #self.hour()
        #self.minute()
        #self.secon
        self.modelTwo()
    ##init the clock face
        self.setDial2()
        self.setNumber()
    def modelTwo(self):
        print ('Another way to come up!')
        self.bt = strftime('%H:%M:%S')
        self.setTime()
        self.create_line(self.h,fill='gray',width=20)
        self.create_line(self.m,fill='gray',width=5)
        self.create_line(self.s)#,fill='gray',width=1)
        self.displayBottom()
        self.master.after(999,self.modelTwo)
    def displayBottom(self):
        sa = self.realToDegree(self.getAngle(self.s))
        sa = (sa + 90) % 360
        self.bt = self.bt + '    The angle of second hand is: ' + str(sa) + ' degrees'
        self.sm.set(self.bt)
    def setNumber(self):
        print ('Radius of the Clock is: %s' % list(self.r))
        ns = list(self.r) #获得基准坐标，秒针最长，取得表针坐标用以绘制刻度
        sms = ('ns is initiated to: %s' % ns)
        self.sm.set(sms)
        ws = float(50) #the length of the scale
        nsCut =[ns[0],ns[1],ns[2],ns[3]+ws]
        na = math.pi/6
        for char in 'kiss me baby':
            print (char)
            print (ns)
            na = na + math.pi/6
            ns = self.getCoords(ns,na)
            print('after rotate pi/6 ns is %s' % ns)
            nsCut = self.getCoords(nsCut,na)
            print(('after rotate pi/6 nsCut is %s' % nsCut))
            nsNew = [nsCut[2],nsCut[3],ns[2],ns[3]]
            print(nsNew)
            self.create_line(nsNew,fill='black',width = 25)
            self.create_line(nsNew,fill='white',width = 1)
    def setDial2(self):
        print (self.r)
        ns = list(self.r) #获得基准坐标，秒针最长，取得表针坐标用以绘制刻度
        sms = ('ns is initiated to: %s' % ns)
        self.sm.set(sms)
        ws = float(16) #the length of the scale
        nsCut =[ns[0],ns[1],ns[2],ns[3]+ws]
        na = math.pi/30
        for i in range(60):
            print (i)
            print (ns)
            na = na + math.pi/30
            ns = self.getCoords(ns,na)
            print('after spin pi/6 ns is %s' % ns)
            nsCut = self.getCoords(nsCut,na)
            print(('after spin pi/6 nsCut is %s' % nsCut))
            nsNew = [nsCut[2],nsCut[3],ns[2],ns[3]]
            print(nsNew)
            self.create_line(nsNew,fill='gray',width = 16)
            #self.create_line(nsNew,fill='white',width = 1)
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
        minHand = self.create_line(self.m,fill='black',width=5)
        self.master.after(1000,self.minute)
        #self.sm.set('minute displayed?\n')
    def hour(self):
        #global self.h
        x = math.pi/(30*60*12)
        self.h = self.setCoords(self.h,x,20)
        hrHand = self.create_line(self.h,fill='black',width=20)
        self.master.after(1000, self.hour)
        print('hour hand displayed?\n')

    def getTimeChange(self): #扫描当前时间，当秒变化时，调用setTime，刷新表盘
        gTime = strftime('%H:%M:%S')
        gTime = gTime.split(':')
        count = 0
        while gTime[2] == self.curs:
            gTime = strftime('%H:%M:%S')
            gTime = gTime.split(':')
            print(gTime)
            count = count + 1
        print('Count is : %d' % count)
        return (gTime[2])
    def setTime(self):
        self.clearHand(self.h,20)    #清除本次调用前时针轨迹
        self.clearHand(self.m,5)     #清除本次调用前分针轨迹
        self.clearHand(self.s,1)     #清除本次调用前秒针轨迹
        sTime = strftime('%H:%M:%S')
        sTime = sTime.split(':')
        hh = int(sTime[0])
        mm = int(sTime[1])
        ss = int (sTime[2])
        print('Current time is: %s'% sTime)
        hha = math.pi * 2 *( (hh % 12) / 12 + mm/(60*12) + ss/(60*60*12))- math.pi/2 #时针偏离基准（x轴正方向)的角度
        mma = math.pi * 2 * (mm + ss/60)/60- math.pi/2 #分针偏离基准（x轴正方向)的角度
        ssa = math.pi * 2 * ss / 60 - math.pi/2 #秒针偏离基准（x轴正方向)的角度
        print (hha, mma, ssa)
        self.h = self.getCoords(self.h,hha)    #时针新坐标
        self.m = self.getCoords(self.m,mma)    #分针新坐标
        self.s = self.getCoords(self.s,ssa)    #秒针新坐标
        ## 设好新坐标后，无需在调用setCoords绘制，主程序中hour(),minute(),second()会循环调用根据新的self.h|m|s值绘制表针
        ## setCoodrs 重命名成clearHand,只用来擦除旧表针，不在绘制当前（新）表针。
        ## 绘制交由 setTime统一完成

        return (self)

    ## 输入表针坐标（x1,y1,x2,y2)——作用仅为标示圆心和表针长度
    ## 输入偏转角（相对于x轴正方向），返回旋转后表针的坐标
    ## 根据当前时间->表针偏转角->换算出表针坐标
    def getCoords(self,cc,a):
        r = ( (cc[2] - cc[0]) ** 2 + (cc[3] - cc[1] ) ** 2 ) ** 0.5
        x = r * math.cos(a)
        y = r * math.sin(a)
        cc[2]=x+cc[0]
        cc[3]=y+cc[1]
        print ('get the coords of hand: %s' % cc)
        return (cc)
    ## 输入当前表针坐标，从表盘擦除表针（以背景色以及相应宽度重新绘表针）针粗细ww
    def clearHand(self,cc,ww):
            self.create_line(cc,fill="white",width=ww)
    # 输入当前表针起始坐标cc、返回表针相对x轴正方向的角度
    def getAngle(self,cc):
            r = ( (cc[2] - cc[0]) ** 2 + (cc[3] - cc[1] ) ** 2 ) ** 0.5
            print('current R is:%8.4f' % r)
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
            print("The angle of the hand is: %f" % starta)
            print('The coords of the hand are (after calculated from the Angle: is %s' % cc)
            return (starta)
    ## 实数角度转换成360°角度
    def realToDegree(self,starta):
        d = int(starta * 180/math.pi)
        return(d)
    def tick(self):
        #self.master.title(strftime('%H:%M:%S'))
        self.master.title('Clock')
        #self.sm.set(strftime('%H:%M:%S'))
        #self.master.after(1000,self.tick)
