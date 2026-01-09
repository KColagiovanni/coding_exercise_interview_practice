"""
Sensor Data Validation

Question:
You receive a stream of sensor readings from a manufacturing station. Each reading includes a timestamp and a value.
Write a function that detects whether any value exceeds an acceptable range for more than N consecutive samples.

Tests:
* Looping & conditionals
* Handling real-world constraints
* Safety logic

Follow-ups:
* How would you handle missing data?
* How would you make this configurable per product?
"""
import random
import time

sample_counter = []

def validate_data(timestamp, data_value, min_tol, max_tol, n_sample):
    """

    :param timestamp: The timestamp of the data.
    :param data_value: The value of the data.
    :param min_tol: The minimum allowable tolerance for the data value.
    :param max_tol: The maximum allowable tolerance for the data value.
    :param n_sample: The number of consecutive samples that can exceed an acceptable range for more than N samples.
    :return: (list) [(str) result: PASS/FAIL, (list) failed timestamps]
    """
    tolerance = 'In-Range'
    if data_value < min_tol or data_value > max_tol:
        sample_counter.append(timestamp)
        if data_value > max_tol:
            tolerance = 'TOO HIGH'
        elif data_value < min_tol:
            tolerance = 'TOO LOW'
        else:
            tolerance = "In-Range"
    print(f'Output - Timestamp:{timestamp} | Data: {data_value}({tolerance})')
    if len(sample_counter) == n_sample:
        out_of_tolerance_counter = 0
        for sample_index in range(1, len(sample_counter)):
            if sample_counter[sample_index - 1] == sample_counter[sample_index] - 1:
                out_of_tolerance_counter += 1
        if out_of_tolerance_counter == n_sample - 1:
            return ['FAIL', sample_counter]
        sample_counter.pop(0)

    return ['PASS', 0]

if '__main__' == __name__:

    data_samples = 100  # Number of times to create "fake" data.
    min_range = 40  # Lower range for the "fake" data.
    max_range = 60  # Upper range for the "fake" data.
    min_tolerance = 45  # Lower value for the tolerance.
    max_tolerance = 55  # Upper value for the tolerance.
    n_samples = 5  # Number of consecutive samples that can exceed an acceptable range.
    delay = .01 # Seconds

    # Create "fake" data
    for count in range(data_samples):

        # Send data to the function
        test_result = validate_data(
            count,
            random.randint(min_range, max_range),
            min_tolerance,
            max_tolerance,
            n_samples
        )

        # Check for failed results
        if test_result[0] == 'FAIL':
            print(f'Results: {test_result[0]} | (Timestamps: {test_result[1]})')
            break
        time.sleep(delay)  # Simulate data delay
