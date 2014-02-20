__author__ = 'kkk'
from tkinter import *
from clock_model import *
import math

def tick():
    master.title(strftime('%H:%M:%S'))
    master.after(1000,tick)
master = Tk()
master.title('Clock')
tick()
cl = clocker(master).setTime()
cl.pack()

mainloop()
