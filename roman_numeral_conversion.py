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

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

Examples:
1 = I
2 = II
3 = III
4 = IV
5 = V
6 = VI
7 = VII
8 = VIII
9 = IV
10 = X
11 = XI
12 = XII
13 = XIII
14 = XIV
15 = XV
16 = XVI
17 = XVII
18 = XVIII
19 = XIX
20 = XX
"""

roman_numeral_dict = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000
}

def convert_rn_to_number(rn):
    # print(f'roman numeral: {rn}')
    # X = 10; I = -1; V = 5 --> 10 + -1 + 5 = 14
    number_list = []

    for value_index in range(len(rn)):
        if value_index < len(rn) - 1:
            if (roman_numeral_dict[rn[value_index]] > roman_numeral_dict[rn[value_index + 1]] or
                    roman_numeral_dict[rn[value_index]] == roman_numeral_dict[rn[value_index + 1]]):
                # print(f'1. appending {roman_numeral_dict[rn[value_index]]}')
                number_list.append(roman_numeral_dict[rn[value_index]])
            else:
                # print(f'2. appending {-roman_numeral_dict[rn[value_index]]}')
                number_list.append(-roman_numeral_dict[rn[value_index]])

        else:
            # print(f'3. appending {roman_numeral_dict[rn[value_index]]}')
            number_list.append(roman_numeral_dict[rn[value_index]])

    # print(f'sum of the number list is: {sum(number_list)}')
    return sum(number_list)


def convert_number_to_rn(num):

    rn = ''
    return rn

if __name__ == '__main__':
    num = 14
    rn1 = 'I'
    rn2 = 'II'
    rn3 = 'III'
    rn4 = 'IV'
    rn5 = 'V'
    rn6 = 'VI'
    rn7 = 'VII'
    rn8 = 'VIII'
    rn9 = 'IX'
    rn10 = 'X'
    rn11 = 'XI'
    rn12 = 'XII'
    rn13 = 'XIII'
    rn14 = 'XIV'
    rn15 = 'XV'
    rn16 = 'MM'  # 2000
    rn17 = 'LVI'  # 56
    rn18 = 'XXVI'  # 26
    rn19 = 'MCMXI'  # 1911
    rn20 = 'CLX'  # 160
    print('\n------------------------------------------------------')
    print(f'{rn1} to number is: {convert_rn_to_number(rn1)}')
    print('\n------------------------------------------------------')
    print(f'{rn2} to number is: {convert_rn_to_number(rn2)}')
    print('\n------------------------------------------------------')
    print(f'{rn3} to number is: {convert_rn_to_number(rn3)}')
    print('\n------------------------------------------------------')
    print(f'{rn4} to number is: {convert_rn_to_number(rn4)}')
    print('\n------------------------------------------------------')
    print(f'{rn5} to number is: {convert_rn_to_number(rn5)}')
    print('\n------------------------------------------------------')
    print(f'{rn6} to number is: {convert_rn_to_number(rn6)}')
    print('\n------------------------------------------------------')
    print(f'{rn7} to number is: {convert_rn_to_number(rn7)}')
    print('\n------------------------------------------------------')
    print(f'{rn8} to number is: {convert_rn_to_number(rn8)}')
    print('\n------------------------------------------------------')
    print(f'{rn9} to number is: {convert_rn_to_number(rn9)}')
    print('\n------------------------------------------------------')
    print(f'{rn10} to number is: {convert_rn_to_number(rn10)}')
    print('\n------------------------------------------------------')
    print(f'{rn11} to number is: {convert_rn_to_number(rn11)}')
    print('\n------------------------------------------------------')
    print(f'{rn12} to number is: {convert_rn_to_number(rn12)}')
    print('\n------------------------------------------------------')
    print(f'{rn13} to number is: {convert_rn_to_number(rn13)}')
    print('\n------------------------------------------------------')
    print(f'{rn14} to number is: {convert_rn_to_number(rn14)}')
    print('\n------------------------------------------------------')
    print(f'{rn15} to number is: {convert_rn_to_number(rn15)}')
    print('\n------------------------------------------------------')
    print(f'{rn16} to number is: {convert_rn_to_number(rn16)}')
    print('\n------------------------------------------------------')
    print(f'{rn17} to number is: {convert_rn_to_number(rn17)}')
    print('\n------------------------------------------------------')
    print(f'{rn18} to number is: {convert_rn_to_number(rn18)}')
    print('\n------------------------------------------------------')
    print(f'{rn19} to number is: {convert_rn_to_number(rn19)}')
    print('\n------------------------------------------------------')
    print(f'{rn20} to number is: {convert_rn_to_number(rn20)}')
    print('\n------------------------------------------------------')
    print('\n')
    print(f'{num} to Roman Numeral is: {convert_number_to_rn(num)}')
