word_list = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'racecar'
]

def is_it_a_palindrome(word):
    """ Check if a word is the same forwards and backwards """

    # Non-Pythonic way.
    rev_string = ''
    for char in range(len(word)):
        last_char = word[-1 - char]
        rev_string += last_char

    # if word == word[::-1]:  # Pythonic
    if word == rev_string:
        print(f'{word} is a palindrome')
    else:
        print(f'"{word}" is NOT a palindrome')

if __name__ == '__main__':
    for phrase in word_list:
        is_it_a_palindrome(phrase)