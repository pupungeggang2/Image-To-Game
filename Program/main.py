import pygame

import os
import sys

import asset
import var
import const

import sceneedit
import sceneplay

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(const.window_size, pygame.SRCALPHA)
    pygame.display.set_caption('Image Game Converter')
    var.Image_Editor.layer['background'] = pygame.Surface(const.canvas_size, pygame.SRCALPHA)
    var.Image_Editor.layer['object'] = pygame.Surface(const.canvas_size, pygame.SRCALPHA)
    var.Image_Editor.full_image = pygame.Surface(const.canvas_size, pygame.SRCALPHA)
    var.game_output = pygame.Surface(const.canvas_size, pygame.SRCALPHA)
    var.clock = pygame.time.Clock()

    load_font()
    load_image()

def load_font():
    pygame.font.init()
    var.Font.title = pygame.font.Font('Font/neodgm.ttf', 32)
    var.Font.main = pygame.font.Font('Font/neodgm.ttf', 24)

def load_image():
    asset.Img.Icon.new = pygame.image.load('Image/Icon/New.png')
    asset.Img.Icon.save = pygame.image.load('Image/Icon/Save.png')
    asset.Img.Icon.image_save = pygame.image.load('Image/Icon/ImageSave.png')
    asset.Img.Icon.layer_load = pygame.image.load('Image/Icon/LayerLoad.png')
    asset.Img.Icon.close = pygame.image.load('Image/Icon/Close.png')
    asset.Img.Icon.upper_directory = pygame.image.load('Image/Icon/UpperDirectory.png')
    asset.Img.Icon.visible = pygame.image.load('Image/Icon/Visible.png')
    asset.Img.Icon.invisible = pygame.image.load('Image/Icon/Invisible.png')

    asset.Img.Icon.prev = pygame.image.load('Image/Icon/Prev.png')
    asset.Img.Icon.next = pygame.image.load('Image/Icon/Next.png')

    asset.Img.Icon.brush = pygame.image.load('Image/Icon/Brush.png')
    asset.Img.Icon.erase = pygame.image.load('Image/Icon/Erase.png')
    asset.Img.Icon.convert = pygame.image.load('Image/Icon/Convert.png')
    asset.Img.Icon.play = pygame.image.load('Image/Icon/Play.png')

def main():
    while True:
        var.clock.tick(var.FPS)
        loop_scene()
        input_handle()

def loop_scene():
    if var.scene == 'edit':
        sceneedit.loop()

    elif var.scene == 'play':
        sceneplay.loop()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            button = event.button

            if var.scene == 'edit':
                sceneedit.mouse_down(mouse[0], mouse[1], button)

            elif var.scene == 'play':
                sceneplay.mouse_down(mouse[0], mouse[1], button)

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            button = event.button

            if var.scene == 'edit':
                sceneedit.mouse_up(mouse[0], mouse[1], button)

            if var.scene == 'play':
                sceneedit.mouse_up(mouse[0], mouse[1], button)

        elif event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()

            if var.scene == 'edit':
                sceneedit.mouse_motion(mouse[0], mouse[1])

            elif var.scene == 'play':
                sceneedit.mouse_motion(mouse[0], mouse[1])

        elif event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'edit':
                sceneedit.key_down(key)

            elif var.scene == 'play':
                sceneedit.key_down(key)

        elif event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'edit':
                sceneedit.key_up(key)

            elif var.scene == 'play':
                sceneedit.key_up(key)

init()
main()