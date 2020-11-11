def sphere_theme():
    task_dict = {
        'sphere': {'center': [0, 0, 10], 'radius': 10.67, },
        'line': [[1, 0.5, 15], [43, -14.6, 0.04]]
    }

    sphere_coords, line_coords = [], []
    for i in range(3):
        sphere_coords.append((
            ((task_dict.get('sphere').get('center')[i]) -
             (task_dict.get('sphere').get('radius'))),
            (((task_dict.get('sphere').get('center')[i])) +
             (task_dict.get('sphere').get('radius'))))
        )
        line_coords.append((
            ((task_dict.get('line')[0][i])),
            ((task_dict.get('line')[1][i]))
        ))

    line_x = list(((task_dict.get('line')[0][0]),
                   (task_dict.get('line')[1][0])))
    line_y = list(((task_dict.get('line')[0][1]),
                   (task_dict.get('line')[1][1])))
    line_z = list(((task_dict.get('line')[0][2]),
                   (task_dict.get('line')[1][2])))

    return print(comparison(line_coords[0], sphere_coords[0]))
    # return print(line_coords)


def comparison(line, sphere):
    if line[0] < sphere[0]:
        print('banana')
    elif line[0] >= sphere[0] and line[0] <= sphere[1]:
        print(f'blyad {line[0]} > {sphere[0]} < {sphere[1]}')
        if line[1] > sphere[1]:
            print(f'{sphere[1]}')
            print(f'{line[1] > sphere[1]}')
            print(f'{line[1] < sphere[1]}')
    elif line[0] >= sphere[0] and line[0] > sphere[1]:
        print('zhopa')


if __name__ == '__main__':
    sphere_theme()
