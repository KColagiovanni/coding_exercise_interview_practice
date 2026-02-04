# Count the number of times a number shows up in a list.
import random

AMOUNT_OF_NUMBERS = 10000
RANGE_MIN = 0
RANGE_MAX = 9

numbers = []
for rand_num in range(AMOUNT_OF_NUMBERS):
    numbers.append(random.randint(RANGE_MIN, RANGE_MAX))

occurrences = {}

def count_number_of_occurrences(number):
    '''
    
    
    :param number: The number that will be 
    '''
    if number in occurrences:
        occurrences[number] += 1
    else:
        occurrences[number] = 1


if __name__ == "__main__":

    # Call the function for each number.
    for num in numbers:
        count_number_of_occurrences(num)

    # Display the Occurrences in a nice format.
    for key, val in occurrences.items():

        # Make the output look nicer.
        percent = (val/AMOUNT_OF_NUMBERS) * 100
        
        if val < 10:
            occurrences_string = f'Occurrences: {val}  '
        elif val < 100:
            occurrences_string = f'Occurrences: {val} '
        else:
            occurrences_string = f'Occurrences: {val}'

        print(f'Number: {key} | {occurrences_string} | {round(percent, 1)}%')