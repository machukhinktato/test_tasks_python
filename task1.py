def num_converter(num, dest_base):
    # num = int(input('Please, enter a number(here may be any format): '))
    # src_base = input('Convert to? (hex, bin, dec, cats)')

    values = {
        'hex': hex,
        'bin': bin,
        'int': int,
        'cats': 'meow',
    }
    result = f"{(values.get(dest_base)).replace('o', 'o' * int(num))}" if dest_base == 'cats' else values.get(dest_base)(num)

    return print(result)


if __name__ == '__main__':
    num_converter(0xf, 'cats')
