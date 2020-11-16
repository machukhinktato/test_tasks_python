def main(str1=None, str2=None):
    if str1 == None or str2 == None:
        return print('В функцию не были переданы аргументы.\n'
                     'Принимаются аргументы строчного типа.\n'
                     'Процесс будет завершен.')
    is_same = False
    length = len(str2[0:(str2.index('*'))])
    if '*' in str2:
        is_same = True if str1[0:length] == str2[0:length] else False
    elif str1 == str2:
        is_same = True
    elif "*" == str2[0]:
        is_same = True
    return print(['OK' if is_same else 'KO'][0])


if __name__ == '__main__':
    main('aaaa', '*')
