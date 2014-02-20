__author__ = 'kkk'
from tkinter import *
from clock_model import *
import math


#master = Tk()
#master.title('Clock')
cl = clocker().setTime()
cl.tick()
cl.pack()
#cl.setMonitor()

mainloop()
