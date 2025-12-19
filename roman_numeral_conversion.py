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

def convert_rn_to_number(rn):
    roman_numeral_dict = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }



    number = 0
    for numeral in range(len(rn)):
        # print(f'{numeral} -> {rn[numeral]}')
        if rn[numeral] == 'I':
            number += 1
        elif rn[numeral] == 'V':
            number += 5
        elif rn[numeral] == 'X':
            number += 10
        elif rn[numeral] == 'L':
            number += 50
        elif rn[numeral] == 'C':
            number += 100
        elif rn[numeral] == 'D':
            number += 500
        elif rn[numeral] == 'M':
            number += 1000
    return number

def convert_number_to_rn(num):
    rn = ''
    return rn

if __name__ == '__main__':
    num = 14
    rn1 = 'XIII'
    rn2 = 'XIX'
    print(f'{num} to Roman Numeral is: {convert_number_to_rn(num)}')
    print('\n')
    print(f'{rn1} to number is: {convert_rn_to_number(rn1)}')
    print(f'{rn2} to number is: {convert_rn_to_number(rn2)}')