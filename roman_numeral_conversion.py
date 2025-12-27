"""
The rules of combination:
Rule 1: When certain numerals are repeated, the number represented by them is their sum. For example, II = 1 + 1 = 2, or XX = 10 + 10 = 20, or, XXX = 10 + 10 + 10 = 30.
Rule 2: It is to be noted that no Roman numerals can come together more than 3 times. For example, we cannot write 40 as XXXX
Rule 3: The letters V, L, and D are not repeated.
Rule 4: Only I, X, and C can be used as subtractive numerals. There can be 6 combinations when we subtract. These are IV = 5 - 1 = 4; IX = 10 - 1 = 9; XL = 50 - 10 = 40; XC = 100 - 10 = 90; CD = 500 - 100 = 400; and CM = 1000 - 100 = 900
Rule 5: When a Roman numeral is placed after another Roman numeral of greater value, the result is the sum of the numerals. For example, VIII = 5 + 1 + 1 + 1 = 8, or, XV = 10 + 5 = 15,
Rule 6: When a Roman numeral is placed before another Roman numeral of greater value, the result is the difference between the numerals. For example, IV = 5 - 1 = 4, or, XL = 50 - 10 = 40, or XC = 100 - 10 = 90
Rule 7: When a Roman numeral of a smaller value is placed between two numerals of greater value, it is subtracted from the numeral on its right. For example, XIV = 10 + (5 - 1) = 14, or, XIX = 10 + (10 - 1) = 19
Rule 8: To multiply a number by a factor of 1000 a bar is placed over it.
Rule 9: Roman numerals do not follow any place value system.
Rule 10: There is no Roman numeral for zero (0).
"""

num_dict = {
    'num1': 1,
    'num2': 2,
    'num3': 3,
    'num4': 4,
    'num5': 5,
    'num6': 6,
    'num7': 7,
    'num8': 8,
    'num9': 9,
    'num10': 10,
    'num11': 11,
    'num12': 12,
    'num13': 13,
    'num14': 14,
    'num15': 15,
    'num16': 2000,  # MM
    'num17': 56,  # LVI
    'num18': 26,  # XXVI
    'num19': 1911,  # MCMXI
    'num20': 160,  # CLX
}

rn_dict = {
    'rn1': 'I',
    'rn2': 'II',
    'rn3': 'III',
    'rn4': 'IV',
    'rn5': 'V',
    'rn6': 'VI',
    'rn7': 'VII',
    'rn8': 'VIII',
    'rn9': 'IX',
    'rn10': 'X',
    'rn11': 'XI',
    'rn12': 'XII',
    'rn13': 'XIII',
    'rn14': 'XIV',
    'rn15': 'XV',
    'rn16': 'MM',  # 2000
    'rn17': 'LVI',  # 56
    'rn18': 'XXVI',  # 26
    'rn19': 'MCMXI',  # 1911
    'rn20': 'CLX',  # 160
}

roman_numeral_value_dict = {
    'I':1,
    'IV':4,
    'V':5,
    'IX':9,
    'X':10,
    'XL':40,
    'L':50,
    'XC':90,
    'C':100,
    'CD':400,
    'D':500,
    'CM':900,
    'M':1000
}

def convert_rn_to_number(rn):
    number_list = []

    for value_index in range(len(rn)):
        if value_index < len(rn) - 1:
            if (roman_numeral_value_dict[rn[value_index]] > roman_numeral_value_dict[rn[value_index + 1]] or
                    roman_numeral_value_dict[rn[value_index]] == roman_numeral_value_dict[rn[value_index + 1]]):
                number_list.append(roman_numeral_value_dict[rn[value_index]])
            else:
                number_list.append(-roman_numeral_value_dict[rn[value_index]])
        else:
            number_list.append(roman_numeral_value_dict[rn[value_index]])
    return sum(number_list)


def convert_number_to_rn(num):
    rn = ''
    index = 0
    keys = list(roman_numeral_value_dict.keys()).reverse()
    length = len(keys)

    while index < length:
        if num > 0:
            numeral = num // roman_numeral_value_dict[keys[index]]
            num -= roman_numeral_value_dict[keys[index]] * numeral
            if numeral > 0:
                rn += keys[index] * numeral
            index += 1
        else:
            break
    return rn

if __name__ == '__main__':

    print('~~~~~~~~~~~~~~~ Roman Numeral to Number Converter ~~~~~~~~~~~~~~~')
    for key, value in rn_dict.items():
        print('------------------------------------------------------')
        print(f'{value} to number is: {convert_rn_to_number(value)}')

    print('\n\n~~~~~~~~~~~~~~~ Number to Roman Numeral Converter ~~~~~~~~~~~~~~~')
    for key, value in num_dict.items():
        print('------------------------------------------------------')
        print(f'{value} to number is: {convert_number_to_rn(value)}')
