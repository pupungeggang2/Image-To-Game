import os
import pandas
from PIL import Image
from sklearn import linear_model

import pygame

import var

def AI_init():
    pass

def convert_image_to_game():
    var.Game.data_level['start_position'] = [var.Image_Editor.start_position[0], var.Image_Editor.start_position[1]]

    pygame.image.save(var.Image_Editor.layer['object'], 'Temp.png')
    img = Image.open('Temp.png')

    img_pieces = slice_image(img, 1)

def slice_image(img, save):
    img_pieces = []

    for i in range(15):
        for j in range(20):
            top = i * 40
            left = j * 40
            bottom = i * 40 + 40
            right = j * 40 + 40
            img_pieces.append(img.crop((left, top, right, bottom)))

    print(len(img_pieces))

    if save == 1:
        for i in range(300):
            img_pieces[i].save('./Slice/Temp' + 'R' + str(i // 20) + 'C' + str(i % 20) + '.png')

    return img_pieces

def determine_image(img_piece):
    pass
