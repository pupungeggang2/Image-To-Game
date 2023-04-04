screen = None
game_output = None
clock = None
FPS = 60
msg = {'msg' : '', 'time' : 0}

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
    layer_selected = 'background'
    layer = {'background' : None, 'object' : None}
    layer_visible = {'background' : True, 'object' : True, 'white' : True, 'player' : False}
    full_image = None

class Game():
    data_map = {}

class Load():
    layer = ''
    current_dir = ''
    current_dir_files = []

class Save():
    current_dir = ''
    current_dir_files = []
    file_name_write = ''
    file_name_mode = False

class Font():
    title = None
    main = None
