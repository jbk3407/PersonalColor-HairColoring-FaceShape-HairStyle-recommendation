from tkinter import *
import numpy as np
import sys
from ShowMeTheColor.personal_color_analysis import tone_analysis
from ShowMeTheColor.personal_color_analysis.detect_face import DetectFace
from ShowMeTheColor.personal_color_analysis.color_extract import DominantColors
from colormath.color_objects import LabColor, sRGBColor, HSVColor
from colormath.color_conversions import convert_color

import torch


def analysis(imgpath):
    #######################################
    #           Face detection            #
    #######################################
    df = DetectFace(imgpath)
    face = [df.left_cheek, df.right_cheek,
            df.left_eyebrow, df.right_eyebrow,
            df.left_eye, df.right_eye]

    #######################################
    #         Get Dominant Colors         #
    #######################################
    temp = []
    clusters = 4
    for f in face:
        dc = DominantColors(f, clusters)
        face_part_color, _ = dc.getHistogram()
        #dc.plotHistogram()
        temp.append(np.array(face_part_color[0]))
    cheek = np.mean([temp[0], temp[1]], axis=0)
    eyebrow = np.mean([temp[2], temp[3]], axis=0)
    eye = np.mean([temp[4], temp[5]], axis=0)

    Lab_b, hsv_s = [], []
    color = [cheek, eyebrow, eye]
    for i in range(3):
        rgb = sRGBColor(color[i][0], color[i][1], color[i][2], is_upscaled=True)
        lab = convert_color(rgb, LabColor, through_rgb_type=sRGBColor)
        hsv = convert_color(rgb, HSVColor, through_rgb_type=sRGBColor)
        Lab_b.append(float(format(lab.lab_b,".2f")))
        hsv_s.append(float(format(hsv.hsv_s,".2f"))*100)

    # print('Lab_b[skin, eyebrow, eye]',Lab_b)
    # print('hsv_s[skin, eyebrow, eye]',hsv_s)
    #######################################
    #      Personal color Analysis        #
    #######################################
    Lab_weight = [30, 20, 5]
    hsv_weight = [10, 1, 1]
    if(tone_analysis.is_warm(Lab_b, Lab_weight)):
        if(tone_analysis.is_spr(hsv_s, hsv_weight)):
            tone = 'Spring Warm Tone(spring)'
        else:
            tone = 'Fall Warm Tone(fall)'
    else:
        if(tone_analysis.is_smr(hsv_s, hsv_weight)):
            tone = 'Summer Cool Tone(summer)'
        else:
            tone = 'Winter Cool Tone(winter)'
    # Print Result

    print('{}의 퍼스널 컬러는 {}입니다.'.format(imgpath, tone))
    # sys.stdout = open('/home/bryan/Desktop/CS_LOG/Printed_results/color_reslut2222.txt', 'w')
    text = 'Your Personal Color is \n {}.'.format(tone)


    def prevpage():
        window.destroy()
        import page3

    def nextPage():
        window.destroy()
        import page4

    window = Tk()
    window.title('CS_PROJECT')
    window.geometry('1000x800')
    image = '/home/bryan/Desktop/CS_LOG/Pictures/four_season.png'
    image_spring = '/home/bryan/Desktop/CS_LOG/Pictures/spring.png'
    image_summer = '/home/bryan/Desktop/CS_LOG/Pictures/summer.png'
    image_fall = '/home/bryan/Desktop/CS_LOG/Pictures/fall.png'
    image_winter = '/home/bryan/Desktop/CS_LOG/Pictures/winter.png'
    background = PhotoImage(file=image)
    window['bg'] = 'orange'

    label = Label(window, image=background, relief=SUNKEN)
    label.pack(pady=20)

    if tone == 'Spring Warm Tone(spring)':
        bg_spring = PhotoImage(file=image_spring)
        label_spring = Label(window, image=bg_spring, relief=SUNKEN)
        label_spring.pack(pady=20)
        print('1')

    elif tone == 'Fall Warm Tone(fall)':
        bg_fall = PhotoImage(file=image_fall)
        label_fall = Label(window, image=bg_fall, relief=SUNKEN)
        label_fall.pack(pady=20)
        print('2')

    elif tone == 'Summer Cool Tone(summer)':
        bg_summer = PhotoImage(file=image_summer)
        label_summer = Label(window, image=bg_summer, relief=SUNKEN)
        label_summer.pack(pady=20)
        print('3')

    elif tone == 'Winter Cool Tone(winter)':
        bg_winter = PhotoImage(file=image_winter)
        label_winter = Label(window, image=bg_winter, relief=SUNKEN)
        label_winter.pack(pady=20)
        print('4')



    label1 = Label(window,
                   text=text,
                   font=('궁서체',30),
                   bg='orange', fg="blue")
    label1.pack(pady=30)

    b1 = Button(window, text='Go apply hair color!!', relief=RAISED, height=10, width=50, command=nextPage)
    b1.pack(side='right')

    b2 = Button(window, text='Go back', relief=RAISED, height=10, width=50, command=prevpage)
    b2.pack(side='left')


    window.mainloop()



