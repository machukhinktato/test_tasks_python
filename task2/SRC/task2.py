def sphere_theme():
    task_dict = {
        'sphere': {'center': [0, 0, 0], 'radius': 10.67, },
        'line': [[1, 0.5, 15], [43, -14.6, 0.04]]
        # 'line': [[15, 0.5, 15], [43, -14.6, 0.04]]
    }
    sphere_coords, line_coords = [], []
    for i in range(3):
        sphere_coords.append((
            ((task_dict.get('sphere').get('center')[i]) -
             (task_dict.get('sphere').get('radius'))),
            (((task_dict.get('sphere').get('center')[i])) +
             (task_dict.get('sphere').get('radius'))))
        )
    for i in range(3):
        line_coords.append((
            [task_dict.get('line')[0][i], task_dict.get('line')[1][i]]
        ))
        if line_coords[i][0] > line_coords[i][1]:
            line_coords[i][0], line_coords[i][1] = line_coords[i][1], line_coords[i][0]

    # print(line_coords)
    line = {'sections': {
        'x': line_coords[0],
        'y': line_coords[1],
        'z': line_coords[2],
    }}
    # print(line.get('sections').values())
    # print(line.get('sections').get('x'))
    # print(line)



    # line_x = list(((task_dict.get('line')[0][0]),
    #                (task_dict.get('line')[1][0])))
    # line_y = list(((task_dict.get('line')[0][1]),
    #                (task_dict.get('line')[1][1])))
    # line_z = list(((task_dict.get('line')[0][2]),
    #                (task_dict.get('line')[1][2])))

    # return print(comparison(line_coords[0], sphere_coords[0]))
    # return print(line_coords[0][0] if line_coords[0][0] > line_coords[0][1] else line_coords[0].insert(0, line_coords[0][1]))
    # print(line_coords, sphere_coords)
    return print(comparison(line, sphere_coords))

# def comparison(line, sphere):
#     inside, outside = [], []
#     for i in range(len(sphere)):
#         if line[i][0] >= sphere[i][0] and line[i][0] <= sphere[i][1] or \
#                 line[i][1] >= sphere[i][0] and line[i][1] <= sphere[i][1]:
#             inside.append(line[i])
#         else:
#             outside.append(line[i])

def comparison(line, sphere):
    x = 0
    # for k in range(3):
    for i in line.get('sections').keys():

        print(x)
    # print(f'{i} {line.get("sections").get(i)}')
        if line.get('sections').get(i)[0] >= sphere[x][0] and\
                line.get('sections').get(i)[0] <= sphere[x][1]:
            line.get('sections').get(i).append(True)
        else:
            line.get('sections').get(i).append(None)
        if line.get('sections').get(i)[1] >= sphere[x][0] and\
                line.get('sections').get(i)[1] <= sphere[x][1]:

            line.get('sections').get(i).append(True)
        else:
            line.get('sections').get(i).append(None)
        x += 1

            # inside.append(line[i])
        # else:
        #     outside.append(line[i])
    # section = line.get('sections')
    # for key in line.get('sections'):
    # section.get
    #     print(key)
    return cross_finder(line, sphere)
    # return print([line.get('sections').get('x')[3] if line.get('sections').get('x')[3] == True else line.get('sections').get('x')[2]])

        # if line[i][1] >= sphere[i][0] and line[i][1] <= sphere[i][1]:
        #     inside.append(line[i][1])
        # else:
        #     outside.append(line[i][1])


        # elif:
        # elif line[i][0] > sphere[i][1]:
        #     print('damn')
        # elif line[0] >= sphere[0] and line[0] <= sphere[1]:
        #     print(f'blyad {line[0]} > {sphere[0]} < {sphere[1]}')
        #     if line[1] > sphere[1]:
        #         print(f'{sphere[1]}')
        #         print(f'{line[1] > sphere[1]}')
        #         print(f'{line[1] < sphere[1]}')
        # elif line[0] >= sphere[0] and line[0] > sphere[1]:
        #     print('zhopa')
        # else:
        #     print('bam')


    # print(inside, outside)
    # return cross_finder(inside, sphere)


def cross_finder(sections, sphere):
    sections = sections.get('sections')
    crosspoints = dict()
    for key in sections.keys():
        if sections[key][2] == True:
            crosspoints[key] = sphere[0][0]
        if sections[key][3] == True:
            crosspoints[key] = sphere[0][1]
        # sections[key][2] = 'banana'
    return crosspoints


if __name__ == '__main__':
    sphere_theme()
