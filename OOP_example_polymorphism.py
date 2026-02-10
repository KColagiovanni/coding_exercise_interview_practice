import random
from OOP_example_basic import Sensor

# Polymorphism
'''
The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same 
name that can be executed on many objects or classes. An example of a Python function that can be used on different 
objects is the len() function.
'''
class PressureSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id, min_value=0, max_value=300)
        self.readings = []

    def add_reading(self, value):
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"Reading {value} out of range")
        self.readings.append(value)

    def average(self):
        avg = super().average()
        if avg is None:
            return None
        return round(avg, 2)

    def __str__(self):
        return f'Sensor({self.sensor_id}, readings={len(self.readings)})'

psi = PressureSensor("PSI-001")

for psi_value in range(100):
    psi.add_reading(random.randint(100, 200))

print(f'Avg Pressure: {psi.average()}psi')
print(psi)
