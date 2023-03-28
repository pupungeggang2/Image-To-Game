import pygame

import var
import const

import draw

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_upper_bar()
    draw.draw_message_bar()
    draw.draw_left_bar()
    draw.draw_game_screen_edit()
    draw.draw_lower_bar()
    pygame.display.flip()

def mouse_down(x, y, button):
    pass

def mouse_up(x, y, button):
    pass

def mouse_motion(x, y):
    pass