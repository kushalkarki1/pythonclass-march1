# Child class "IS A" Parent Class

# class Person:
#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact

#     def walk(self):
#         print(f"{self.name} is walking.")

# class Student(Person):
#     def __init__(self, name, contact):
#         super().__init__(name, contact)

# class Teacher(Person):
#     def __init__(self, name, contact):
#         super().__init__(name, contact)

# st = Student("Ram", "987654321")
# st.walk()
# t = Teacher("Shyam", "987654")
# t.walk()

class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying.")

class Pigeon(Bird):
    def __init__(self, name):
        super().__init__(name)

class Ostrich(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        print(f"{self.name} could not fly.")

class HummingBird(Bird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        super().fly()
        print(f"{self.name} can also fly backward.")

p = Pigeon("Sabin")
p.fly()
o = Ostrich("Monster")
o.fly()
h = HummingBird("Saugat")
h.fly()

p = Pigeon("Saugat")
p.fly()