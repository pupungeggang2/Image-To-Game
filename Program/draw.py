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
    var.screen.blit(asset.Img.Icon.move, UI.Upper_Bar.move)
    var.screen.blit(asset.Img.Icon.palette, UI.Upper_Bar.palette)
    var.screen.blit(asset.Img.Icon.game, UI.Upper_Bar.game)
    var.screen.blit(asset.Img.Icon.convert, UI.Upper_Bar.convert)
    var.screen.blit(asset.Img.Icon.play, UI.Upper_Bar.play)

    if var.Image_Editor.brush_mode == 'draw':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.brush, 2)

    elif var.Image_Editor.brush_mode == 'erase':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.erase, 2)

    elif var.Image_Editor.brush_mode == 'move':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.move, 2)

    if var.Image_Editor.canvas_mode == 'draw':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.palette, 2)

    elif var.Image_Editor.canvas_mode == 'game':
        pygame.draw.rect(var.screen, const.Color.green, UI.Upper_Bar.game, 2)

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

        if var.Image_Editor.layer_visible['player'] == True:
            var.screen.blit(asset.Img.player, [UI.Game_Screen_Edit.rect[0] + var.Image_Editor.start_position[0] - 16, UI.Game_Screen_Edit.rect[1] + var.Image_Editor.start_position[1] - 16])

    elif var.Image_Editor.canvas_mode == 'game':
        draw_game_file(var.Game.data_level)

    draw_grid()

    pygame.draw.rect(var.screen, const.Color.black, UI.Game_Screen_Edit.rect, 2)

def draw_grid():
    for i in range(19):
        pygame.draw.line(var.screen, const.Color.gray, [UI.Game_Screen_Edit.rect[0] + 40 * i + 40, UI.Game_Screen_Edit.rect[1]], [UI.Game_Screen_Edit.rect[0] + 40 * i + 40, UI.Game_Screen_Edit.rect[1] + UI.Game_Screen_Edit.rect[3]], 1)

    for i in range(14):
        pygame.draw.line(var.screen, const.Color.gray, [UI.Game_Screen_Edit.rect[0], UI.Game_Screen_Edit.rect[1] + i * 40 + 40], [UI.Game_Screen_Edit.rect[0] + UI.Game_Screen_Edit.rect[2], UI.Game_Screen_Edit.rect[1] + i * 40 + 40], 1)

def draw_game_file(game_file):
    var.screen.blit(var.Image_Editor.layer['background'], UI.Game_Screen_Edit.rect[:2])

    for i in range(15):
        for j in range(20):
            if var.Game.data_level['block'][i][j] != 0:
                var.screen.blit(asset.Img.block[var.Game.data_level['block'][i][j]], [UI.Game_Screen_Edit.rect[0] + j * 40, UI.Game_Screen_Edit.rect[1] + i * 40])

    for i in range(len(var.Game.data_level['thing'])):
        var.screen.blit(asset.Img.thing[var.Game.data_level['thing'][i][0]], [UI.Game_Screen_Edit.rect[0] + var.Game.data_level['thing'][i][1], UI.Game_Screen_Edit.rect[1] + var.Game.data_level['thing'][i][2]])

    var.screen.blit(asset.Img.player, [UI.Game_Screen_Edit.rect[0] + var.Game.data_level['start_position'][0] - 16, UI.Game_Screen_Edit.rect[1] + var.Game.data_level['start_position'][1] - 16])

def draw_lower_bar():
    pygame.draw.rect(var.screen, const.Color.black, UI.Lower_Bar.rect, 2)
    var.screen.blit(var.Font.title.render(var.Image_Editor.brush_mode + ' / ' + var.Image_Editor.canvas_mode, const.Color.black, False), UI.Lower_Bar.text_status)

