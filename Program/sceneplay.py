import pygame

import var
import const

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    pygame.display.flip()