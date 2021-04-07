# 1. Class and object
    # Noun -> object
    # adjective -> property (characterstics)
    # verb (action) -> behaviour (method)(function)
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism
# 5. Abstraction
# 6. Access modifier
# 7. Accessor and Mutator function
#   ->Getter      ->Setter

# class Laptop:
    # Initializer function (initailize object)
#     def __init__(self, brand, color, ram):
#         self.brand = brand
#         self.color = color
#         self.ram = ram

#     def power_on(self):
#         print(f"{self.brand} laptop is starting.")

#     def reboot(self):
#         print(f"{self.brand} laptop is rebooting.")

# d= Laptop("LENOVO", "Black", "16 GB")
# l = Laptop("DELL", "Silver", "8 GB")
# print(d.__dict__)
# print(l.__dict__)
# d.power_on()
# l.power_on()

# class -> Car
# attribute -> brand, year, color
# method-> start

# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     # instance method
#     def add(self):
#         return self.num1 + self.num2

#     def difference(self):
#         return self.num1 - self.num2

#     def product(self):
#         return self.num1 * self.num2

#     @staticmethod
#     def square_root(num):
#         return num ** 0.5

# c = Calculator(19, 10)
# # print(c.add())
# # print(c.difference())
# # print(c.product())
# print(c.square_root(100))

# class Student:
#     # class or static variable
#     college_name = "ABC College"

#     def __init__(self, _id, name, contact):
#         # instance variable
#         self._id = _id
#         self.name = name
#         self.contact = contact

# st = Student("001", "Ram", "987654321")
# std = Student("002", "Shyam", "98765407")
# print(Student.college_name)
# # print(std.__dict__)

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         # _Product__price
#         # Name Managaling _ClassName__attrname
#         self.__price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, price):
#         if price > 0:
#             self.__price = price

#     # def get_price(self):
#     #     return self.__price

#     # def set_price(self, price):
#     #     self.__price = price

# pant = Product("Pant", 1600)
# # print(pant.get_price())
# # pant.set_price(1700)
# print(f"Initial value: {pant.price}")
# pant.price = 900
# print(f"Final Value: {pant.price}")
# print(pant.__dict__)

# class Product:

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __eq__(self, obj):
#         return self.price == obj.price

#     def __add__(self, obj):
#         return self.price + obj.price

# pant = Product("Pant", 1600)
# tshirt = Product("Tshirt", 1600)
# print(pant.__eq__(tshirt))
# print(pant+tshirt)