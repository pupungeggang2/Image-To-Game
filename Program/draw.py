import pygame

import UI

import var
import const

def draw_upper_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Upper_Bar.rect, 2)

def draw_message_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Message_Bar.rect, 2)

def draw_left_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.rect, 2)

def draw_game_screen_edit():
    pygame.draw.rect(var.screen, const.Color.black, UI.Game_Screen_Edit.rect, 2)

    if var.canvas_mode == 'draw':
        if var.Image_Editor.layer_visible['backgorund'] == True:
            var.screen.blit(var.Image_Editor.layer['background'], UI.Game_Screen_Edit.rect[:2])
        
        if var.Image_Editor.layer_visible['object'] == True:
            var.screen.blit(var.Image_Editor.layer['object'], UI.Game_Screen_Edit.rect[:2])

    elif var.canvas_mode == 'game':
        var.screen.blit(var.game_output, UI.Game_Screen_Edit.rect[:2])

def draw_lower_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Lower_Bar.rect, 2)