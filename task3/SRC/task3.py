import csv
import re

log = 'log.log'
start = '2020-01-01Т12:51:31'
end = '2020-01-01Т12:51:35'


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
             'water capacity in barrel at the start(ltr)',
             'water capacity in barrel at the end(ltr)'])

    return 'done'


def log_scraper(log, start, end):
    fill_attempts = 0
    fill_err_percent = 0.0
    fill_fails = 0
    withdrawal_att = 0
    withdrawal_err_pct = 0.0
    withdrawal_fails = 0
    data = file_loader(log)
    data = [i.split(',') for i in data]
    print(data)
    save_data(data)
    barrel_max_cap = re.findall('[0-9]+', data[0][0]).pop()
    barrel_cap_at_start = re.findall('[0-9]+', data[1][0]).pop()
    log_data, success, fail = [], [], []
    for i in range(len(data)):
        try:
            if start <= data[i + 2][0].split('.')[0]:
                log_data.append(data[i + 2])
        except:
            continue
    print(log_data)
    for i in range(len(log_data)):
        for elem in log_data:
            # print(elem[i].split('.')[0])
            try:
                if elem[i].split('.')[0] > end:
                    # print(log_data[-i])
                    # print(elem[-i].split('.'))
                    try:
                        log_data.pop(i)
                    except:
                        continue
            except:
                continue
    # print(log_data)
    for elem in range(len(log_data)):
        if 'top up' in log_data[elem][0]:
            fill_attempts += 1
            if 'top up' and 'успех' in log_data[elem][0].split('.')[1].split('-')[1]:
                success.append(
                    log_data[elem][0].split('.')[1].split('-')[1].
                        replace('\n', ''))
            else:
                fill_fails += 1
        elif 'scoop' in log_data[elem][0]:
            if 'успех' in log_data[elem][0].split('.')[1].split('-')[1]:
                withdrawal_att += 1

            else:
                withdrawal_fails += 1
                fail.append(
                    log_data[elem][0].split('.')[1].split('-')[1].
                                    replace('\n', ''))
    try:
        fill_err_percent = fill_fails * 100 / fill_attempts
        withdrawal_err_pct = withdrawal_fails * 100 / fill_attempts
    except:
        ''

    return print(f'{success} omg {fail}')
    # return ''

if __name__ == '__main__':
    log_scraper(log, start, end)
    # save_data()
