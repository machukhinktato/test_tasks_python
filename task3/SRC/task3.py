import csv
import re


def file_loader(data):
    with open(data, 'r', encoding='utf8') as f:
        file = f.readlines()

        return file


def save_data(data=None):
    with open('data.csv', 'w+', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(
            ['attempts to fill', 'err percent', 'fill success(ltr)',
             'fill fails(ltr)', 'attempts to withdrawal', 'err percent',
             'withdrawal success(ltr)', 'withdrawal fails(ltr)',
             'water volume in barrel at the start(ltr)',
             'water volume in barrel at the end(ltr)'])

    return 'done'


def log_scraper():
    data = file_loader('log.log')
    data = [i.split(',') for i in data]
    save_data(data)
    # barrel_data = dict()
    barrel_max_cap = re.findall('[0-9]+', data[0][0]).pop()
    barrel_cap_at_start = re.findall('[0-9]+', data[1][0]).pop()
    log = list()
    for i in range(len(data)):
        try:
            log.append(data[i + 2][0].split('.')[0])
        except:
            continue

    # barrel_data[w_vol] = re.match('[0-9]+', data[0][0])
    # for i in range(len(data)):
    #     data[i][0].replace('\n', '')
    #     print(data[i][0])
    # print([data[i] for i in range(len(data))][0])
    # return print(log)
    return print(data[3][0].split('.')[1].split('-')[1])


if __name__ == '__main__':
    log_scraper()
    # save_data()
