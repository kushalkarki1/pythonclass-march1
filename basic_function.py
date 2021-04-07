# def func_name():
    # function body
    # code or instructions

# def demo():
#     print("This is demo function")

# demo => call by reference
# demo() # => call for execution

# def welcome(name): # name => parameter
#     print("Welcome", name)

# welcome("Ram") # "Ram" => argument
# welcome("Shyam") # "Shyam" => argument
# welcome("Hari") # "Hari" => argument

# def display_profile(name, address, contact, country="Nepal"):
#     print("Name", name)
#     print("Address", address)
#     print("Contact", contact)
#     print("Country", country)

# display_profile("Ram", "Ktm", "987323")
# print("---------------------------------")
# display_profile("Shyam", "Kabul", "987323", "Afganistan")
# positional argument
# print("---------------------------------")
# display_profile(name="Shyam", contact="98433", address="Pkr")
# keyword argument


# Function with return type and
# without return type

# def add(num1, num2):
#     total = num1 + num2
#     return total

# res = add(10, 8)
# print("Result", res)

def difference(num1, num2):
    if num1 >  num2:
        return num1 - num2
    else:
        return num2 - num1

def product(num1, num2):
    return num1 * num2

print(difference(10, 8))
print(difference(8, 10))
print(product(10, 8))
# 18
# None -> NoneType