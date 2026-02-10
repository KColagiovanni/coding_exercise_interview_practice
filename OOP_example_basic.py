import random

class Sensor:

    def __init__(self, sensor_id, min_value, max_value):
        self.sensor_id = sensor_id
        self.min_value = min_value
        self.max_value = max_value
        self.readings = []

    def add_reading(self, value):
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"Reading {value} out of range")
        self.readings.append(value)

    def average(self):
        if not self.readings:
            return None
        return sum(self.readings) / len(self.readings)

    def __str__(self):
        return f'Sensor({self.sensor_id}, readings={len(self.readings)})'

temp_sensor = Sensor("TEMP-001", 20, 35)
# temp_sensor.add_reading(25)
# temp_sensor.add_reading(30)
for temp_value in range(100):
    temp_sensor.add_reading(random.randint(20, 35))

print(f'Avg Temp: {temp_sensor.average()}*c')
print(temp_sensor)
