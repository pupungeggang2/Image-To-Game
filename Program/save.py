import var
import const
import pygame

def load_image_drawn():
    pass

def save_image_drawn(image_name):
    var.Image_Editor.full_image.fill(const.Color.erase)
    var.Image_Editor.full_image.bilt(var.Image_Editor.layer['background'])
    var.Image_Editor.full_image.bilt(var.Image_Editor.layer['object'])

    pygame.image.save(var.Image_Editor.full_image, './Drawing/' + image_name + '_full.png')
    pygame.image.save(var.Image_Editor.layer['background'], './Drawing/' + image_name + '_background.png')
    pygame.image.save(var.Image_Editor.layer['object'], './Drawing/' + image_name + '_object.png')