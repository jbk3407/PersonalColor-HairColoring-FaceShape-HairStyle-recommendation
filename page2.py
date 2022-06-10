from tkinter import *
import cv2

def nextPage():
    window.destroy()
    import page3

def initial_page():
    window.destroy()
    import integrate

def webcam():
    cam = cv2.VideoCapture(0)
    while (True):
        # ret : frame capture결과(boolean)
        # frame : Capture한 frame

        ret, frame = cam.read()
        if (ret):
            cv2.imshow('Space to capture / Esc to exit', frame)
            k = cv2.waitKey(1)

            if k % 256 == 32:
                # SPACE pressed
                img_name = "captured_image.png"
                captured_image = cv2.imwrite('/home/bryan/Desktop/CS_LOG/Pictures/' + img_name, frame)
                print("{} written!".format(img_name))
                # window.destroy()
                # import page3
                break
                # return captured_image


            # elif k % 256 == 27:
            #     # ESC pressed
            #     print("Escape hit, closing...")
            #     break

    cam.release()
    cv2.destroyAllWindows()
    window.destroy()
    import page3

window = Tk()
window.title('page2')
window.geometry('600x500')
window['bg'] = 'white'

background = PhotoImage(file='/home/bryan/Desktop/CS_LOG/Pictures/photo.png')
label = Label(window, image=background, relief=SUNKEN)
label.pack()

b1 = Button(window, text='Take New Photo \n Space to capture / Esc to exit', relief=RAISED, height=10, width=30, command=webcam)
b1.pack(side='left')

b2 = Button(window, text='Use Already taken Photo', relief=RAISED, height=10, width=30, command=nextPage)
b2.pack(side='right')

b3 = Button(window, text='EXIT', relief=RAISED, height=5, width=100, command=window.quit)
b3.pack(side='bottom')

b4 = Button(window,
            text='First Page',
            relief=RAISED,
            height=5, width=50,
            bg='orange', fg='blue',
            command=initial_page)
b4.pack(side=BOTTOM)


window.mainloop()