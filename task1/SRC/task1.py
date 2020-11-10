def num_converter(num, dest_base, dest_src=None):


    values = {
        'hex': hex(num).replace('0x', ''),
        'oct': oct(num).replace('0o', ''),
        'ter': ter(num),
        'bin': bin(num).replace('0b', ''),
        'int': int,
        'cats': 'meow'.replace('o', 'o' * num),
    }
    # result = f"{(values.get(dest_base)).replace('o', 'o' * int(num))}" if \
    #     dest_base == 'cats' else values.get(dest_base)(num)


    # return print(result, end='\n')
    return print(values.get(dest_base))



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
    num_converter(15, 'cats')
