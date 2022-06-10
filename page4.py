from tkinter import *
import HairColoring
from HairColoring import webcam
from HairColoring.param import *
from HairColoring import models

def haircoloring():
    webcam()


window = Tk()
window.title('CS_PROJECT')
window.geometry('1000x800')
window['bg'] = 'orange'

label1 = Label(window,
               text=('/home/bryan/Desktop/CS_LOG/Printed_results22222/color_reslut.txt'),
               font=("궁서체", 30),
               bg='orange', fg="blue")
label1.pack()

b1 = Button(window, text='Get result', relief=RAISED, height=20, width=50, command=haircoloring)
b1.pack()