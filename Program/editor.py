import var
import const

import UI
import pygame

def draw_point(x, y):
    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]
    pygame.draw.circle(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, var.Image_Editor.brush_line_start, var.Image_Editor.brush_size / 2)

def draw_line(x, y):
    var.Image_Editor.brush_line_current = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]
    pygame.draw.line(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, var.Image_Editor.brush_line_start, var.Image_Editor.brush_line_current, var.Image_Editor.brush_size)
    pygame.draw.circle(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, var.Image_Editor.brush_line_start, var.Image_Editor.brush_size / 2)
    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

def erase_point(x, y):
    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]
    pygame.draw.circle(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, var.Image_Editor.brush_line_start, var.Image_Editor.brush_size / 2)

def erase_line(x, y):
    var.Image_Editor.brush_line_current = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]
    pygame.draw.line(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, var.Image_Editor.brush_line_start, var.Image_Editor.brush_line_current, var.Image_Editor.brush_size)
    pygame.draw.circle(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, var.Image_Editor.brush_line_start, var.Image_Editor.brush_size / 2)
    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]