import csv
import re

log = 'log.log'
start = '2020-01-01Т12:51:33'
end = '2020-01-01Т12:51:34'


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


def log_scraper(log, start, end):
    data = file_loader(log)
    data = [i.split(',') for i in data]
    save_data(data)
    # barrel_data = dict()
    barrel_max_cap = re.findall('[0-9]+', data[0][0]).pop()
    barrel_cap_at_start = re.findall('[0-9]+', data[1][0]).pop()
    # print(data)
    log_data, success, fail = [], [], []
    for i in range(len(data)):
        try:
            if start > data[i + 2][0].split('.')[0]:
                log_data.append(data[i + 2])
        except:
            continue
    for elem in log_data:
        for i in range(len(log_data)):
            if elem[-i].split('.')[0] > end:
                log_data.pop([-i])

            # log_data.append(data[i + 2][0].split('.')[0])
    #                             if 'успех' in data[i + 2][0].split('.')[1].split('-')[1]:
    #                                 success.append(
    #                                     data[i + 2][0].split('.')[1].split('-')[1].
    #                                         replace('\n', ''))
    #                             else:
    #                                 fail.append(
    #                                     data[i + 2][0].split('.')[1].split('-')[1].
    #                                         replace('\n', ''))


    # err_percentage = len(fail) * 100 / (len(success) + len(fail))
    # for i in range(len(log_data)):
    #     if start < log_data[i]:
    #         # log_data[i].pop()
    #         log_data.pop(i)


# barrel_data[w_vol] = re.match('[0-9]+', data[0][0])
# for i in range(len(data)):
#     data[i][0].replace('\n', '')
#     print(data[i][0])
# print([data[i] for i in range(len(data))][0])
# return print(start, log_data, end)
    return print(log_data)
# return print(data[3][0].split('.')[1].split('-')[1])


if __name__ == '__main__':
    log_scraper(log, start, end)
    # save_data()
