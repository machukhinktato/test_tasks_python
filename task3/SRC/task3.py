import csv


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
    # for i in range(len(data)):
    #     data[i][0].replace('\n', '')
    #     print(data[i][0])
    return data


if __name__ == '__main__':
    # log_scraper()
    save_data()
