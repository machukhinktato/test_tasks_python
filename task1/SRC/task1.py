def num_converter(num, dest_base):
    values = {
        'hex': hex(num).replace('0x', ''),
        'oct': oct(num).replace('0o', ''),
        'ter': ter(num),
        'bin': bin(num).replace('0b', ''),
        'int': int,
        'cats': 'meow'.replace('o', 'o' * num),
    }

    return values.get(dest_base)


def ter(num):
    """ternary numeral system converter"""
    quotient = num / 3
    remainder = num % 3
    if quotient == 0:
        return ""
    else:
        return ter(int(quotient)) + str(int(remainder))


def main():
    return print(num_converter(15, 'cats'))


if __name__ == '__main__':
    num_converter(15, 'cats')
    main()
