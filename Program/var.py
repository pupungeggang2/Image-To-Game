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
    layer_visible = {'background' : True, 'object' : True}
    full_image = None

class Font():
    title = None
    main = None
