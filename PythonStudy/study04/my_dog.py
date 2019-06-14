"""导入dog模块"""
from study04.dog  import Dog
from study04.car import Car, ElectricCar

my_new_dog = Dog("while", 6)
print(my_new_dog.sit())

my_new_car = Car("volk", "beetle", 2016)
print(my_new_car.get_descriptive_name())

my_testa = ElectricCar('testa', 'roadster', 2016)
print(my_testa.get_descriptive_name())