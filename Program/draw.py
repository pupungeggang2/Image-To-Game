import pygame

import UI
import asset

import var
import const

def draw_upper_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Upper_Bar.rect, 2)
    var.screen.blit(asset.Img.Icon.new, UI.Upper_Bar.new)
    var.screen.blit(asset.Img.Icon.save, UI.Upper_Bar.save)
    var.screen.blit(asset.Img.Icon.image_save, UI.Upper_Bar.image_save)
    var.screen.blit(asset.Img.Icon.brush, UI.Upper_Bar.brush)
    var.screen.blit(asset.Img.Icon.erase, UI.Upper_Bar.erase)
    var.screen.blit(asset.Img.Icon.convert, UI.Upper_Bar.convert)
    var.screen.blit(asset.Img.Icon.play, UI.Upper_Bar.play)

def draw_message_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Message_Bar.rect, 2)

def draw_left_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.rect, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.brush_point_rect, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.brush_size_slider, 2)

def draw_game_screen_edit():
    pygame.draw.rect(var.screen, const.Color.black, UI.Game_Screen_Edit.rect, 2)

    if var.Image_Editor.canvas_mode == 'draw':
        if var.Image_Editor.layer_visible['background'] == True:
            var.screen.blit(var.Image_Editor.layer['background'], UI.Game_Screen_Edit.rect[:2])
        
        if var.Image_Editor.layer_visible['object'] == True:
            var.screen.blit(var.Image_Editor.layer['object'], UI.Game_Screen_Edit.rect[:2])

    elif var.Image_Editor.canvas_mode == 'game':
        var.screen.blit(var.game_output, UI.Game_Screen_Edit.rect[:2])

def draw_lower_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Lower_Bar.rect, 2)