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

    for i in range(15):
        for j in range(20):
            top = i * 40
            left = j * 40
            bottom = i * 40 + 40
            right = j * 40 + 40
            img_piece = img.crop((left, top, right, bottom))

def determine_image(img_piece):
    pass
