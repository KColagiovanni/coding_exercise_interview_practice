# Count the number of times a number shows up in a list.
numbers = [5, 8, 3, 7, 3, 9, 4, 5, 1, 6, 3, 8, 5, 3, 3, 5, 4, 2, 2, 3, 7, 6, 8, 7, 8, 4, 2, 2, 6, 5]
occurrences = {}

def count_number_of_occurrences(number):
    if number in occurrences:
        occurrences[number] += 1
    else:
        occurrences[number] = 1


if __name__ == "__main__":
    for num in numbers:
        count_number_of_occurrences(num)
    print(f'The Occurrences are:\n{occurrences}')