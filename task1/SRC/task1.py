def num_converter(num, dest_base):
    """общий конвертер систем счисления"""

    values = {
        'hex': hex(num).replace('0x', ''),
        'oct': oct(num).replace('0o', ''),
        'ter': ter(num),
        'bin': bin(num).replace('0b', ''),
        'dec': int(num),
        'cats': '(^o_o^)~ ' * (num),
    }

    if dest_base in values.keys():
        return values.get(dest_base)
    else:
        return f'Система счисления `{dest_base}` и/или число `{num}` указаны некорректно \n' \
               f'для корректоной работы функции используйте числа с положительными значениями\n' \
               f'системы счисления указывайте как: hex, dec, ter, bin, int, cats'


def tern_num(num):
    """конвертер троичной системы"""
    quotient = num / 3
    remainder = num % 3
    if quotient == 0:
        return ""
    else:
        return tern_num(int(quotient)) + str(int(remainder))


def ter(num):
    """ Конвертер троичной системы с реализацией отрицательной степени"""
    a = tern_num(num) if num > 0 else f'-{tern_num(num)}'
    return int(a)


def main(nb, base_src, base_dst):
    """
    Основная функция вызова программы, принимает число, базовую и конечную
    систему счисления
    """
    # nb = input('Введите число: ')
    # base_src = input('начальная система счисления: ')
    # base_dst = input('конечная система счисления: ')
    values = {
        'hex': 16,
        'dec': 10,
        'oct': 8,
        'ter': 3,
        'bin': 2,
    }
    if 'cats' in base_src:
        try:
            nb, base_src = nb.count('~'), None
            return print(num_converter(nb, base_dst))
        except:
            return usage()
    try:
        nb = int(nb, values.get(base_src))
        return print(num_converter(nb, base_dst))
    except:
        return usage()


def usage():
    return print(f'Система счисления и/или число указаны некорректно\n'
                 f'для корректоной работы программы используйте целые числа или\n'
                 f'их аналогии в необходимой системе счисления(указаны ниже), а\n'
                 f'систему счисления указывайте как: \n'
                 f'bin - двоичная, ter - троичная, oct - восьмеричная,\n'
                 f'dec - десятичная, hex - шестнадцеричная, cats - в котиках.\n'
                 f'Принимаются только данные строчного типа')


if __name__ == '__main__':
    main(1010, 'bin', 'hex')
