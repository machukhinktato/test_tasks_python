def sphere_theme():
    task_dict = {
        'sphere': {
        'center': [0,0,0],
        'radius': 10.67,
        },
        'line': [[1, 0.5, 15], [43, -14.6, 0.04]]
    }

    return print(task_dict.get('line')[1][1])


if __name__ == '__main__':
    sphere_theme()