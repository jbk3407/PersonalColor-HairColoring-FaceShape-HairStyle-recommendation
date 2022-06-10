import sys
from tkinter import *

import ShowMeTheColor.src.main
from ShowMeTheColor.res import *
import ShowMeTheColor.personal_color_analysis

def run_color():
    window.destroy()
    ShowMeTheColor.src.main.main()


def goback():
    window.destroy()
    import page2



window = Tk()
window.title('page3')
window.geometry('1000x800')
image = '/home/bryan/Desktop/CS_LOG/Pictures/captured_image.png'
window['bg'] = 'orange'

background = PhotoImage(file=image)

label1 = Label(window,
               text="Get result",
               font=("궁서체",30),
               bg='orange', fg="blue")
label1.pack()

label = Label(window, image=background, relief=SUNKEN)
label.pack()

input_image = '/home/bryan/Desktop/CS_LOG/Pictures/captured_image.png'
b1 = Button(window, text='Get result', relief=RAISED, height=20, width=50, command=run_color)
b1.pack()

b2 = Button(window, text='goback', relief=RAISED, height=20, width=50, command=goback)
b2.pack()


window.mainloop()