import sys
from tkinter import *

import ShowMeTheColor.src.main
from ShowMeTheColor.res import *
import ShowMeTheColor.personal_color_analysis

import torch


def run_color():
    window.destroy()
    ShowMeTheColor.src.main.main()


def goback():
    window.destroy()
    import personal_color_2



window = Tk()
window.title('CS_PROJECT \n personal_color_3')
window.geometry('1000x1100')
image = '/home/bryan/Desktop/CS_LOG/Pictures/captured_image.png'
window['bg'] = 'orange'

background = PhotoImage(file=image)

label1 = Label(window,
               text="Get result",
               font=("궁서체",30),
               bg='orange', fg="blue")
label1.pack()

label = Label(window, image=background, relief=SUNKEN)
label.pack(pady=20)

input_image = '/home/bryan/Desktop/CS_LOG/Pictures/captured_image.png'
b1 = Button(window, text='Get result', relief=RAISED, height=5, width=50, font=("궁서체",15), command=run_color)
b1.pack(pady=20)

b2 = Button(window, text='goback', relief=RAISED, height=5, width=50, font=("궁서체",15), command=goback)
b2.pack(pady=20)

b3 = Button(window, text='EXIT', relief=RAISED, height=5, width=50, font=("궁서체",15), command=window.quit)
b3.pack(pady=20)

window.mainloop()
