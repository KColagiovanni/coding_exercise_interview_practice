"""
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

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
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

    number = 0
    for numeral in range(len(rn)):
        # print(f'{numeral} -> {rn[numeral]}')
        if rn[numeral] == 'I':
            if numeral == 0 or numeral == len(rn) -1:
                number += roman_numeral_dict['I']
            else:
                if rn[numeral] < rn[numeral + 1]:
                    number -= roman_numeral_dict['I']
                else:
                    number += roman_numeral_dict['I']
        
        elif rn[numeral] == 'V':
            if numeral == 0 or numeral == len(rn) -1:
                number += roman_numeral_dict['V']
            else:
                if rn[numeral] < rn[numeral + 1]:
                    number -= roman_numeral_dict['V']
                else:
                    number += roman_numeral_dict['V']
        
        elif rn[numeral] == 'X':
            if numeral == 0 or numeral == len(rn) -1:
                number += roman_numeral_dict['X']
            else:
                if rn[numeral] < rn[numeral + 1]:
                    number -= roman_numeral_dict['X']
                else:
                    number += roman_numeral_dict['X']
        
        elif rn[numeral] == 'L':
            if numeral == 0 or numeral == len(rn) -1:
                number += roman_numeral_dict['L']
            else:
                if rn[numeral] < rn[numeral + 1]:
                    number -= roman_numeral_dict['L']
                else:
                    number += roman_numeral_dict['L']
        
        elif rn[numeral] == 'C':
            if numeral == 0 or numeral == len(rn) -1:
                number += roman_numeral_dict['C']
            else:
                if rn[numeral] < rn[numeral + 1]:
                    number -= roman_numeral_dict['C']
                else:
                    number += roman_numeral_dict['C']
        
        elif rn[numeral] == 'D':
            if numeral == 0 or numeral == len(rn) -1:
                number += roman_numeral_dict['D']
            else:
                if rn[numeral] < rn[numeral + 1]:
                    number -= roman_numeral_dict['D']
                else:
                    number += roman_numeral_dict['D']
        
        elif rn[numeral] == 'M':
            if numeral == 0 or numeral == len(rn) -1:
                number += roman_numeral_dict['M']
            else:
                if rn[numeral] < rn[numeral + 1]:
                    number -= roman_numeral_dict['M']
                else:
                    number += roman_numeral_dict['M']
    return number


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
    rn9 = 'MM'
    rn10 = 'MCMXCIX'
    print(f'{rn1} to number is: {convert_rn_to_number(rn1)}')
    print(f'{rn2} to number is: {convert_rn_to_number(rn2)}')
    print(f'{rn3} to number is: {convert_rn_to_number(rn3)}')
    print(f'{rn4} to number is: {convert_rn_to_number(rn4)}')
    print(f'{rn5} to number is: {convert_rn_to_number(rn5)}')
    print(f'{rn6} to number is: {convert_rn_to_number(rn6)}')
    print(f'{rn7} to number is: {convert_rn_to_number(rn7)}')
    print(f'{rn8} to number is: {convert_rn_to_number(rn8)}')
    print(f'{rn9} to number is: {convert_rn_to_number(rn9)}')
    print(f'{rn10} to number is: {convert_rn_to_number(rn10)}')
    print('\n')
    print(f'{num} to Roman Numeral is: {convert_number_to_rn(num)}')
