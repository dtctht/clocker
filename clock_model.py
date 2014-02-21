__author__ = 'kkk'
from tkinter import *
from time import *
import math
##
##主类是继承Tk.Cavas
##所有时钟相关功能全部在此类中实现
##主要方法有：
##表针转换为坐标（线段），指针（线段）转换为坐标，
## 根据表针当前坐标和偏转角度返回表针新坐标
##根据表针（线段）坐标，宽度（粗细）绘制线段（时针分针秒针）
##绘制表盘，大刻度和小刻度
##根据当前时间计算表针位置，返回相对于x轴正方向（右）偏转角
##
class clocker(Canvas):
    def __init__(self):
        self.master = Tk()                  ##定义表盘窗口(tk)
        Canvas.__init__(self,self.master,width = 800, height = 800, bg = 'white')##生成表盘画布(Cavas)
        self.π = math.pi
        self.r = (400,400,400,100)          ##定义时钟半径（实际零点位置时钟中心最长线段坐标）300像素
        self.create_oval(100,100,700,700)   ##画出时钟轮廓
        self.s = [400,400,400,120]          ##秒针初始化到零点位置，长度为280像素
        self.m = [400,400,400,200]          ##秒针初始化到零点位置，长度为200像素
        self.h = [400,400,400,250]          ##秒针初始化到零点位置，长度为150像素
        gTime = strftime('%H:%M:%S')        ##获取当前时间
        gTime = gTime.split(':')
        self.curs = gTime[2]                ##当前时间秒的读数（范围0~59）赋予类全局变量curs
        self.sm = StringVar()               ##定义字符串变量用于界面控件显示文字内容
        self.lm = Label(self.master,text= 'what\'s up', textvariable = self.sm)
        self.lm.pack(side =BOTTOM)          ##显示内容为当前时间，HH:MM:SS形式，放置在窗口底部
    ##
    ## 第一种方法，读取当前时间，转换成时分秒指针的位置。然后计算出一秒钟各个表针转角，按照计算出转角每秒分别转动各表针一次，
    ## Model one, spin the hand by angle a (e.g pi/30 for second hand) every second
        #self.hour()
        #self.minute()
        #self.second()
    ##
        print('π is : %f' % self.π)
    ## 第二种方法实现，每秒（实际是999毫秒）读取当前时间，并转换成时分秒针位置坐标，刷新界面上时钟时分秒针位置
        self.modelTwo()

    ##i nit the clock face
        self.setDial2()                     ##初始化时钟刻度盘小刻度
        self.setNumber()                    ##初始化时钟刻度盘大刻度
    ## 第二种方法，实时读取当前系统时间刷新钟面
    def modelTwo(self):
        self.sm.set(strftime('%H:%M:%S'))
        self.setTime()
        self.create_line(self.h,fill='gray',width=20)
        self.create_line(self.m,fill='gray',width=5)
        self.create_line(self.s)#,fill='gray',width=1)
        self.master.after(999,self.modelTwo)
    ## 初始化表盘大刻度
    def setNumber(self):
        ###print (self.r)
        ns = list(self.r) #获得基准坐标，秒针最长，取得表针坐标用以绘制刻度
        sms = ('ns is initiated to: %s' % ns)
        self.sm.set(sms)
        ws = float(50) #the length of the scale
        nsCut =[ns[0],ns[1],ns[2],ns[3]+ws]
        na = math.pi/6
        for char in 'kiss me baby':
            na = na + math.pi/6
            ns = self.getCoords(ns,na)
            ###print('after rotate pi/6 ns is %s' % ns)
            nsCut = self.getCoords(nsCut,na)
            ###print(('after rotate pi/6 nsCut is %s' % nsCut))
            nsNew = [nsCut[2],nsCut[3],ns[2],ns[3]]
            ###print(nsNew)
            self.create_line(nsNew,fill='black',width = 25)
            self.create_line(nsNew,fill='white',width = 1)
    ## 初始化表盘小刻度
    def setDial2(self):
        ### print (self.r)
        ns = list(self.r) #获得基准坐标，秒针最长，取得表针坐标用以绘制刻度
        sms = ('ns is initiated to: %s' % ns)
        self.sm.set(sms)
        ws = float(16) #the length of the scale
        nsCut =[ns[0],ns[1],ns[2],ns[3]+ws]
        na = math.pi/30
        for i in range(60):
            ###print (i)
            ###print (ns)
            na = na + math.pi/30
            ns = self.getCoords(ns,na)
            ###print('after spin pi/6 ns is %s' % ns)
            nsCut = self.getCoords(nsCut,na)
            ###print(('after spin pi/6 nsCut is %s' % nsCut))
            nsNew = [nsCut[2],nsCut[3],ns[2],ns[3]]
            ###print(nsNew)
            self.create_line(nsNew,fill='gray',width = 16)
            #self.create_line(nsNew,fill='white',width = 1)
    ## 转动秒针，每次（秒）旋转6度
    def second(self):
        #global self.s
        #master.title(strftime('%H:%M:%S'))
        x = math.pi/30
        self.s = self.setCoords(self.s,x,1)
        secHand = self.create_line(self.s)
        self.master.after(1000, self.second)
        #self.sm.set('secHand displayed?')
        #self.setMonitor()
    ## 转动分针，每次（秒）旋转1/10度
    def minute(self):
        #global self.m
        x = math.pi/(30*60)
        self.m = self.setCoords(self.m,x,5)
        minHand = self.create_line(self.m,fill='black',width=5)
        self.master.after(1000,self.minute)
        #self.sm.set('minute displayed?\n')
    ## 转动时针，每次旋转1/120度
    def hour(self):
        #global self.h
        x = math.pi/(30*60*12)
        self.h = self.setCoords(self.h,x,20)
        hrHand = self.create_line(self.h,fill='black',width=20)
        self.master.after(1000, self.hour)
        ###print('hour hand displayed?\n')
    ##
    # ## getTimeChange(self):
    ## 当前秒读数curs为输入参数，扫描当前时间变化，当秒变化，返回当前秒读数。未实际未调用
    ##（设计目标是：扫描当前时间，当秒变化时，调用setTime，刷新表盘。但未实现，
    ## 现象：当上层循环调用本方法，则无法显示GUI，本层自调用则仍会用到after方法
    def getTimeChange(self):
        gTime = strftime('%H:%M:%S')
        gTime = gTime.split(':')
        count = 0
        while gTime[2] == self.curs:
            gTime = strftime('%H:%M:%S')
            gTime = gTime.split(':')
        self.curs = gTime[2]
        #self.master.after(999,self.getTimeChange)
    ## 刷新时分秒针位置，现将当前时分秒针位置擦除，转动时分秒针
    ## 秒针，每次（秒）旋转6度；分针，每次（秒）旋转1/10度；时针，每次旋转1/120度
    ## 方法中使用的是实数，360度对应实数角度为2π
    def setTime(self):
        self.h = self.setCoords(self.h,0,20)    #清除本次调用前时针轨迹
        self.m = self.setCoords(self.m,0,5)     #清除本次调用前分针轨迹
        self.s = self.setCoords(self.s,0,1)     #清除本次调用前秒针轨迹
        sTime = strftime('%H:%M:%S')
        sTime = sTime.split(':')
        hh = int(sTime[0])
        mm = int(sTime[1])
        ss = int (sTime[2])
        print('Current time is: %s'% sTime)
        hha = math.pi * 2 *( (hh % 12) / 12 + mm/(60*12) + ss/(60*60*12))- math.pi/2 #时针偏离基准（x轴正方向)的角度
        mma = math.pi * 2 * (mm + ss/60)/60- math.pi/2 #分针偏离基准（x轴正方向)的角度
        ssa = math.pi * 2 * ss / 60 - math.pi/2 #秒针偏离基准（x轴正方向)的角度
        ###print (hha, mma, ssa)
        self.h = self.getCoords(self.h,hha)    #时针新坐标
        self.m = self.getCoords(self.m,mma)    #分针新坐标
        self.s = self.getCoords(self.s,ssa)    #秒针新坐标
        ##设好新坐标后，无需在调用setCoords绘制，主程序中hour(),minute(),second()会循环调用根据新的self.h|m|s值绘制表针
        return (self)
    ##
    ## 输入当前时间对应表针的当前坐标（x1,y1,x2,y2),偏转角（相对于x轴正方向），返回旋转后表针的坐标
    ## 此方法为“绝对寻址”，表针起点为钟面圆心，转角起点为x轴正向，使用（正）三角函数得到新坐标
    def getCoords(self,cc,a):
        r = ( (cc[2] - cc[0]) ** 2 + (cc[3] - cc[1] ) ** 2 ) ** 0.5
        x = r * math.cos(a)
        y = r * math.sin(a)
        cc[2]=x+cc[0]
        cc[3]=y+cc[1]
        ###print ('get the coords of hand: %s' % cc)
        return (cc)

    ## 输入当前表针起始坐标cc、旋转角a，和表针粗细ww,返回表针旋转后的坐标（线段起始坐标）
    ## 此方法为“相对寻址”，表针起点为起点坐标(x1,y1)，转角起点为表针（线段）当前位置
    ## 会使用到反三角函数，所以会有分区间处理
    ## 改进：其实两方法分别实现两种功能，一个是已知转角，计算旋转后坐标，一个是已知坐标，计算转角
    def setCoords(self,cc,a, ww):
            self.create_line(cc,fill="white",width=ww)
            r = ( (cc[2] - cc[0]) ** 2 + (cc[3] - cc[1] ) ** 2 ) ** 0.5
            ###print('current R is:%8.4f' % r)
            ###print('angle is %8f'% a)
            ###print (cc)
            x = cc[2] - cc[0]
            y = cc[3] - cc[1]
            ###print(x,y)
            sina = y / r
            cosa = x / r
            starta = float()
            if y > 0 and x > 0:
                starta=math.asin ( sina ) ## 0 ~ PI/2
            else:
                if  y > 0 and x <=0:
                    starta = math.acos(cosa) ## PI/2 ~ PI
                else:
                    if y <=0 and x <=0:
                        starta = math.pi*2 - math.acos(cosa)
                    else:
                        starta = math.pi * 2 + math.asin(sina)
            ###print (starta)
            a = starta + a
            ###print("new a is: %f" % a)
            cc[2] = cc[0] + r * math.cos(a)
            cc[3] = cc[1] + r * math.sin(a)
            ###print ('after spin, R is %8f\n' % r)
            return (cc)
    def tick(self):
        #self.master.title(strftime('%H:%M:%S'))
        self.master.title('Clock')
        #self.sm.set(strftime('%H:%M:%S'))
        #self.master.after(1000,self.tick)
