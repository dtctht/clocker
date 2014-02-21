__author__ = 'kkk'
from tkinter import *
from clock_model import *
import math


##简单时钟演示程序。主要功能实现均在Class中
cl = clocker()
cl.tick()
cl.pack()
mainloop()
