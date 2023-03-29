class Upper_Bar():
    rect = [0, 0, 1280, 40]
    new = [0, 0, 40, 40]
    save = [40, 0, 40, 40]
    image_save = [80, 0, 40, 40]
    brush = [200, 0, 40, 40]
    erase = [240, 0, 40, 40]
    convert = [280, 0, 40, 40]
    play = [320, 0, 40, 40]

class Message_Bar():
    rect = [0, 40, 1280, 40]
    text_msg = [4, 4]

class Left_Bar():
    rect = [0, 80, 480, 600]
    brush_point_rect = [0, 80, 40, 40]
    brush_point = [20, 100]
    brush_size_slider = [60, 100, 400, 100]
    brush_size_text = [440, 90]

    layer_object_rect = [0, 600, 480, 40]
    layer_object_select = [0, 600, 360, 40]
    layer_object_text = [8, 610]
    layer_object_erase = [400, 600, 40, 40]
    layer_object_load = [440, 600, 40, 40]
    layer_background_rect = [0, 640, 480, 40]
    layer_background_select = [0, 640, 360, 40]
    layer_background_text = [8, 650]
    layer_background_erase = [400, 640, 40, 40]
    layer_background_load = [440, 640, 440, 40]

class Game_Screen_Edit():
    rect = [480, 80, 800, 600]

class Lower_Bar():
    rect = [0, 680, 1280, 40]
    text_status = [4, 684]