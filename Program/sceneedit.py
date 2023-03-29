import pygame

import var
import const

import UI
import draw
import physics

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
    if button == 1:
        if var.state == '':
            if var.Image_Editor.canvas_mode == 'draw':
                if var.Image_Editor.brush_mode == 'draw':
                    if physics.point_inside_rect_array(x, y, UI.Game_Screen_Edit.rect):
                        var.Image_Editor.brush_pressed = True
                        var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

def mouse_up(x, y, button):
    if button == 1:
        var.Image_Editor.brush_pressed = False

        if var.state == '':
            # Top bar
            if physics.point_inside_rect_array(x, y, UI.Upper_Bar.brush):
                var.Image_Editor.brush_mode = 'draw'

            elif physics.point_inside_rect_array(x, y, UI.Upper_Bar.erase):
                var.Image_Editor.brush_mode = 'erase'

            # Left bar
            if physics.point_inside_rect_array(x, y, UI.Left_Bar.layer_background_select):
                var.Image_Editor.layer_selected = 'background'

            elif physics.point_inside_rect_array(x, y, UI.Left_Bar.layer_object_select):
                var.Image_Editor.layer_selected = 'object'

        elif var.state == 'save':
            pass

        elif var.state == 'load':
            pass

def mouse_motion(x, y):
    if var.state == '':
        if var.Image_Editor.canvas_mode == 'draw':
            if var.Image_Editor.brush_mode == 'draw':
                if physics.point_inside_rect_array(x, y, UI.Game_Screen_Edit.rect):
                    if var.Image_Editor.brush_pressed == True:
                        var.Image_Editor.brush_line_current = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]
                        pygame.draw.line(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, var.Image_Editor.brush_line_start, var.Image_Editor.brush_line_current, var.Image_Editor.brush_size)
                        pygame.draw.circle(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, var.Image_Editor.brush_line_current, var.Image_Editor.brush_size / 3)
                        var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

def key_down(key):
    pass

def key_up(key):
    pass