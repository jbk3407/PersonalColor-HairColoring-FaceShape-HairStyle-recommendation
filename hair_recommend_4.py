from tkinter import *

import read_shape

window = Tk()
window.title('CS_PROJECT \n Hair_recmmend_4')
window.geometry('1000x1100')

image = '/home/bryan/Desktop/CS_LOG/Pictures/four_season.png'
image_square_recommend = '/home/bryan/Desktop/CS_LOG/Pictures/square_recommend.png'
image_square_nonrecommend = '/home/bryan/Desktop/CS_LOG/Pictures/oblong_nonrecommend.png'

image_round = '/home/bryan/Desktop/CS_LOG/Pictures/oblong_recommend.png'

image_oval_recommend = '/home/bryan/Desktop/CS_LOG/Pictures/oblong_recommend.png'
image_oval_nonrecommend = '/home/bryan/Desktop/CS_LOG/Pictures/oblong_nonrecommend.png'

image_oblong = '/home/bryan/Desktop/CS_LOG/Pictures/oblong_recommend.png'

image_heart = '/home/bryan/Desktop/CS_LOG/Pictures/oblong_recommend.png'

background = PhotoImage(file=image)
window['bg'] = 'orange'


shape = read_shape.get_most_shape()

label1 = Label(window,
               text='Your Face Shape is ' + shape + '\n',
               font=("궁서체", 30),
               bg='orange', fg="blue")
label1.pack()

# label = Label(window, image=background, relief=SUNKEN)
# label.pack()


if shape == 'Square':
    label_square_recommend2 = Label(window, text='RECOMMENED \n  Two Block & Az perm',
                                    font=('궁서체, 20'),
                                    bg='orange', fg='blue',
                                    relief=SUNKEN)
    label_square_recommend2.pack()

    bg_square_recommend = PhotoImage(file=image_oval_recommend)
    label_square_recommend = Label(window, image=bg_square_recommend, relief=SUNKEN)
    label_square_recommend.pack(pady=20)

    label_square_nonrecommend2 = Label(window, text='NOT RECOMMENED \n 5:5 garma',
                                       font=('궁서체, 20'),
                                       bg='orange', fg='red',
                                       relief=SUNKEN)
    label_square_nonrecommend2.pack()

    bg_square_nonrecommend = PhotoImage(file=image_oval_nonrecommend)
    label_square_nonrecommend = Label(window, image=bg_square_nonrecommend, relief=SUNKEN)
    label_square_nonrecommend.pack(pady=20)



elif shape == 'Round':
    label_round_recommend2 = Label(window, text='RECOMMENED \n Two Block & Az perm',
                                   font=('궁서체, 20'),
                                   bg='orange', fg='blue',
                                   relief=SUNKEN)
    label_round_recommend2.pack()

    bg_round_recommend = PhotoImage(file=image_oval_recommend)
    label_round_recommend = Label(window, image=bg_round_recommend, relief=SUNKEN)
    label_round_recommend.pack(pady=20)

    label_round_nonrecommend2 = Label(window, text='NOT RECOMMENED \n 5:5 garma',
                                      font=('궁서체, 20'),
                                      bg='orange', fg='red',
                                      relief=SUNKEN)
    label_round_nonrecommend2.pack()

    bg_round_nonrecommend = PhotoImage(file=image_oval_nonrecommend)
    label_round_nonrecommend = Label(window, image=bg_round_nonrecommend, relief=SUNKEN)
    label_round_nonrecommend.pack(pady=20)


elif shape == 'Oval':
    label_oval_recommend2 = Label(window, text='RECOMMENED \n Two Block & Az perm',
                                  font=('궁서체, 20'),
                                  bg='orange', fg='blue',
                                  relief=SUNKEN)
    label_oval_recommend2.pack()

    bg_oval_recommend = PhotoImage(file=image_oval_recommend)
    label_oval_recommend = Label(window, image=bg_oval_recommend, relief=SUNKEN)
    label_oval_recommend.pack(pady=20)

    label_oval_nonrecommend2 = Label(window, text='NOT RECOMMENED \n 5:5 garma',
                                     font=('궁서체, 20'),
                                     bg='orange', fg='red',
                                     relief=SUNKEN)
    label_oval_nonrecommend2.pack()

    bg_oval_nonrecommend = PhotoImage(file=image_oval_nonrecommend)
    label_oval_nonrecommend = Label(window, image=bg_oval_nonrecommend, relief=SUNKEN)
    label_oval_nonrecommend.pack(pady=20)


elif shape == 'Oblong':
    label_oblong_recommend2 = Label(window, text='RECOMMENED \n Two Block & Az perm',
                                    font=('궁서체, 20'),
                                    bg='orange', fg='blue',
                                    relief=SUNKEN)
    label_oblong_recommend2.pack()

    bg_oblong_recommend = PhotoImage(file=image_oval_recommend)
    label_oblong_recommend = Label(window, image=bg_oblong_recommend, relief=SUNKEN)
    label_oblong_recommend.pack(pady=20)

    label_oblong_nonrecommend2 = Label(window, text='NOT RECOMMENED \n 5:5 garma',
                                       font=('궁서체, 20'),
                                       bg='orange', fg='red',
                                       relief=SUNKEN)
    label_oblong_nonrecommend2.pack()

    bg_oblong_nonrecommend = PhotoImage(file=image_oval_nonrecommend)
    label_oblong_nonrecommend = Label(window, image=bg_oblong_nonrecommend, relief=SUNKEN)
    label_oblong_nonrecommend.pack(pady=20)


elif shape == 'Heart':
    label_heart_recommend2 = Label(window, text='RECOMMENED \n Two Block & Az perm',
                                   font=('궁서체, 20'),
                                    fg='blue',
                                   relief=SUNKEN)
    label_heart_recommend2.pack()

    bg_heart_recommend = PhotoImage(file=image_oval_recommend)
    label_heart_recommend = Label(window, image=bg_heart_recommend, relief=SUNKEN)
    label_heart_recommend.pack(pady=20)

    label_heart_nonrecommend2 = Label(window, text='NOT RECOMMENED \n 5:5 Garma',
                                      font=('궁서체, 20'),
                                       fg='red',
                                      relief=SUNKEN)
    label_heart_nonrecommend2.pack()

    bg_heart_nonrecommend = PhotoImage(file=image_oval_nonrecommend)
    label_heart_nonrecommend = Label(window, image=bg_heart_nonrecommend, relief=SUNKEN)
    label_heart_nonrecommend.pack(pady=20)


def initial_page():
    window.destroy()
    import integrate

b1 = Button(window,
            text='Go Back to First Page',
            relief=RAISED,
            height=5, width=50,
            command=initial_page,
            font=("궁서체", 20),)
b1.pack(pady=20)
# b2 = Button(window,
#             text='Get HairStyle Recommendation',
#             relief=RAISED,
#             height=20, width=50,
#             bg='orange', fg='blue',
#             command=getpage4)


window.mainloop()
