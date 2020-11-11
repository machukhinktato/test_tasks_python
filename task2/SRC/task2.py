def sphere_theme():
    task_dict = {
        'sphere': {'center': [0, 0, 10], 'radius': 10.67, },
        'line': [[1, 0.5, 15], [43, -14.6, 0.04]]
    }
    x,y,z = task_dict.get('sphere').get('center')
    # sphere_points = {
    #     'x': [(x - task_dict.get('sphere').get('radius')),
    #           (x + task_dict.get('sphere').get('radius'))],
    #     'y': [(y - task_dict.get('sphere').get('radius')),
    #           (y + task_dict.get('sphere').get('radius'))],
    #     'z': [(z - task_dict.get('sphere').get('radius')),
    #           (z + task_dict.get('sphere').get('radius'))],
    # }
    ok = []
    for i in range(3):

        ok.append((((task_dict.get('sphere').get('center')[i]) - (task_dict.get('sphere').get('radius'))),
                   (((task_dict.get('sphere').get('center')[i])) + (task_dict.get('sphere').get('radius'))))
)        # sphere_y = list(((y - task_dict.get('sphere').get('radius'),
        #            (y + task_dict.get('sphere').get('radius')))))
        # sphere_z = list(((z - task_dict.get('sphere').get('radius'),
        #            (z + task_dict.get('sphere').get('radius')))))
    # x, y, z = [[i for i in range(-10, 10)] for i in range(3)]

    line_x = list(((task_dict.get('line')[0][0]),
                   (task_dict.get('line')[1][0])))
    line_y = list(((task_dict.get('line')[0][1]),
                   (task_dict.get('line')[1][1])))
    line_z = list(((task_dict.get('line')[0][2]),
                   (task_dict.get('line')[1][2])))


    def comparison(param_1, param_2):
        if param_1[0] < param_2[0]:
            print('banana')
        elif param_1[0] >= param_2[0] and param_1[0] >= param_2[1]:
            print('zhopa')
        elif param_1[0] >= param_2[0] and param_1[0] < param_2[1]:
            print(f'blyad {param_1[0]} > {param_2[0]} < {param_2[1]}')


    # if line_x[0] < sphere_x[0]:
    #     print('banana')
    # elif line_x[0] >= sphere_x[0] and line_x[0] >= sphere_x[1]:
    #     print('zhopa')
    # elif line_x[0] >= sphere_x[0] and line_x[0] < sphere_x[1]:
    #     print('blyad')
    # return print(task_dict.get('line')[1][1])
    # return print(sphere_x, sphere_y, sphere_z)
    # return print(line_x, line_y, line_z)
    # return print(comparison(line_x[0], sphere_x[0]))
    return print(comparison(line_x, ok[0]))
if __name__ == '__main__':
    sphere_theme()
