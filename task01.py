def num_converter(num, value):
    # num = int(input('Please, enter a number: '))
    # value = input('Convert to? (hex, bin, dec, cats)')

    values = {
        'hex': hex,
        'bin': bin,
        'int': int,
        'cats': 'meow',
    }
    result = f"{(values.get(value)).replace('o', 'o' * num)}" if value == 'cats' else values.get(value)(num)
    
    return print(result)


if __name__ == '__main__':
    num_converter(15, 'cats')
