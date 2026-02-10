import random
from OOP_example_basic import Sensor

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
print(t)
