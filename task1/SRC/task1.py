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


def ter(num):
    """конвертер троичной системы"""
    quotient = num / 3
    remainder = num % 3
    if quotient == 0:
        return ""
    else:
        return ter(int(quotient)) + str(int(remainder))


def main(nb, base_src='int', base_dst='hex'):
    """работает с двумя аргументами, третий используется для соответсвия ТЗ"""
    return print(num_converter(nb, base_dst))


if __name__ == '__main__':
    main(10, 'int', 'hen')