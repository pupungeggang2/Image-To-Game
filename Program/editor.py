import var
import const

import UI
import pygame
import json

def draw_point(x, y):
    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

    point_start_ul = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.
    brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ur = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ll = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]
    point_start_lr = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]

    pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, [point_start_ll, point_start_lr, point_start_ur, point_start_ul])

def draw_line(x, y):
    var.Image_Editor.brush_line_current = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

    point_cur_ul = [var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_size / 2]
    point_cur_ur = [var.Image_Editor.brush_line_current[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_size / 2]
    point_cur_ll = [var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] + var.Image_Editor.brush_size / 2]
    point_cur_lr = [var.Image_Editor.brush_line_current[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] + var.Image_Editor.brush_size / 2]

    point_start_ul = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ur = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ll = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]
    point_start_lr = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] > 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] > 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, [point_start_ll, point_start_ul, point_start_ur, point_cur_ur, point_cur_lr, point_cur_ll])

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] > 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] <= 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, [point_start_ul, point_start_ll, point_start_lr, point_cur_lr, point_cur_ur, point_cur_ul])

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] <= 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] > 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, [point_start_ul, point_start_ur, point_start_lr, point_cur_lr, point_cur_ll, point_cur_ul])

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] <= 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] <= 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], var.Image_Editor.brush_color, [point_start_ur, point_start_lr, point_start_ll, point_cur_ll, point_cur_ul, point_cur_ur])

    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

def erase_point(x, y):
    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

    point_start_ul = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.
    brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ur = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ll = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]
    point_start_lr = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]

    pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, [point_start_ll, point_start_lr, point_start_ur, point_start_ul])

def erase_line(x, y):
    var.Image_Editor.brush_line_current = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

    point_cur_ul = [var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_size / 2]
    point_cur_ur = [var.Image_Editor.brush_line_current[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_size / 2]
    point_cur_ll = [var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] + var.Image_Editor.brush_size / 2]
    point_cur_lr = [var.Image_Editor.brush_line_current[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_current[1] + var.Image_Editor.brush_size / 2]

    point_start_ul = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ur = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] - var.Image_Editor.brush_size / 2]
    point_start_ll = [var.Image_Editor.brush_line_start[0] - var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]
    point_start_lr = [var.Image_Editor.brush_line_start[0] + var.Image_Editor.brush_size / 2, var.Image_Editor.brush_line_start[1] + var.Image_Editor.brush_size / 2]

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] > 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] > 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, [point_start_ll, point_start_ul, point_start_ur, point_cur_ur, point_cur_lr, point_cur_ll])

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] > 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] <= 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, [point_start_ul, point_start_ll, point_start_lr, point_cur_lr, point_cur_ur, point_cur_ul])

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] <= 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] > 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, [point_start_ul, point_start_ur, point_start_lr, point_cur_lr, point_cur_ll, point_cur_ul])

    if var.Image_Editor.brush_line_current[0] - var.Image_Editor.brush_line_start[0] <= 0 and var.Image_Editor.brush_line_current[1] - var.Image_Editor.brush_line_start[1] <= 0:
        pygame.draw.polygon(var.Image_Editor.layer[var.Image_Editor.layer_selected], const.Color.erase, [point_start_ur, point_start_lr, point_start_ll, point_cur_ll, point_cur_ul, point_cur_ur])

    var.Image_Editor.brush_line_start = [x - UI.Game_Screen_Edit.rect[0], y - UI.Game_Screen_Edit.rect[1]]

def load_game_file():
    var.Game.data_playing = json.loads(json.dumps(var.Game.data_level))
    var.Game.data_playing['player_position'] = [var.Game.data_level['start_position'][0], var.Game.data_level['start_position'][1]]
    var.Game.data_playing['speed'] = 160
    var.Game.data_playing['y_speed'] = 0
    var.Game.data_playing['terminal_speed'] = 800
    var.Game.data_playing['gravity'] = 1600
    var.Game.data_playing['jump_power'] = -500
    var.Game.data_playing['jump_num'] = 0
    var.Game.data_playing['ground'] = False
    var.Game.coin = 0