def draw_save_image_window():
    # Upper Bar
    pygame.draw.rect(var.screen, const.Color.white, UI.Save_Window.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.title_bar, 2)
    var.screen.blit(var.Font.title.render('Save', False, const.Color.black), UI.Save_Window.title_text)
    var.screen.blit(asset.Img.Icon.close, UI.Save_Window.close_button)

    # Directory Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.directory_bar, 2)
    var.screen.blit(var.Font.main.render('.../dir/Drawing/' + var.Save.current_dir, False, const.Color.black), UI.Save_Window.directory_text)

    # Center
    for i in range(20):
        if var.Save.file_list_page * 20 + i < len(var.Save.current_dir_files):
            var.screen.blit(var.Font.main.render(var.Save.current_dir_files[var.Save.file_list_page * 20 + i], False, const.Color.black), [UI.Save_Window.file_list[i][0] + 8, UI.Save_Window.file_list[i][1] + 8])

    var.screen.blit(asset.Img.Icon.prev, UI.Save_Window.file_list_prev_button)
    var.screen.blit(asset.Img.Icon.next, UI.Save_Window.file_list_next_button)
    var.screen.blit(var.Font.title.render(str(var.Save.file_list_page + 1) + '/' + str((len(var.Save.current_dir_files) - 1) // 20 + 1), False, const.Color.black), UI.Save_Window.file_list_page_text)

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

    # Center
    if var.Load.file_list_selected > -1:
        pygame.draw.rect(var.screen, const.Color.green, UI.Load_Window.file_list[var.Load.file_list_selected], 2)

    for i in range(20):
        if var.Load.file_list_page * 20 + i < len(var.Load.current_dir_files):
            var.screen.blit(var.Font.main.render(var.Load.current_dir_files[var.Load.file_list_page * 20 + i], False, const.Color.black), [UI.Load_Window.file_list[i][0] + 8, UI.Load_Window.file_list[i][1] + 8])

    var.screen.blit(asset.Img.Icon.prev, UI.Load_Window.file_list_prev_button)
    var.screen.blit(asset.Img.Icon.next, UI.Load_Window.file_list_next_button)
    var.screen.blit(var.Font.title.render(str(var.Load.file_list_page + 1) + '/' + str((len(var.Load.current_dir_files) - 1) // 20 + 1), False, const.Color.black), UI.Load_Window.file_list_page_text)

    # Lower Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.load_button, 2)
    var.screen.blit(var.Font.title.render('Load', False, const.Color.black), UI.Load_Window.load_text)

    pygame.draw.rect(var.screen, const.Color.black, UI.Load_Window.rect, 2)

def draw_game_file_save():
    # Upper Bar
    pygame.draw.rect(var.screen, const.Color.white, UI.Save_Window.rect)
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.title_bar, 2)
    var.screen.blit(var.Font.title.render('Save', False, const.Color.black), UI.Save_Window.title_text)
    var.screen.blit(asset.Img.Icon.close, UI.Save_Window.close_button)

    # Directory Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.directory_bar, 2)
    var.screen.blit(var.Font.main.render('.../dir/Drawing/' + var.Save.current_dir, False, const.Color.black), UI.Save_Window.directory_text)

    # Center
    for i in range(20):
        if var.Save.file_list_page * 20 + i < len(var.Save.current_dir_files):
            var.screen.blit(var.Font.main.render(var.Save.current_dir_files[var.Save.file_list_page * 20 + i], False, const.Color.black), [UI.Save_Window.file_list[i][0] + 8, UI.Save_Window.file_list[i][1] + 8])

    var.screen.blit(asset.Img.Icon.prev, UI.Save_Window.file_list_prev_button)
    var.screen.blit(asset.Img.Icon.next, UI.Save_Window.file_list_next_button)
    var.screen.blit(var.Font.title.render(str(var.Save.file_list_page + 1) + '/' + str((len(var.Save.current_dir_files) - 1) // 20 + 1), False, const.Color.black), UI.Save_Window.file_list_page_text)

    # Lower Bar
    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.lower_text_rect, 2)
    
    if var.Save.file_name_mode == True:
        pygame.draw.rect(var.screen, const.Color.green, UI.Save_Window.lower_text_rect, 2)

    var.screen.blit(var.Font.main.render(var.Save.file_name_write, False, const.Color.black), UI.Save_Window.file_name)

    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.save_button, 2)
    var.screen.blit(var.Font.title.render('Save', False, const.Color.black), UI.Save_Window.save_text)

    pygame.draw.rect(var.screen, const.Color.black, UI.Save_Window.rect, 2)

def draw_upper_bar_play():
    var.screen.blit(asset.Img.Icon.play, UI.Game.play_button)
    var.screen.blit(asset.Img.Icon.pause, UI.Game.pause_button)
    var.screen.blit(asset.Img.Icon.stop, UI.Game.stop_button)

def draw_game_screen_play():
    var.screen.blit(var.Image_Editor.layer['background'], UI.Game.screen[:2])

    if var.state == 'win':
        var.screen.blit(var.Font.title.render('You Win!', False, const.Color.black), UI.Game.status_text)

    elif var.state == 'defeat':
        var.screen.blit(var.Font.title.render('You Lose!', False, const.Color.black), UI.Game.status_text)

    elif var.state == 'pause':
        var.screen.blit(var.Font.title.render('Paused', False, const.Color.black), UI.Game.status_text)

    var.screen.blit(asset.Img.thing[1], UI.Game.coin_icon)
    var.screen.blit(var.Font.title.render(str(var.Game.coin), False, const.Color.black), UI.Game.coin_text)

    var.screen.blit(var.Font.main.render("ArrowLeft:Left", False, const.Color.black), UI.Game.tutorial_1)
    var.screen.blit(var.Font.main.render("ArrowLeft:Right", False, const.Color.black), UI.Game.tutorial_2)
    var.screen.blit(var.Font.main.render("ArrowUp:Interact", False, const.Color.black), UI.Game.tutorial_3)
    var.screen.blit(var.Font.main.render("Space:Jump", False, const.Color.black), UI.Game.tutorial_4)

    for i in range(15):
        for j in range(20):
            if var.Game.data_playing['block'][i][j] != 0:
                var.screen.blit(asset.Img.block[var.Game.data_playing['block'][i][j]], [UI.Game.screen[0] + j * 40, UI.Game.screen[1] + i * 40])

    for i in range(len(var.Game.data_playing['thing'])):
        var.screen.blit(asset.Img.thing[var.Game.data_playing['thing'][i][0]], [UI.Game.screen[0] + var.Game.data_playing['thing'][i][1], UI.Game.screen[1] + var.Game.data_playing['thing'][i][2]])

    var.screen.blit(asset.Img.player, [UI.Game.screen[0] + var.Game.data_playing['player_position'][0] - 16, UI.Game.screen[1] + var.Game.data_playing['player_position'][1] - 16])

    pygame.draw.rect(var.screen, const.Color.black, UI.Game.screen, 2)

    var.screen.blit(var.Font.main.render('Current Speed : (' + str((var.Game.position_current_frame[0] - var.Game.position_previous_frame[0]) * 60) + ',' + str((var.Game.position_current_frame[1] - var.Game.position_previous_frame[1]) * 60) + ')' + ' Number of Objects : ' + str(len(var.Game.data_playing['thing'])), False, const.Color.black), UI.Game.status_1)
    var.screen.blit(var.Font.main.render('Position : (' + str(int(var.Game.data_playing['player_position'][0])) + ',' + str(int(var.Game.data_playing['player_position'][1])) + ')' + ' Touching Ground : ' + str(var.Game.data_playing['ground']), False, const.Color.black), UI.Game.status_2)

def convert_color_code_to_hex(color):
    color_code = '#'
    hex_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    for i in range(3):
        front = color[i] // 16
        back = color[i] % 16
        color_code += hex_num[front]
        color_code += hex_num[back]

    return color_code