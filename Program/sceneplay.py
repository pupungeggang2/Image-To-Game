import pygame

import UI
import var
import const
import physics

import game
import draw

def loop():
    if var.state == 'play':
        var.Game.position_previous_frame = [int(var.Game.data_playing['player_position'][0]), int(var.Game.data_playing['player_position'][1])]
        game.player_move()
        game.player_coin_collect()

        if game.player_defeat_check() == True:
            var.state = 'defeat'
        elif game.player_win_check() == True:
            var.state = 'win'
        var.Game.position_current_frame = [int(var.Game.data_playing['player_position'][0]), int(var.Game.data_playing['player_position'][1])]

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

        elif physics.point_inside_rect_array(x, y, UI.Game.pause_button):
            if var.state == 'play':
                var.state = 'pause'

        elif physics.point_inside_rect_array(x, y, UI.Game.play_button):
            if var.state == 'pause':
                var.state = 'play'

def mouse_motion(x, y):
    pass

def key_down(key):
    if var.state == 'play':
        if key == pygame.K_w or key == pygame.K_UP:
            var.Game.keyboard['up'] = True

        if key == pygame.K_a or key == pygame.K_LEFT:
            var.Game.keyboard['left'] = True

        if key == pygame.K_s or key == pygame.K_DOWN:
            var.Game.keyboard['down'] = True

        if key == pygame.K_d or key == pygame.K_RIGHT:
            var.Game.keyboard['right'] = True

        if key == pygame.K_SPACE:
            game.try_jump()

        if key == pygame.K_UP:
            game.interact()

def key_up(key):
    if var.state == 'play':
        if key == pygame.K_w or key == pygame.K_UP:
            var.Game.keyboard['up'] = False

        if key == pygame.K_a or key == pygame.K_LEFT:
            var.Game.keyboard['left'] = False

        if key == pygame.K_s or key == pygame.K_DOWN:
            var.Game.keyboard['down'] = False

        if key == pygame.K_d or key == pygame.K_RIGHT:
            var.Game.keyboard['right'] = False