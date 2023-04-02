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
    # Brush size change
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.brush_point_rect, 2)
    pygame.draw.circle(var.screen, const.Color.black, UI.Left_Bar.brush_point, var.Image_Editor.brush_size / 2)
    pygame.draw.line(var.screen, const.Color.black, UI.Left_Bar.brush_size_slider[:2], UI.Left_Bar.brush_size_slider[2:], 10)
    var.screen.blit(var.Font.main.render(str(var.Image_Editor.brush_size), False, const.Color.black), UI.Left_Bar.brush_size_text)
    pygame.draw.circle(var.screen, const.Color.white, [UI.Left_Bar.brush_size_slider[0] + 300 / 39 * (var.Image_Editor.brush_size - 1), UI.Left_Bar.brush_size_slider[1]], 10)
    pygame.draw.circle(var.screen, const.Color.black, [UI.Left_Bar.brush_size_slider[0] + 300 / 39 * (var.Image_Editor.brush_size - 1), UI.Left_Bar.brush_size_slider[1]], 10, 2)

    # Brush color
    pygame.draw.rect(var.screen, var.Image_Editor.brush_color, UI.Left_Bar.brush_color_rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.brush_color_rect, 2)
    var.screen.blit(var.Font.title.render(convert_color_code_to_hex(var.Image_Editor.brush_color), False, const.Color.black), UI.Left_Bar.brush_color_code_text)

    var.screen.blit(var.Font.main.render('Red', False, const.Color.black), UI.Left_Bar.brush_color_red_text)
    pygame.draw.line(var.screen, const.Color.black, UI.Left_Bar.brush_color_red_slider[:2], UI.Left_Bar.brush_color_red_slider[2:], 10)
    pygame.draw.circle(var.screen, const.Color.white, [UI.Left_Bar.brush_color_red_slider[0] + 300 / 255 * (var.Image_Editor.brush_color[0]), UI.Left_Bar.brush_color_red_slider[1]], 10)
    pygame.draw.circle(var.screen, const.Color.black, [UI.Left_Bar.brush_color_red_slider[0] + 300 / 255 * (var.Image_Editor.brush_color[0]), UI.Left_Bar.brush_color_red_slider[1]], 10, 2)
    var.screen.blit(var.Font.main.render(str(var.Image_Editor.brush_color[0]), False, const.Color.black), UI.Left_Bar.brush_color_red_val_text)

    var.screen.blit(var.Font.main.render('Green', False, const.Color.black), UI.Left_Bar.brush_color_green_text)
    pygame.draw.line(var.screen, const.Color.black, UI.Left_Bar.brush_color_green_slider[:2], UI.Left_Bar.brush_color_green_slider[2:], 10)
    pygame.draw.circle(var.screen, const.Color.white, [UI.Left_Bar.brush_color_green_slider[0] + 300 / 255 * (var.Image_Editor.brush_color[1]), UI.Left_Bar.brush_color_green_slider[1]], 10)
    pygame.draw.circle(var.screen, const.Color.black, [UI.Left_Bar.brush_color_green_slider[0] + 300 / 255 * (var.Image_Editor.brush_color[1]), UI.Left_Bar.brush_color_green_slider[1]], 10, 2)
    var.screen.blit(var.Font.main.render(str(var.Image_Editor.brush_color[1]), False, const.Color.black), UI.Left_Bar.brush_color_green_val_text)

    var.screen.blit(var.Font.main.render('Blue', False, const.Color.black), UI.Left_Bar.brush_color_blue_text)
    pygame.draw.line(var.screen, const.Color.black, UI.Left_Bar.brush_color_blue_slider[:2], UI.Left_Bar.brush_color_blue_slider[2:], 10)
    pygame.draw.circle(var.screen, const.Color.white, [UI.Left_Bar.brush_color_blue_slider[0] + 300 / 255 * (var.Image_Editor.brush_color[2]), UI.Left_Bar.brush_color_blue_slider[1]], 10)
    pygame.draw.circle(var.screen, const.Color.black, [UI.Left_Bar.brush_color_blue_slider[0] + 300 / 255 * (var.Image_Editor.brush_color[2]), UI.Left_Bar.brush_color_blue_slider[1]], 10, 2)
    var.screen.blit(var.Font.main.render(str(var.Image_Editor.brush_color[2]), False, const.Color.black), UI.Left_Bar.brush_color_blue_val_text)

    # Color picker
    for i in range(len(const.Color.color_list)):
        row = i // 8
        column = i % 8

        pygame.draw.rect(var.screen, const.Color.color_list[i], [UI.Left_Bar.color_picker[0] + column * UI.Left_Bar.color_picker_rect_size[0], UI.Left_Bar.color_picker[1] + row * UI.Left_Bar.color_picker_rect_size[1], UI.Left_Bar.color_picker_rect_size[0], UI.Left_Bar.color_picker_rect_size[1]])

    # Layer
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_object_rect, 2)
    var.screen.blit(var.Font.main.render('Object', False, const.Color.black), UI.Left_Bar.layer_object_text)
    var.screen.blit(asset.Img.Icon.erase, UI.Left_Bar.layer_object_erase)
    var.screen.blit(asset.Img.Icon.layer_load, UI.Left_Bar.layer_object_load)

    if var.Image_Editor.layer_visible['object'] == True:
        var.screen.blit(asset.Img.Icon.visible, UI.Left_Bar.layer_object_visible)

    elif var.Image_Editor.layer_visible['object'] == False:
        var.screen.blit(asset.Img.Icon.invisible, UI.Left_Bar.layer_object_visible)

    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_background_rect, 2)
    var.screen.blit(var.Font.main.render('Background', False, const.Color.black), UI.Left_Bar.layer_background_text)
    var.screen.blit(asset.Img.Icon.erase, UI.Left_Bar.layer_background_erase)
    var.screen.blit(asset.Img.Icon.layer_load, UI.Left_Bar.layer_background_load)

    if var.Image_Editor.layer_visible['background'] == True:
        var.screen.blit(asset.Img.Icon.visible, UI.Left_Bar.layer_background_visible)

    elif var.Image_Editor.layer_visible['background'] == False:
        var.screen.blit(asset.Img.Icon.invisible, UI.Left_Bar.layer_background_visible)

    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_player_rect, 2)
    var.screen.blit(var.Font.main.render('Player', False, const.Color.black), UI.Left_Bar.layer_player_text)

    if var.Image_Editor.layer_visible['player'] == True:
        var.screen.blit(asset.Img.Icon.visible, UI.Left_Bar.layer_player_visible)

    elif var.Image_Editor.layer_visible['player'] == False:
        var.screen.blit(asset.Img.Icon.invisible, UI.Left_Bar.layer_player_visible)

    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.layer_white_rect, 2)
    var.screen.blit(var.Font.main.render('White', False, const.Color.black), UI.Left_Bar.layer_white_text)

    if var.Image_Editor.layer_visible['white'] == True:
        var.screen.blit(asset.Img.Icon.visible, UI.Left_Bar.layer_white_visible)

    elif var.Image_Editor.layer_visible['white'] == False:
        var.screen.blit(asset.Img.Icon.invisible, UI.Left_Bar.layer_white_visible)

    if var.Image_Editor.layer_selected == 'background':
        pygame.draw.rect(var.screen, const.Color.green, UI.Left_Bar.layer_background_rect, 2)

    if var.Image_Editor.layer_selected == 'object':
        pygame.draw.rect(var.screen, const.Color.green, UI.Left_Bar.layer_object_rect, 2)

    # Border
    pygame.draw.rect(var.screen, const.Color.black, UI.Left_Bar.rect, 2)

