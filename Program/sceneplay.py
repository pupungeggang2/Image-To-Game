import pygame

import UI
import var
import const
import physics

import game
import draw

def loop():
    if var.state == 'play':
        game.player_move()

        if game.player_defeat_check() == True:
            var.state = 'win'
        elif game.player_win_check() == True:
            var.state = 'defeat'

    display()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_upper_bar_play()
    draw.draw_game_screen_play()
    pygame.display.flip()

def mouse_down(x, y, button):
    pass

def mouse_up(x, y, button):
    if button == 1:
        if physics.point_inside_rect_array(x, y, UI.Game.stop_button):
            var.scene = 'edit'
            var.state = ''

def mouse_motion(x, y):
    pass

def key_down(key):
    if var.state == 'play':
        if key == pygame.K_w:
            var.Game.keyboard['up'] = True

        if key == pygame.K_a:
            var.Game.keyboard['left'] = True

        if key == pygame.K_s:
            var.Game.keyboard['down'] = True

        if key == pygame.K_d:
            var.Game.keyboard['right'] = True

def key_up(key):
    if var.state == 'play':
        if key == pygame.K_w:
            var.Game.keyboard['up'] = False

        if key == pygame.K_a:
            var.Game.keyboard['left'] = False

        if key == pygame.K_s:
            var.Game.keyboard['down'] = False

        if key == pygame.K_d:
            var.Game.keyboard['right'] = False