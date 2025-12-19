def reverse_string(string):
    print(f'Normal input is: {string}')
    rev_string = ''
    for char in range(len(string)):
        last_char = string[-1 - char]
        rev_string += last_char
    print(f'Reversed input is: {rev_string}')

def pythonic_reverse_string(string):
    print(f'Normal input is: {string}')
    print(f'Reversed input is: {string[::-1]}')

if __name__ == '__main__':
    print(f'My reverse version')
    reverse_string('colagiovanni')

    print('\nPythonic Reverse String')
    pythonic_reverse_string('colagiovanni')