screen = None
clock = None
FPS = 60
msg = {'msg' : '', 'time' : 0}
game_output = {}

scene = 'edit'
state = ''

class Image_Editor():
    brush_mode = 'draw'
    brush_size = 10
    brush_color = [0, 0, 0, 255]
    brush_pressed = False
    brush_line_start = [0, 0]
    brush_line_current = [0, 0]
    canvas_mode = 'draw'
    eraser_size = 10
    layer_selected = 'object'
    layer = {'background' : None, 'object' : None}
    layer_visible = {'background' : True, 'object' : True, 'white' : True, 'player' : True}
    full_image = None
    start_position = [40, 40]

class Game():
    data_level = {}
    keyboard = {'up' : False, 'down' : False, 'left' : False, 'right' : False}
    data_playing = {}
    coin = 0
    position_previous_frame = []
    position_current_frame = []

class Load():
    layer = ''
    current_dir = ''
    current_dir_files = []
    file_list_page = 0
    file_list_selected = 0

class Save():
    current_dir = ''
    current_dir_files = []
    file_name_write = ''
    file_name_mode = False
    file_list_page = 0

class Font():
    title = None
    main = None
