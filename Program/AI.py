import os
import pandas as pd
from PIL import Image

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score,recall_score, f1_score
from sklearn.metrics import confusion_matrix
from collections import Counter

import json

import pygame

import var
import const

df_color = None
df_object = None

logreg_color = None
logreg_object = None

def AI_init():
    global df_color
    global df_object

    df_color = pd.read_csv('Data/color_data.csv')
    df_object = None

def convert_image_to_game():
    var.Game.data_level['start_position'] = [var.Image_Editor.start_position[0], var.Image_Editor.start_position[1]]

    pygame.image.save(var.Image_Editor.layer['object'], 'Temp.png')
    img = Image.open('Temp.png')
    img_pieces = slice_image(img, 0)

    converted_game = json.loads(json.dumps(const.zero_game_file))
    converted_game['start_position'] = [var.Image_Editor.start_position[0], var.Image_Editor.start_position[1]]

    make_model_color()
    make_model_object()

    for i in range(300):
        row = i // 20
        column = i % 20
        img_pieces_pixels = list(img_pieces[i].getdata())

        # Determining whether the image is void
        if find_void_percentage(img_pieces_pixels) > 75:
            converted_game['block'][row][column] = 0
            converted_game['wall'][row][column] = 0
            
        elif find_void_percentage(img_pieces_pixels) < 20:
            block = determine_block(img_pieces_pixels)
            converted_game['block'][row][column] = block

            if block != 0:
                converted_game['wall'][row][column] = 1
            else:
                converted_game['wall'][row][column] = 0

        else:
            determine_thing(img_pieces_pixels)

    var.Game.data_level = json.loads(json.dumps(converted_game))

def make_model_color():
    global df_color
    global logreg_color

    X = df_color[df_color.columns[0:3]]
    y = df_color[df_color.columns[3]]
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state = 289)

    logreg_color = LogisticRegression(solver= 'lbfgs',max_iter=400)
    logreg_color.fit(X_train, y_train)

def make_model_object():
    pass

def determine_block(img_piece):
    global logreg_color

    color_pixels = []
    duplicate = False
    
    for i in range(len(img_piece)):
        if img_piece[i][3] != 0:
            duplicate = False
            color_pixel = [img_piece[i][0], img_piece[i][1], img_piece[i][2]]

            for j in range(len(color_pixels)):
                if color_pixel[0] == color_pixels[j][1][0] and color_pixel[1] == color_pixels[j][1][1] and color_pixel[2] == color_pixels[j][1][2]:
                    color_pixels[j][0] += 1
                    duplicate = True
                    break

            if duplicate == False:
                color_pixels.append([0, [color_pixel[0], color_pixel[1], color_pixel[2]]])

    color_pixels.sort()
    color_pixels.reverse()

    if len(color_pixels) > 5:
        color_pixels = color_pixels[:5]
    
    color_top_five = []

    for i in range(len(color_pixels)):
        color = logreg_color.predict(pd.DataFrame([[color_pixels[i][1][0], color_pixels[i][1][1], color_pixels[i][1][2]]], columns=["Red", "Green", "Blue"]))[0]
        color_top_five.append(color)

    for j in range(len(color_pixels), 5):
        color_top_five.append('None')

    if color_top_five[0] == 'Yellow':
        return 3
    elif color_top_five[0] == 'LightBlue':
        return 4
    elif color_top_five[0] == 'Green':
        return 2
    elif color_top_five[0] == 'Brown':
        if 'Green' in color_top_five:
            return 2
        else:
            return 1
    return 0

def determine_thing(img_piece):
    pass

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
