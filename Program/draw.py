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

    if var.Image_Editor.brush_mode == 'draw':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.brush, 2)

    elif var.Image_Editor.brush_mode == 'erase':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.erase, 2)

def draw_message_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Message_Bar.rect, 2)

def draw_left_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.rect, 2)

    # Brush size change
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.brush_point_rect, 2)
    pygame.draw.circle(var.screen, const.Color.black, UI.Left_Bar.brush_point, var.Image_Editor.brush_size / 2)
    pygame.draw.line(var.screen, const.Color.black, UI.Left_Bar.brush_size_slider[:2], UI.Left_Bar.brush_size_slider[2:], 10)
    var.screen.blit(var.Font.main.render(str(var.Image_Editor.brush_size), False, const.Color.black), UI.Left_Bar.brush_size_text)
    pygame.draw.circle(var.screen, const.Color.white, [UI.Left_Bar.brush_size_slider[0] + 300 / 19 * (var.Image_Editor.brush_size - 1), UI.Left_Bar.brush_size_slider[1]], 10)
    pygame.draw.circle(var.screen, const.Color.black, [UI.Left_Bar.brush_size_slider[0] + 300 / 19 * (var.Image_Editor.brush_size - 1), UI.Left_Bar.brush_size_slider[1]], 10, 2)

    # Layer
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_object_rect, 2)
    var.screen.blit(var.Font.main.render('Object', False, const.Color.black), UI.Left_Bar.layer_object_text)
    var.screen.blit(asset.Img.Icon.erase, UI.Left_Bar.layer_object_erase)
    var.screen.blit(asset.Img.Icon.layer_load, UI.Left_Bar.layer_object_load)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_background_rect, 2)
    var.screen.blit(var.Font.main.render('Background', False, const.Color.black), UI.Left_Bar.layer_background_text)
    var.screen.blit(asset.Img.Icon.erase, UI.Left_Bar.layer_background_erase)
    var.screen.blit(asset.Img.Icon.layer_load, UI.Left_Bar.layer_background_load)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_player_rect, 2)
    var.screen.blit(var.Font.main.render('Player', False, const.Color.black), UI.Left_Bar.layer_player_text)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_white_rect, 2)
    var.screen.blit(var.Font.main.render('White', False, const.Color.black), UI.Left_Bar.layer_white_text)

    if var.Image_Editor.layer_selected == 'background':
        pygame.draw.rect(var.screen, const.Color.green, UI.Left_Bar.layer_background_rect, 2)

    if var.Image_Editor.layer_selected == 'object':
        pygame.draw.rect(var.screen, const.Color.green, UI.Left_Bar.layer_object_rect, 2)

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

def draw_save_image_window():
    pygame.draw.rect(var.screen, const.Color.white, UI.Save_Window.rect)

    # Upper Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.rect, 2)
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.title_bar, 2)
    var.screen.blit(asset.Img.Icon.close, UI.Save_Window.close_button)
    var.screen.blit(var.Font.title.render('Save', False, const.Color.black), UI.Save_Window.title_text)

    # Directory Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.directory_bar, 2)
    var.screen.blit(var.Font.main.render('.../dir/Drawing/' + var.Save.current_dir, False, const.Color.black), UI.Save_Window.directory_text)

    # Lower Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.lower_text_rect, 2)
    
    if var.Save.file_name_mode == True:
        pygame.draw.rect(var.screen, const.Color.green, UI.Save_Window.lower_text_rect, 2)

    var.screen.blit(var.Font.main.render(var.Save.file_name_write, False, const.Color.black), UI.Save_Window.file_name)

    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.save_button, 2)
    var.screen.blit(var.Font.title.render('Save', False, const.Color.black), UI.Save_Window.save_text)

def draw_load_window():
    pass
