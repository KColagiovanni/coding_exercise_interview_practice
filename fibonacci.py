def fibonacci(n):
    """
    Generates the first n_terms of the Fibonacci sequence iteratively.
    """
    a, b = 0, 1  # Initial values.
    count = 0

    while count < n:
        # The new 'a' becomes the old 'b', and the new 'b' becomes the sum of the old 'a' and 'b'.
        temp = a
        a = b
        b = temp + b
        # a, b = b, a + b  # Pythonic
        count += 1
    print(f'The {n}th number in the Fibonacci sequence is: {a}')

if __name__ == '__main__':
    fibonacci(9)