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
    if word == word[::-1]:  # Pythonic
        print(f'{word} is a palindrome')
    else:
        print(f'"{word}" is NOT a palindrome')

if __name__ == '__main__':
    for word in word_list:
        is_it_a_palindrome(word)