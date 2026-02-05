# Count the occurrences of each letter in a list of words.

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

occurrences = {}

def count_number_of_letters(letter):
    """
    Takes a letter and adds it to a dict as a key, if that letter is encountered again, the count will be increased by
    1.
    :param letter: (string/char) The letter that will be counted.
    """
    if letter in occurrences:
        occurrences[letter] += 1
    else:
        occurrences[letter] = 1


if __name__ == "__main__":
    letter_counter = 0

    # Iterate through the list of words.
    for word in words:

        # Call the function for each letter.
        for letter in word:
            letter_counter += 1
            count_number_of_letters(letter)

    # Display the Occurrences in a nice format.
    for key, val in occurrences.items():

        # Make the output look nicer(for 3 digits max).
        percent = (val/letter_counter) * 100

        if val < 10:
            occurrences_string = f'Occurrences: {val}  '
        elif val < 100:
            occurrences_string = f'Occurrences: {val} '
        else:
            occurrences_string = f'Occurrences: {val}'

        print(f'Letter: {key} | {occurrences_string} | {round(percent, 1)}%')