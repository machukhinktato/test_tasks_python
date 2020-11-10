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

    return values.get(dest_base)


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
    num_converter(0xf, 'int')
    main()
