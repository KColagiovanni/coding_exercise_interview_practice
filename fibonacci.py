def fibonacci(n):
    """
    Generates the first n_terms of the Fibonacci sequence iteratively.
    :param n: (int) The Nth term in the Fibonacci sequence.
    :return: None
    """
    a, b = 0, 1  # Initial values of the Fibonacci sequence.
    count = 0

    while count < n:
        # The new 'a' becomes the old 'b', and the new 'b' becomes the sum of the old 'a' and 'b'.
        temp = a
        a = b
        b = temp + b
        # a, b = b, a + b  # Pythonic way to accomplish the above 3 lines.
        count += 1
    print(f'The {n}th number in the Fibonacci sequence is: {a}')

if __name__ == '__main__':
    fibonacci(20577)