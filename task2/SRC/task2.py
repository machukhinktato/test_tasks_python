def sphere_theme():
    task_dict = {
        'sphere': {'center': [0, 0, 10], 'radius': 10.67, },
        'line': [[1, 0.5, 15], [43, -14.6, 0.04]]
    }
    x,y,z = task_dict.get('sphere').get('center')
    sphere_points = {
        'x': [(x - task_dict.get('sphere').get('radius')),
              (x + task_dict.get('sphere').get('radius'))],
        'y': [(y - task_dict.get('sphere').get('radius')),
              (y + task_dict.get('sphere').get('radius'))],
        'z': [(z - task_dict.get('sphere').get('radius')),
              (z + task_dict.get('sphere').get('radius'))],
    }
    sphere_x = list(((x - task_dict.get('sphere').get('radius'),
               (x + task_dict.get('sphere').get('radius')))))
    sphere_y = list(((y - task_dict.get('sphere').get('radius'),
               (y + task_dict.get('sphere').get('radius')))))
    sphere_z = list(((z - task_dict.get('sphere').get('radius'),
               (z + task_dict.get('sphere').get('radius')))))
    # x, y, z = [[i for i in range(-10, 10)] for i in range(3)]

    line_x = list(((task_dict.get('line')[0][0]),
                   (task_dict.get('line')[1][0])))
    line_y = list(((task_dict.get('line')[0][1]),
                   (task_dict.get('line')[1][1])))
    line_z = list(((task_dict.get('line')[0][2]),
                   (task_dict.get('line')[1][2])))


    def comparison():
        pass


    if line_x[0] < sphere_x[0]:
        print('banana')
    elif line_x[0] >= sphere_x[0] and line_x[0] >= sphere_x[1]:
        print('zhopa')
    elif line_x[0] >= sphere_x[0] and line_x[0] < sphere_x[1]:
        print('blyad')
    # return print(task_dict.get('line')[1][1])
    # return print(sphere_x, sphere_y, sphere_z)
    # return print(line_x, line_y, line_z)
    return print(line_x, sphere_x)
if __name__ == '__main__':
    sphere_theme()
