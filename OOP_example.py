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


# Inheritance
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''
class TemperatureSensor(Sensor):

    # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.
    # Python also has a super() function that will make the child class inherit all the methods and properties from its
    # parent. By using the super() function, you do not have to use the name of the parent element, it will
    # automatically inherit the methods and properties from its parent.

    def __init__(self, sensor_id):
        super().__init__(sensor_id, min_value=20, max_value=35)


    # If you add a method in the child class with the same name as a function in the parent class, the inheritance of
    # the parent method will be overridden.
    def to_fahrenheit(self):
        avg = self.average()
        if avg is None:
            return None
        return avg * 9 / 5 + 32

t = TemperatureSensor("TEMP-002")
# t.add_reading(20)
# t.add_reading(22)
for temp_value in range(100):
    t.add_reading(random.randint(20, 35))

print(f'Avg Temp: {t.to_fahrenheit()}*f')


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
