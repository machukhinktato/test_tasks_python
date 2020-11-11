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
    # x, y, z = [[i for i in range(-10, 10)] for i in range(3)]

    # return print(task_dict.get('line')[1][1])
    return print(sphere_points.values())

if __name__ == '__main__':
    sphere_theme()
