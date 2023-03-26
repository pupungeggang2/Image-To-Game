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
    var.screen = pygame.display.set_mode(const.window_size)
    pygame.display.set_caption('Image Game Converter')
    var.clock = pygame.time.Clock()

    load_font()
    load_image()

def load_font():
    pygame.font.init()
    var.Font.main = pygame.font.SysFont(None, 32)
    var.Font.title = pygame.font.SysFont(None, 24)

def load_image():
    pass

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

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            button = event.button

            if var.scene == 'edit':
                sceneedit.mouse_up(mouse[0], mouse[1], button)

        elif event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()

            if var.scene == 'edit':
                sceneedit.mouse_motion(mouse[0], mouse[1])

init()
main()