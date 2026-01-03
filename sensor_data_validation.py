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

file_path = 'fake_data.txt'
def create_fake_sensor_data():
    with open(file_path, 'w') as fake_file:
        for count in range(100):
            fake_file.write(f'{count + 1}: {random.randint(40, 60)}\n')
    fake_file.close()

# def validate_data(file_path, tolerance):
#     out_of_range_values = {0:0}
#     value_checker = []
#     out_of_range = 0
#     result = 'Pass'
#
#     with open(file_path, 'r') as fake_file:
#         for line in fake_file:
#             # validate_data()
#             count = int(line.split(':')[0])
#             data_value = int(line.split(':')[1])
#             # print(f'line is: {type(line)}')
#             # print(f'{count}: {data_value}')
#             if data_value < 45 or data_value > 55:
#                 out_of_range_values[count] = data_value
#                 # print(f'{data_value} is outside of the range.')
#     fake_file.close()
#
#     for key, value in out_of_range_values.items():
#         print(f'{key}: {value}')
#         value_checker.append(key)
#         if value_checker:
#             out_of_range +=1
#             print(f'out of range is: {out_of_range}')
#             if out_of_range == tolerance:
#                 result = "Fail"
#         else:
#             out_of_range = 0
#
#     return result

out_of_range_values = []

def validate_data(timestamp, data_value, min_tolerance, max_tolerance, n_samples):
    if data_value < min_tolerance or data_value > max_tolerance:
        out_of_range_values.append(timestamp)
    # print(f'length of out_of_range_values is: {len(out_of_range_values)}')

    tolerance_exceeded = 0
    # print(f'len(out_of_range_values) == n_samples is: {len(out_of_range_values) == n_samples}')
    if len(out_of_range_values) == n_samples:
        for index in range(len(out_of_range_values)):
            print(out_of_range_values)
            print(f'\nout_of_range_values[index] is: {out_of_range_values[index - 1]}')
            print(f'out_of_range_values[index + 1] + 1 is: {out_of_range_values[index] - 1}')
            print(f'out_of_range_values[index] == out_of_range_values[index + 1] is: {out_of_range_values[index - 1] == out_of_range_values[index] - 1}')
            if index == 0:
                if out_of_range_values[index] == out_of_range_values[index + 1] - 1:
                    tolerance_exceeded += 1
            else:
                if out_of_range_values[index - 1] == out_of_range_values[index] - 1:
                    tolerance_exceeded += 1
                    if tolerance_exceeded == n_samples:
                        return 'FAIL', out_of_range_values
        out_of_range_values.pop(0)
    return 'PASS'

if '__main__' == __name__:
    # create_fake_sensor_data()
    # print(validate_data('fake_data.txt', 5))
    result = 'PASS'
    with open(file_path, 'r') as fake_file:
        for line in fake_file:
            # validate_data()
            counter = int(line.split(':')[0])
            data = int(line.split(':')[1])
            function = validate_data(counter, data, 45, 55, 5)
            if function[0] == 'FAIL':
                result = function
    fake_file.close()
    print(f'Result is: {result[0]} | Timestamp values: {result[1]}')