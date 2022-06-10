from ShowMeTheColor.personal_color_analysis import personal_color

captured_image = '/home/bryan/Desktop/CS_LOG/Pictures/captured_image.png'

def main():
    # 인자값 받을 인스턴스 생성
    # parser = argparse.ArgumentParser(description = 'Please input your image.')
    #
    # # 입력받을 인자값 등록
    # parser.add_argument('--image', required = False, help='input .jpg or .png file')
    # parser.add_argument('--dir', required = False, help='input image directory')
    #
    # # 입력받은 인자값을 args에 저장
    # args = parser.parse_args()

    #################################
     #       a single image         #
    #################################
    # if args.image != None:
    #     imgpath = args.image
    #     # imgpath = captured_image
    #     personal_color.analysis(imgpath)

    personal_color.analysis(captured_image)
    ##################################
    #  multiple images in directory  #
    ##################################
    # elif args.dir != None:
    #     dirpath = args.dir
    #     imgs = os.listdir(dirpath)
    #     for imgpath in imgs:
    #         #print(os.path.join(dirpath, imgpath))
    #         personal_color.analysis(os.path.join(dirpath, imgpath))

# def webcam():
#     cam = cv2.VideoCapture(0)
#     while (True):
#         # ret : frame capture결과(boolean)
#         # frame : Capture한 frame
#
#         ret, frame = cam.read()
#         if (ret):
#             cv2.imshow('Space to capture / Esc to exit', frame)
#             k = cv2.waitKey(1)
#             if k % 256 == 27:
#                 # ESC pressed
#                 print("Escape hit, closing...")
#                 break
#             elif k % 256 == 32:
#                 # SPACE pressed
#                 img_name = "captured_image.png"
#                 captured_image = cv2.imwrite('/home/bryan/Pictures/' + img_name, frame)
#                 print("{} written!".format(img_name))
#
#     cam.release()
#     cv2.destroyAllWindows()



if __name__ == '__main__':

    # webcam()
    main()
    # main()

