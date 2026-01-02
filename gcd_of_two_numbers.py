def gcd(a, b):
    denominator = 0

    while True:
        denominator += 1
        if denominator % a == 0 and denominator % b == 0:
            break
    print(f'The GCD of {a} and {b} is {denominator}')

if __name__ == '__main__':
    gcd(23764, 21349)