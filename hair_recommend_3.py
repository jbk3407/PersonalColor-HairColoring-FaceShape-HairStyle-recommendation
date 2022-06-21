import time
from tkinter import *

import cv2
import numpy as np  # for mathematical calculations
import dlib
import torch
from sklearn.cluster import KMeans
import math
from math import degrees
import keras
from wandb import keras
import tensorflow as tf
import sys

cap = cv2.VideoCapture(0)
a = cap.set(4, 640) #WIDTH
b = cap.set(4, 640) #HEIGHT

cap2 = cv2.VideoCapture(0)
c = cap.set(4, 640) #WIDTH
d = cap.set(4, 640) #HEIGHT

#얼굴 인식 캐스케이드 파일 읽는다
CASCADE = 'models/Face_cascade.xml'
predictor_path = "models/shape_predictor_81_face_landmarks.dat"
face_cascade = cv2.CascadeClassifier(CASCADE)
predictor = dlib.shape_predictor(predictor_path)

import os

def main():
    if os.path.exists('/home/bryan/Desktop/CS_LOG/Printed_results/face_shape.txt'):
        os.remove('/home/bryan/Desktop/CS_LOG/Printed_results/face_shape.txt')
    loopcount = 0

    while(loopcount<180):

        # frame 별로 capture 한다
        ret, frame = cap.read(image=None)
        frame = cv2.flip(frame, 1)
        # frame2 = cap2.read(image=None)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(gray, (3, 3), 0)

        faces = face_cascade.detectMultiScale(
            gauss,
            scaleFactor=1.05,
            minNeighbors=5,
            minSize=(100, 100),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

    #Drawing Lines using facelandmark
        for (x, y, w, h) in faces:
            # draw a rectangle around the faces
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
            detected_landmarks = predictor(frame, dlib_rect).parts()
            landmarks = np.matrix([[p.x, p.y] for p in detected_landmarks])


            # line 1
            # line_point_left = (landmarks[76, 0], landmarks[76, 1])
            # line_point_right = (landmarks[73, 0], landmarks[73, 1])
            #
            # line1 = np.subtract(line_point_left, line_point_right)[0]
            #
            # cv2.line(frame, line_point_left, line_point_right, color=(0, 255, 0), thickness=2)
            # cv2.putText(frame, ' Line 1', line_point_left, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
            #             color=(0, 255, 0),
            #             thickness=2)
            # cv2.circle(frame, line_point_left, 5, color=(255, 0, 0), thickness=-1)
            # cv2.circle(frame, line_point_right, 5, color=(255, 0, 0), thickness=-1)
            #
            # line 2
            line_point_left = (landmarks[1, 0], landmarks[1, 1])
            line_point_right = (landmarks[15, 0], landmarks[15, 1])

            line2 = np.subtract(line_point_right, line_point_left)[0]
            cv2.line(frame, line_point_left, line_point_right, color=(0, 255, 0), thickness=2)
            cv2.putText(frame, ' Line 2', line_point_left, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 255, 0),
                        thickness=2)
            cv2.circle(frame, line_point_left, 5, color=(255, 0, 0), thickness=-1)
            cv2.circle(frame, line_point_right, 5, color=(255, 0, 0), thickness=-1)

            ## Line 3
            line_point_left = (landmarks[3, 0], landmarks[3, 1])
            line_point_right = (landmarks[13, 0], landmarks[13, 1])
            line3 = np.subtract(line_point_right, line_point_left)[0]
            cv2.line(frame, line_point_left, line_point_right, color=(0, 255, 0), thickness=2)
            cv2.putText(frame, ' Line 3', line_point_left, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 255, 0),
                        thickness=2)
            cv2.circle(frame, line_point_left, 5, color=(255, 0, 0), thickness=-1)
            cv2.circle(frame, line_point_right, 5, color=(255, 0, 0), thickness=-1)

            # Line 4
            line_point_top = (landmarks[71, 0], landmarks[71, 1])
            line_point_bottom = (landmarks[8, 0], landmarks[8, 1])
            line4 = np.subtract(line_point_bottom, line_point_top)[1]



            cv2.line(frame, line_point_top, line_point_bottom, color=(0, 255, 0), thickness=2)
            cv2.putText(frame, ' Line 4', line_point_top, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 255, 0),
                        thickness=2)
            cv2.circle(frame, line_point_top, 5, color=(255, 0, 0), thickness=-1)
            cv2.circle(frame, line_point_bottom, 5, color=(255, 0, 0), thickness=-1)


    #######################################################################################
    #######################################################################################
            ax, ay = landmarks[1, 0], landmarks[1, 1]
            bx, by = landmarks[3, 0], landmarks[3, 1]
            cx, cy = landmarks[4, 0], landmarks[4, 1]
            dx, dy = landmarks[8, 0], landmarks[8, 1]

            # Line 5
            line_point_1 = (landmarks[14, 0], landmarks[14, 1])
            line_point_3 = (landmarks[12, 0], landmarks[12, 1])
            line5 = np.subtract(line_point_1, line_point_3)[1]

            cv2.line(frame, line_point_1, line_point_3, color=(0, 0, 255), thickness=2)
            cv2.putText(frame, ' Line 5', line_point_3, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 255, 0),
                        thickness=2)
            cv2.circle(frame, line_point_1, 5, color=(0, 255, 0), thickness=-1)
            cv2.circle(frame, line_point_3, 5, color=(0, 255, 0), thickness=-1)

            # Line 6
            line_point_4 = (landmarks[12, 0], landmarks[12, 1])
            line_point_8 = (landmarks[9, 0], landmarks[9, 1])
            line6 = np.subtract(line_point_4, line_point_8)[0]

            cv2.line(frame, line_point_4, line_point_8, color=(0, 0, 255), thickness=2)
            cv2.putText(frame, ' Line 6', line_point_8, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                        color=(0, 255, 0),
                        thickness=2)
            cv2.circle(frame, line_point_4, 5, color=(0, 255, 0), thickness=-1)
            cv2.circle(frame, line_point_8, 5, color=(0, 255, 0), thickness=-1)

    ###################################################################################################
    ###################################################################################################

            similarity = line3/line2

            # print(similarity)
            ovalsimilarity = line4/w
            # print(ovalsimilarity)

            alpha0 = math.atan2(cy - ay, cx - ax)
            alpha1 = math.atan2(dy - by, dx - bx)
            alpha = alpha1 - alpha0
            angle = abs(degrees(alpha))
            angle = 180 - angle

            sys.stdout = open('/home/bryan/Desktop/CS_LOG/Printed_results/face_shape.txt', 'a')
            # for i in range(1):

            if similarity > 0.91 and angle < 142:
                print('Square')
                break

            if 0.9 < similarity < 0.929:
                if ovalsimilarity > 1.08:
                    print('Round')
                    break

                elif 1.0 < ovalsimilarity < 1.08:
                    print('Oval')
                    break

                elif ovalsimilarity < 0.99:
                    print('Oblong')
                    break

            elif similarity < 0.905 and ovalsimilarity > 1:
                print('Heart')
                break

            sys.stdout.close()

        ######################################################################################################

    ######################################################################################################
        ## 화면에 출력한다

        cv2.imshow('hold still for 5seconds', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # time.sleep(0.001)
        loopcount = loopcount+1
        cv2.imwrite('/home/bryan/Desktop/CS_LOG/Pictures/shape_capture.png', frame)

    cap.release()
    cv2.destroyAllWindows()



from read_shape import get_most_shape


def new_page():

    def getpage5():
        window.destroy()
        import Hair_recommend_4

    shape = get_most_shape()

    window = Tk()
    window.title('CS_PROJECT \n Hair_recmmend_3')
    window.geometry('1000x1100')
    image = '/home/bryan/Desktop/CS_LOG/Pictures/shape_capture.png'
    window['bg'] = 'orange'

    background = PhotoImage(file=image)

    label1 = Label(window,
                   text='Your Face Shape is '+shape,
                   font=("궁서체", 30),
                   bg='orange', fg="blue")
    label1.pack()

    label = Label(window, image=background, relief=SUNKEN)
    label.pack(pady=20)

    b1 = Button(window, text='Get Recommendation', relief=RAISED, height=5, width=50, font=("궁서체", 15),command=getpage5)
    b1.pack(pady=20)

    b1 = Button(window, text='Go back', relief=RAISED, height=5, width=50, font=("궁서체", 15))
    b1.pack(pady=20)

    b4 = Button(window, text='First Page', relief=RAISED, height=5, width=50, font=("궁서체", 15),)
    b4.pack(pady=20)

    b3 = Button(window, text='EXIT', relief=RAISED, height=5, width=50, font=("궁서체", 15), command=window.quit)
    b3.pack(pady=20)

    window.mainloop()

# main()
# new_page()
