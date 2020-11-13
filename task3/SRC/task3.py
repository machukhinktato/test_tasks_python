def file_loader(data):
    with open(data, 'r', encoding='utf8') as f:
        file = f.readlines()

        return file


def log_scraper():
    data = file_loader('log.log')
    data = [i.split(',') for i in data]
    return print(data[0][0])


if __name__ == '__main__':
    log_scraper()
