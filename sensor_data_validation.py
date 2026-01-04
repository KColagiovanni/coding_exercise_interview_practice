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

def validate_data(timestamp, data_value, min_tolerance, max_tolerance, n_samples):
    tolerance = 'In-Range'
    if data_value < min_tolerance or data_value > max_tolerance:
        sample_counter.append(timestamp)
        if data_value > max_tolerance:
            tolerance = 'TOO HIGH'
        elif data_value < min_tolerance:
            tolerance = 'TOO LOW'
        else:
            tolerance = "In-Range"
    print(f'Output - Timestamp:{timestamp} | Data: {data_value}({tolerance})')
    if len(sample_counter) == n_samples:
        out_of_tolerance_counter = 0
        for sample_index in range(1, len(sample_counter)):
            if sample_counter[sample_index - 1] == sample_counter[sample_index] - 1:
                out_of_tolerance_counter += 1
        if out_of_tolerance_counter == n_samples - 1:
            return ['FAIL', sample_counter]
        sample_counter.pop(0)

    return ['PASS', 0]

if '__main__' == __name__:
    for count in range(100):
        test_result = validate_data(count, random.randint(40, 60), 45, 55, 5)
        if test_result[0] == 'FAIL':
            print(f'Results: {test_result[0]} | (Timestamps: {test_result[1]})')
            break
        time.sleep(.1)