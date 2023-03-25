import pygame

import os
import sys

import var
import const

import sceneedit

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(const.window_size)
    pygame.display.set_caption('Image Game Converter')

def main():
    while True:
        loop_scene()
        input_handle()

def loop_scene():
    pass

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

init()
main()