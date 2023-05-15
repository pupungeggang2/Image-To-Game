class Upper_Bar():
    rect = [0, 0, 1280, 40]
    new = [0, 0, 40, 40]
    save = [40, 0, 40, 40]
    image_save = [80, 0, 40, 40]
    brush = [120, 0, 40, 40]
    erase = [160, 0, 40, 40]
    move = [200, 0, 40, 40]
    palette = [240, 0, 40, 40]
    game = [280, 0, 40, 40]
    convert = [600, 0, 40, 40]
    play = [640, 0, 40, 40]

class Message_Bar():
    rect = [0, 40, 1280, 40]
    text_msg = [4, 44]

class Left_Bar():
    rect = [0, 80, 480, 600]
    brush_point_rect = [0, 80, 40, 40]
    brush_point = [20, 100]
    brush_size_slider = [80, 100, 380, 100]
    brush_size_text = [420, 90]
    brush_size_click_rect = [80, 80, 300, 80]

    brush_color_rect = [0, 140, 40, 40]
    brush_color_code_text = [80, 144]

    brush_color_red_click_rect = [80, 200, 300, 40]
    brush_color_red_text = [8, 208]
    brush_color_red_slider = [80, 220, 380, 220]
    brush_color_red_val_text = [420, 210]
    brush_color_green_click_rect = [80, 240, 300, 40]
    brush_color_green_text = [8, 248]
    brush_color_green_slider = [80, 260, 380, 260]
    brush_color_green_val_text = [420, 250]
    brush_color_blue_click_rect = [80, 280, 300, 40]
    brush_color_blue_text = [8, 288]
    brush_color_blue_slider = [80, 300, 380, 300]
    brush_color_blue_val_text = [420, 290]

    color_picker = [0, 340]
    color_picker_rect_size = [60, 60]

    layer_object_rect = [0, 560, 480, 40]
    layer_object_select = [0, 560, 360, 40]
    layer_object_text = [8, 568]
    layer_object_erase = [400, 560, 40, 40]
    layer_object_load = [440, 560, 40, 40]
    layer_object_visible = [360, 560, 40, 40]
    layer_background_rect = [0, 600, 480, 40]
    layer_background_select = [0, 600, 360, 40]
    layer_background_text = [8, 608]
    layer_background_erase = [400, 600, 40, 40]
    layer_background_load = [440, 600, 40, 40]
    layer_background_visible = [360, 600, 40, 40]
    layer_white_rect = [0, 640, 480, 40]
    layer_white_text = [8, 648]
    layer_white_visible = [440, 640, 40, 40]
    layer_player_rect = [0, 520, 480, 40]
    layer_player_text = [8, 528]
    layer_player_visible = [440, 520, 40, 40]

class Game_Screen_Edit():
    rect = [480, 80, 800, 600]

class Lower_Bar():
    rect = [0, 680, 1280, 40]
    text_status = [4, 684]

class Save_Window():
    rect = [160, 80, 960, 560]
    close_button = [1080, 80, 40, 40]
    title_bar = [160, 80, 960, 40]
    title_text = [168, 84]
    directory_bar = [160, 120, 960, 40]
    directory_text = [168, 128]
    file_list = [
        [160, 160, 480, 40], [160, 200, 480, 40], [160, 240, 480, 40], [160, 280, 480, 40],
        [160, 320, 480, 40], [160, 360, 480, 40], [160, 400, 480, 40], [160, 440, 480, 40],
        [160, 480, 480, 40], [160, 520, 480, 40],
        [640, 160, 480, 40], [640, 200, 480, 40], [640, 240, 480, 40], [640, 280, 480, 40],
        [640, 320, 480, 40], [640, 360, 480, 40], [640, 400, 480, 40], [640, 440, 480, 40],
        [640, 480, 480, 40], [640, 520, 480, 40],
    ]
    file_list_prev_button = [160, 560, 40, 40]
    file_list_next_button = [1080, 560, 40, 40]
    file_list_page_text = [564, 560]
    lower_bar = [160, 600, 960, 40]
    lower_text_rect = [160, 600, 840, 40]
    file_name = [168, 608]
    save_button = [1000, 600, 120, 40]
    save_text = [1008, 604]

class Load_Window():
    rect = [160, 80, 960, 560]
    close_button = [1080, 80, 40, 40]
    title_bar = [160, 80, 40, 40]
    title_text = [168, 84]
    directory_bar = [160, 120, 960, 40]
    directory_text = [168, 128]
    file_list = [
        [160, 160, 480, 40], [160, 200, 480, 40], [160, 240, 480, 40], [160, 280, 480, 40],
        [160, 320, 480, 40], [160, 360, 480, 40], [160, 400, 480, 40], [160, 440, 480, 40],
        [160, 480, 480, 40], [160, 520, 480, 40],
        [640, 160, 480, 40], [640, 200, 480, 40], [640, 240, 480, 40], [640, 280, 480, 40],
        [640, 320, 480, 40], [640, 360, 480, 40], [640, 400, 480, 40], [640, 440, 480, 40],
        [640, 480, 480, 40], [640, 520, 480, 40],
    ]
    file_list_prev_button = [160, 560, 40, 40]
    file_list_next_button = [1080, 560, 40, 40]
    file_list_page_text = [564, 560]
    lower_bar = [160, 600, 960, 40]
    lower_text_rect = [160, 600, 840, 40]
    load_button = [1000, 600, 120, 40]
    load_text = [1008, 604]

class Game():
    status_text = [8, 4]
    coin_icon = [0, 40]
    coin_text = [48, 44]
    play_button = [580, 0, 40, 40]
    pause_button = [620, 0, 40, 40]
    stop_button = [660, 0, 40, 40]
    screen = [240, 40, 800, 600]