# Find the first non-repeating character for each string in a list of strings.

# All strings are 15 char long.
# Needs to be improved because the first letter is not a repeated character. so for the string "pyyyyyyyyyyyyyy", y
# should not be the first non-repeated char.

strings = [
    'aaaaaaaaaeaaaaa',
    'wdwwwwwwwwwwwww',
    'pyyyyyyyyyyyyyy',
    'jjjjjjjkjjjjjjj',
    'xxxxxxxxxxxxxxz',
    'rrrrrrstttttttt',
    'ddddddddddddddd',
    'abcdefghijklmno'
]

def find_non_repeater(value):
    initial_value = ''
    for char_index in range(len(value)):
        if char_index == 0:
            initial_value = value[char_index]
        else:
            if value[char_index] == initial_value:
                continue
            else:

                return value[char_index]

if __name__ == '__main__':

    for string in strings:
        output = find_non_repeater(string)
        if output:
            print(f'{output} is the first non-repeated word in {string}')
        else:
            print(f'{string} did not have any repeating characters.')