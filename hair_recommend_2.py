from tkinter import *
import os
import ShowMeTheColor
import Hair_recommend_3

def open_faceshape():
    Hair_recommend_3.main()
    window.destroy()
    Hair_recommend_3.new_page()

def initial_page():
    window.destroy()
    import integrate

window = Tk()
window.title('CS_PROJECT \n Hair_recmmend_2')
window.geometry('1000x1100')
window['bg'] = 'orange'
# image = '/home/bryan/Desktop/CS_LOG/Pictures/face_landmark.png'
image = '/home/bryan/Desktop/CS_LOG/Pictures/fc.png'
background = PhotoImage(file=image)

label1 = Label(window,
               text='FIRST WE NEED TO FIND OUT \n YOUR FACE SHAPE',
               font=("궁서체", 25),
               bg='orange', fg="blue")
label1.pack(pady=20)

label = Label(window, image=background, relief=SUNKEN)
label.pack(pady=20)

b1 = Button(window, text='Click to find Face Shape', relief=RAISED, height=5, width=50, font=("궁서체",15), command=open_faceshape)
b1.pack(pady=20)

b1 = Button(window, text='Go back', relief=RAISED, height=5, width=50, font=("궁서체",15),command=initial_page)
b1.pack(pady=20)

b3 = Button(window, text='EXIT', relief=RAISED, height=5, width=50, font=("궁서체",15), command=window.quit)
b3.pack(pady=20)


window.mainloop()


