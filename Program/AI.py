import os
import pandas as pd
from PIL import Image
from sklearn import linear_model
import json

import pygame

import var
import const

data_color = None
data_object = None

def AI_init():
    data_color = pd.read_csv('Data/color_data.csv')
    data_object = None

def convert_image_to_game():
    var.Game.data_level['start_position'] = [var.Image_Editor.start_position[0], var.Image_Editor.start_position[1]]

    pygame.image.save(var.Image_Editor.layer['object'], 'Temp.png')
    img = Image.open('Temp.png')
    img_pieces = slice_image(img, 0)

    converted_game = json.loads(json.dumps(const.zero_game_file))
    converted_game['start_position'] = [var.Image_Editor.start_position[0], var.Image_Editor.start_position[1]]

    for i in range(300):
        row = i // 20
        column = i % 20
        img_pieces_pixels = list(img_pieces[i].getdata())

        # Determining whether the image is void
        if find_void_percentage(img_pieces_pixels) > 80:
            converted_game['block'][row][column] = 0
            converted_game['wall'][row][column] = 0
            
        elif find_void_percentage(img_pieces_pixels) < 20:
            determine_block(img_pieces_pixels)

        else:
            determine_thing(img_pieces_pixels)
            pass

    var.Game.data_level = json.loads(json.dumps(converted_game))

def slice_image(img, save):
    img_pieces = []

    for i in range(15):
        for j in range(20):
            top = i * 40
            left = j * 40
            bottom = i * 40 + 40
            right = j * 40 + 40
            img_pieces.append(img.crop((left, top, right, bottom)))

    if save == 1:
        for i in range(300):
            img_pieces[i].save('./Slice/Temp' + 'R' + str(i // 20) + 'C' + str(i % 20) + '.png')

    return img_pieces

def find_void_percentage(img_pixels):
    num_of_pixels = len(img_pixels)
    num_of_void_pixels = 0

    for i in range(num_of_pixels):
        if img_pixels[i][3] == 0:
            num_of_void_pixels += 1

    return(num_of_void_pixels / num_of_pixels * 100)

def determine_block(img_piece):
    pass

def determine_thing(img_piece):
    pass