def draw_game_screen_edit():
    if var.Image_Editor.canvas_mode == 'draw':
        if var.Image_Editor.layer_visible['background'] == True:
            var.screen.blit(var.Image_Editor.layer['background'], UI.Game_Screen_Edit.rect[:2])
        
        if var.Image_Editor.layer_visible['object'] == True:
            var.screen.blit(var.Image_Editor.layer['object'], UI.Game_Screen_Edit.rect[:2])

    elif var.Image_Editor.canvas_mode == 'game':
        var.screen.blit(var.game_output, UI.Game_Screen_Edit.rect[:2])

    pygame.draw.rect(var.screen, const.Color.black, UI.Game_Screen_Edit.rect, 2)

def draw_lower_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Lower_Bar.rect, 2)

def draw_save_image_window():
    # Upper Bar
    pygame.draw.rect(var.screen, const.Color.white, UI.Save_Window.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.title_bar, 2)
    var.screen.blit(var.Font.title.render('Save', False, const.Color.black), UI.Save_Window.title_text)
    var.screen.blit(asset.Img.Icon.close, UI.Save_Window.close_button)

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

    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.rect, 2)

def draw_layer_load_window():
    # Upper Bar
    pygame.draw.rect(var.screen, const.Color.white, UI.Load_Window.rect)
    pygame.draw.rect(var.screen, const.Color.white, UI.Load_Window.title_bar, 2)
    var.screen.blit(var.Font.title.render('Load Image', False, const.Color.black), UI.Load_Window.title_text)
    var.screen.blit(asset.Img.Icon.close, UI.Load_Window.close_button)

    # Directory Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.directory_bar, 2)
    var.screen.blit(var.Font.main.render('.../dir/Input/' + var.Save.current_dir, False, const.Color.black), UI.Load_Window.directory_text)

    # Lower Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.load_button, 2)
    var.screen.blit(var.Font.title.render('Load', False, const.Color.black), UI.Load_Window.load_text)

    pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.rect, 2)

def convert_color_code_to_hex(color):
    color_code = '#'
    hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for i in range(3):
        front = color[i] // 16
        back = color[i] % 16
        color_code += hex_num[front]
        color_code += hex_num[back]

    return color_code