import os
import var
import const
import pygame

def load_image_drawn():
    pass

def save_image_drawn(image_name):
    var.Image_Editor.full_image.fill(const.Color.erase)
    
    if var.Image_Editor.layer_visible['white'] == True:
        var.Image_Editor.full_image.fill(const.Color.white)

    if var.Image_Editor.layer_visible['background'] == True:
        var.Image_Editor.full_image.blit(var.Image_Editor.layer['background'], [0, 0])

    if var.Image_Editor.layer_visible['object'] == True:
        var.Image_Editor.full_image.blit(var.Image_Editor.layer['object'], [0, 0])

    pygame.image.save(var.Image_Editor.full_image, './Drawing/' + var.Save.current_dir + image_name + 'Full.png')
    pygame.image.save(var.Image_Editor.layer['background'], './Drawing/' + var.Save.current_dir + image_name + 'Background.png')
    pygame.image.save(var.Image_Editor.layer['object'], './Drawing/'+ var.Save.current_dir + image_name + 'Object.png')

def save_image_window_init():
    var.Save.current_dir = ''
    var.Save.current_dir_files = os.listdir('./Drawing/' + var.Save.current_dir)
    var.Save.file_name_write = ''
    var.Save.file_name_mode = False
    var.Save.file_list_page = 0

def save_game_file_init():
    var.Save.current_dir = ''
    var.Save.current_dir_files = os.listdir('./GameFile/' + var.Save.current_dir)
    var.Save.file_name_write = ''
    var.Save.file_name_mode = False
    var.Save.file_list_page = 0

def layer_load_window_init():
    var.Load.current_dir = ''
    var.Load.current_dir_files = os.listdir('./Input/' + var.Save.current_dir)
    var.Load.file_list_page = 0
    var.Load.file_list_selected = -1

def go_upper_directory():
    directory_split = var.Save.current_dir.split('/')

    if len(directory_split) <= 0:
        var.Save.current_dir = ''

    else:
        directory_split = directory_split[:-1]
        var.Save.current_dir = '/'.join(map(str, directory_split))
