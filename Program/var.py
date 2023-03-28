screen = None
game_output = None
clock = None
FPS = 60
error_msg = {'error' : '', 'time' : 0}

scene = 'edit'
state = ''

class Image_Editor():
    mode = 'draw'
    brush_size = 1
    brush_color = [0, 0, 0]
    eraser_size = 1
    layer_selected = 'background'
    layer = {'background' : None, 'object' : None}
    layer_visible = {'background' : False, 'object' : False}
    full_image = None

class Font():
    title = None
    main = None
