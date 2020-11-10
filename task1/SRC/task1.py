def num_converter(num, dest_base):
    """общий конвертер систем счисления"""

    values = {
        'hex': hex(num).replace('0x', ''),
        'oct': oct(num).replace('0o', ''),
        'ter': ter(num),
        'bin': bin(num).replace('0b', ''),
        'int': int(num),
        'cats': 'meow'.replace('o', 'o' * num),
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
        return ter(int(quotient)) + str(int(remainder))


def ter(num):
    """ Конвертер троичной системы с реализацией отрицательной степени"""
    return tern_num(num) if num > 0 else f'-{tern_num(num)}'


def main(nb, base_src, base_dst):
    """ """
    # nb = input('Введите число: ')
    # base_src = input('начальная система счисления числа: ')
    # base_dst = input('конечная система счисления числа: ')
    values = {
        'hex': 16,
        'int': 10,
        'oct': 8,
        'ter': 3,
        'bin': 2,
        'cats': 'meow',
    }
    if 'cats' in base_src:
        nb, base_src = nb.count('o'), None
        return print(num_converter(nb, base_dst))
    try:
        nb = int(nb, values.get(base_src))
        return print(num_converter(nb, base_dst))
    except Exception as e:
        # if 'cats' in base_src
        print(e)


if __name__ == '__main__':
    main('-15', 'int', 'ter')
