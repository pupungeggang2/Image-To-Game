import var
import physics

def player_move():
    if var.Game.keyboard['left'] == True:
        var.Game.data_playing['player_position'][0] -= var.Game.data_playing['speed'] / var.FPS

    if var.Game.keyboard['right'] == True:
        var.Game.data_playing['player_position'][0] += var.Game.data_playing['speed'] / var.FPS

def player_win_check():
    for i in range(len(var.Game.data_playing['thing'])):
        if var.Game.data_playing['thing'][i][0] == 2 and physics.point_inside_rect(var.Game.data_playing['player_position'][0],var.Game.data_playing['player_position'][1], var.Game.data_playing['thing'][i][1], var.Game.data_playing['thing'][i][2], 40, 40):
            return True

    return False

def player_defeat_check():
    if var.Game.data_playing['player_position'][1] > 600:
        return True
    
    return False