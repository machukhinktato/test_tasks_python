def num_converter(num, dest_base, dest_src=None):
    # num = int(input('Please, enter a number(here may be any format): '))
    # src_base = input('Convert to? (hex, bin, dec, cats)')

    values = {
        'hex': hex,
        'oct': oct,
        'ter': ter,
        'bin': bin,
        'int': int,
        'cats': 'meow',
    }
    result = f"{(values.get(dest_base)).replace('o', 'o' * int(num))}" if \
        dest_base == 'cats' else values.get(dest_base)(num)

    return print(result, '\n')



def ter(num):
    """ternary numeral system converter"""
    quotient = num/3
    remainder = num%3
    if quotient == 0:
        return ""
    else:
        return ter(int(quotient)) + str(int(remainder))


# number = int(input("Enter a number : ")) #1
# print(ter(123))


if __name__ == '__main__':
    num_converter(15, 'oct')
