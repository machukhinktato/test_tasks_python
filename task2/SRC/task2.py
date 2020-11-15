import json

def file_loader(name):
    """Загружает json файл с данынми"""
    with open(name) as f:
        try:
            file = json.load(f)
        except:
            file = f.readlines()
        f.close()
    return file


def main(filename):
    """
    Основная функция, принимает исходные значения, сортирует данные
    и отдаёт их на обработку профильным функциям
    """
    # task_dict = file_loader(input('Enter the file name, to start program: '))
    task_dict = file_loader(filename)
    sphere_coords, line_coords = [], []
    for i in range(3):
        sphere_coords.append((
            ((task_dict.get('sphere').get('center')[i]) -
             (task_dict.get('sphere').get('radius'))),
            (((task_dict.get('sphere').get('center')[i])) +
             (task_dict.get('sphere').get('radius'))))
        )
        line_coords.append((
            [task_dict.get('line')[0][i], task_dict.get('line')[1][i]]
        ))

    line = {'sections': {
        'x': line_coords[0],
        'y': line_coords[1],
        'z': line_coords[2],
    }}
    result = comparison(line, sphere_coords)
    try:
        for key in result.keys():
            # ok.append(f"{key} = {result.get(key)}")
            print(f"{key} : {result.get(key)}")
        return ''
    except:
        return print('Коллизий не найдено')


def comparison(line, sphere):
    """Функция находящая точки внутри сферы"""
    x = 0
    section = line.get('sections')
    for key in section.keys():
        for i in range(2):
            if section[key][i] >= sphere[0][0] and section[key][i] <= sphere[x][1]:
                section.get(key).append(True)
            else:
                section.get(key).append(None)
        x += 1

    return cross_finder(line, sphere)


def cross_finder(sections, sphere):
    """
    Функция производящая финальную оценку по точкам
    линии проходящим через или входящим в сферу
    """
    x = 0
    sections = sections.get('sections')
    crosspoints = dict()
    for key in sections.keys():
        if sections[key][2] and sections[key][3] == True or \
                float(sections[key][0]) < min(sphere[x]) and \
                float(sections[key][1]) < min(sphere[x]) or \
                float(sections[key][0]) > max(sphere[x]) and \
                float(sections[key][1]) > max(sphere[x]):
            continue
        elif sections[key][2] == True:
            if sections[key][0] > sections[key][1]:
                # Номера присватваются в зависимот от элемента вхождения
                crosspoints[key + '_1'] = sphere[x][0]
            else:
                crosspoints[key + '_1'] = sphere[x][1]
        elif sections[key][3] == True:
            if sections[key][1] > sections[key][0]:
                crosspoints[key + '_2'] = sphere[x][0]
            else:
                crosspoints[key + '_2'] = sphere[x][1]

    cords = ['x_1', 'y_1', 'z_1', 'x_2', 'y_2', 'z_2']
    for point in cords:
        if point in crosspoints:
            return crosspoints


if __name__ == '__main__':
    main('test.txt')