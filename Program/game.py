import var
import const
import physics

def player_move():
    temp_position = [var.Game.data_playing['player_position'][0], var.Game.data_playing['player_position'][1]]

    # Checking left right
    if var.Game.keyboard['left'] == True:
        temp_position[0] -= var.Game.data_playing['speed'] / var.FPS

    if var.Game.keyboard['right'] == True:
        temp_position[0] += var.Game.data_playing['speed'] / var.FPS

    temp_position[1] += var.Game.data_playing['y_speed'] / var.FPS

    # Checking ceiling floor
    var.Game.data_playing['ground'] = False

    if var.Game.data_playing['y_speed'] < 0:
        for i in range(15):
            for j in range(20):
                if var.Game.data_playing['wall'][i][j] != 0:
                    if physics.point_inside_rect(temp_position[0], temp_position[1], j * 40 + const.area_collide['up'][0], i * 40 + const.area_collide['up'][1], const.area_collide['up'][2], const.area_collide['up'][3]):
                        var.Game.data_playing['y_speed'] = 0
                        temp_position[1] = i * 40 + 56
                        break

    if var.Game.data_playing['y_speed'] >= 0:
        for i in range(15):
            for j in range(20):
                if var.Game.data_playing['wall'][i][j] != 0:
                    if physics.point_inside_rect(temp_position[0], temp_position[1], j * 40 + const.area_collide['down'][0], i * 40 + const.area_collide['down'][1], const.area_collide['down'][2], const.area_collide['down'][3]):
                        var.Game.data_playing['y_speed'] = 0
                        temp_position[1] = i * 40 - 16
                        var.Game.data_playing['jump_num'] = 1
                        var.Game.data_playing['ground'] = True
                        break

    if var.Game.data_playing['ground'] == False:
        if var.Game.data_playing['y_speed'] + var.Game.data_playing['gravity'] / var.FPS >= var.Game.data_playing['terminal_speed']:
            var.Game.data_playing['y_speed'] = var.Game.data_playing['terminal_speed']
        else:
            var.Game.data_playing['y_speed'] += var.Game.data_playing['gravity'] / var.FPS

    for i in range(15):
        for j in range(20):
            if var.Game.data_playing['wall'][i][j] != 0:
                if physics.point_inside_rect(temp_position[0], temp_position[1], j * 40 + const.area_collide['left'][0], i * 40 + const.area_collide['left'][1], const.area_collide['left'][2], const.area_collide['left'][3]):
                    temp_position[0] = j * 40 + 56
                    break

                elif physics.point_inside_rect(temp_position[0], temp_position[1], j * 40 + const.area_collide['right'][0], i * 40 + const.area_collide['right'][1], const.area_collide['right'][2], const.area_collide['right'][3]):
                    temp_position[0] = j * 40 - 16
                    break

    var.Game.data_playing['player_position'] = [temp_position[0], temp_position[1]]

def try_jump():
    if var.Game.data_playing['jump_num'] > 0:
        var.Game.data_playing['jump_num'] -= 1
        var.Game.data_playing['y_speed'] = var.Game.data_playing['jump_power']

def player_win_check():
    for i in range(len(var.Game.data_playing['thing'])):
        if var.Game.data_playing['thing'][i][0] == 2 and physics.point_inside_rect(var.Game.data_playing['player_position'][0],var.Game.data_playing['player_position'][1], var.Game.data_playing['thing'][i][1], var.Game.data_playing['thing'][i][2], 40, 40):
            return True

    return False

def player_defeat_check():
    if var.Game.data_playing['player_position'][1] > 600:
        return True
    
    return False