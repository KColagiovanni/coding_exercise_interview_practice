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
        return f"Sensor({self.sensor_id}, readings={len(self.readings)})"

temp_sensor = Sensor("TEMP-001", -40, 125)
# temp_sensor.add_reading(25)
# temp_sensor.add_reading(30)
for temp_value in range(100):
    temp_sensor.add_reading(random.randint(20, 35))

print(temp_sensor.average())   # 27.5
print(temp_sensor)             # Sensor(TEMP-001, readings=2)

class TemperatureSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id, min_value=-40, max_value=125)

    def to_fahrenheit(self):
        avg = self.average()
        if avg is None:
            return None
        return avg * 9 / 5 + 32

t = TemperatureSensor("TEMP-002")
t.add_reading(20)
t.add_reading(22)

print(t.to_fahrenheit())  # 71.6

class PressureSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id, min_value=0, max_value=300)

    def average(self):
        avg = super().average()
        if avg is None:
            return None
        return round(avg, 2)