from tkinter import *


def nextPage():
    window.destroy()
    import page2

def getpage4():
    window.destroy()
    import page4


window = Tk()
window.title('CS_PROJECT')
window.geometry('1000x800')
window['bg'] = 'orange'

label1 = Label(window,
               text="CS_PROJECT \n Beauty Salon",
               font=("궁서체",30),
               bg='orange', fg="blue")
label1.pack()

background = PhotoImage(file='/home/bryan/Desktop/CS_LOG/Pictures/photo.png')
label2 = Label(window, image=background, relief=SUNKEN)
label2.pack()



b1 = Button(window,
            text='Find out My Personal Color',
            relief=RAISED,
            height=20, width=50,
            command=nextPage,
            bg='orange', fg='blue')

b2 = Button(window,
            text='Get HairStyle Recommendation',
            relief=RAISED,
            height=20, width=50,
            bg='orange', fg='blue',
            command=getpage4)

b3 = Button(window,
            text='EXIT',
            relief=RAISED,
            height=5, width=50,
            bg='orange', fg='blue',
            command=window.quit)



b1.pack(side=LEFT, padx=10)
b2.pack(side=RIGHT, padx=10)
b3.pack(side=BOTTOM)


# b3 = Button(root, text='Run', relief=RAISED, height=20, width=20)
# b3.pack(side=LEFT, padx=10)
#
# b4 = Button(root, text='Run', relief=RAISED, height=20, width=20)
# b4.pack(side=LEFT, padx=10)


window.mainloop()