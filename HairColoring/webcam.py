import cv2
import torch
import os
import numpy as np
import argparse
from PIL import Image

from HairColoring.models import modelv1
from HairColoring.models import modelv2



def get_mask(image, net, size=224):
    # print('image type',type(image))
    image_h, image_w = image.shape[0], image.shape[1]
    # print(image.shape)
    # print('image h w',image_h, image_w)

    down_size_image = cv2.resize(image, (size, size)) #(480,640,3) --> (224,224,3)
    down_size_image = cv2.cvtColor(down_size_image, cv2.COLOR_BGR2RGB)
    down_size_image = torch.from_numpy(down_size_image).float().div(255.0).unsqueeze(0)
    down_size_image = np.transpose(down_size_image, (0, 3, 1, 2)).to(device)
    mask: torch.nn.Module = net(down_size_image)

    # mask = torch.squeeze(mask[:, 1, :, :])
    mask = mask.argmax(dim=1).squeeze()
    mask_cv2 = mask.data.cpu().numpy() * 255
    mask_cv2 = mask_cv2.astype(np.uint8)
    mask_cv2 = cv2.resize(mask_cv2, (image_w, image_h))

    return mask_cv2

def load_model(model_path,  device=torch.device('cpu')):

    print('check:', os.path.exists(model_path))
    print(f'[*] Load Model from {model_path} / device: {device}')
    # save_info = {'model': net, 'state_dict': net.state_dict(), 'optimizer' : optimizer.state_dict()}

    net = modelv2.MobileHairNetV2()
    net.load_state_dict(torch.load(model_path)['state_dict'])
    net.cuda()

    # save_info = torch.load(model_path, map_location=device)
    # net = save_info['model']
    # net.load_state_dict(save_info['state_dict'])

    return net


def alpha_image1(image, mask, alpha=0.1):
    color = np.zeros((mask.shape[0], mask.shape[1], 3))
    color[np.where(mask != 0)] = [0, 130, 255] # BGR
    # color[np.where(mask != 0)] = [0, 200, 255] # blonde
    alpha_hand = ((1 - alpha) * image + alpha * color).astype(np.uint8)
    alpha_hand = cv2.bitwise_and(alpha_hand, alpha_hand, mask=mask)

    # cv2.imshow('wetew',cv2.add(alpha_hand, image))
    return cv2.add(alpha_hand, image)

def alpha_image2(image, mask, alpha=0.1):
    color = np.zeros((mask.shape[0], mask.shape[1], 3))
    # color[np.where(mask != 0)] = [0, 130, 255] # BGR
    color[np.where(mask != 0)] = [0, 200, 255] # blonde
    alpha_hand = ((1 - alpha) * image + alpha * color).astype(np.uint8)
    alpha_hand = cv2.bitwise_and(alpha_hand, alpha_hand, mask=mask)

    # cv2.imshow('wetew',cv2.add(alpha_hand, image))
    return cv2.add(alpha_hand, image)

def string_to_array(img_path):
    img = Image.open(img_path)
    numpy_data = np.asarray(img)

    return numpy_data

def main():

        cam = cv2.VideoCapture(0)


        if not cam.isOpened():
            raise Exception("webcam is not detected")

        while (True):
            # ret : frame capture결과(boolean)
            # frame : Capture한 frame

            ret, frame = cam.read()

            if (ret):
                mask = get_mask(frame, net)
                add1 = alpha_image1(frame, mask)
                add2 = alpha_image2(frame, mask)

                both = np.concatenate((frame, add1, add2), axis=1)

                cv2.imshow('both', both)
                # cv2.imshow('add', add)
                # cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        cam.release()
        cv2.destroyAllWindows()




print('+++', os.getcwd())

# model_path = f'param/best.pt'
model_path = 'jbk_yc.tar' # '../hair_coloring_best.pt'

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
net = load_model(model_path, device)

print('탈출')

# main()
