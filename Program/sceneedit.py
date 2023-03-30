import pygame

import var
import const

import UI
import draw
import physics
import save
import editor

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    draw.draw_upper_bar()
    draw.draw_message_bar()
    draw.draw_left_bar()
    draw.draw_game_screen_edit()
    draw.draw_lower_bar()

    if var.state == 'image_save':
        draw.draw_save_image_window()

    elif var.state == 'layer_load':
        draw.draw_load_window()

    pygame.display.flip()

def mouse_down(x, y, button):
    if button == 1:
        if var.state == '':
            if var.Image_Editor.canvas_mode == 'draw':
                if var.Image_Editor.brush_mode == 'draw':
                    if physics.point_inside_rect_array(x, y, UI.Game_Screen_Edit.rect):
                        var.Image_Editor.brush_pressed = True
                        editor.draw_point(x, y)

                elif var.Image_Editor.brush_mode == 'erase':
                    if physics.point_inside_rect_array(x, y, UI.Game_Screen_Edit.rect):
                        var.Image_Editor.brush_pressed = True
                        editor.erase_point(x, y)

def mouse_up(x, y, button):
    if button == 1:
        var.Image_Editor.brush_pressed = False

        if var.state == '':
            # Top bar
            if physics.point_inside_rect_array(x, y, UI.Upper_Bar.new):
                var.Image_Editor.layer['background'].fill(const.Color.erase)
                var.Image_Editor.layer['object'].fill(const.Color.erase)
                var.Image_Editor.brush_mode = 'draw'

            if physics.point_inside_rect_array(x, y, UI.Upper_Bar.image_save):
                var.state = 'image_save'
                save.save_window_init()
                print(var.state)

            if physics.point_inside_rect_array(x, y, UI.Upper_Bar.brush):
                var.Image_Editor.brush_mode = 'draw'

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.erase):
                var.Image_Editor.brush_mode = 'erase'

            # Left bar
            if physics.point_inside_rect_array(x, y, UI.Left_Bar.layer_background_select):
                var.Image_Editor.layer_selected = 'background'

            elif physics.point_inside_rect_array(x, y, UI.Left_Bar.layer_object_select):
                var.Image_Editor.layer_selected = 'object'

        elif var.state == 'image_save':
            if physics.point_inside_rect_array(x, y, UI.Save_Window.close_button):
                var.state = ''

            if physics.point_inside_rect_array(x, y, UI.Save_Window.lower_text_rect):
                if var.Save.file_name_mode == True:
                    var.Save.file_name_mode = False
                else:
                    var.Save.file_name_mode = True

            if physics.point_inside_rect_array(x, y, UI.Save_Window.save_button):
                if len(var.Save.file_name_write) > 0:
                    save.save_image_drawn(var.Save.file_name_write)
                    var.state = ''

        elif var.state == 'layer_load':
            pass

def mouse_motion(x, y):
    if var.state == '':
        if var.Image_Editor.canvas_mode == 'draw':
            if var.Image_Editor.brush_mode == 'draw':
                if physics.point_inside_rect_array(x, y, UI.Game_Screen_Edit.rect):
                    if var.Image_Editor.brush_pressed == True:
                        editor.draw_line(x, y)

            elif var.Image_Editor.brush_mode == 'erase':
                if physics.point_inside_rect_array(x, y, UI.Game_Screen_Edit.rect):
                    if var.Image_Editor.brush_pressed == True:
                        editor.erase_line(x, y)

def key_down(key):
    if var.state == 'image_save':
        if var.Save.file_name_mode == True:
            if (key >= 48 and key <= 57) or (key >= 97 and key <= 122):
                var.Save.file_name_write += chr(key)

            elif key == pygame.K_BACKSPACE:
                if len(var.Save.file_name_write) > 0:
                    var.Save.file_name_write = var.Save.file_name_write[:-1]

def key_up(key):
    pass