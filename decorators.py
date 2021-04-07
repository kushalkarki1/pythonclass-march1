# def decorate_func(func):
#     def wrapper():
#         print(f"func: {func}")
#         print("Nice to see u.")
#         func()
#         print("Welcome again.")
#     return wrapper

# @decorate_func
# def greet():
#     print("Welcome home.")

# greet()
# print(f"greet: {greet}")

def smart_division(func):
    def wrapper(a, b):
        if b == 0:
            return "could not divide by zero"
        else:
            return func(a, b)
    return wrapper

@smart_division
def division(num1, num2):
    return num1 / num2

print(division(10, 10))
print(division(10, 0))


def is_admin_required(func):
    def wrapper():
        if user is admin and user is salesperson:
            func()
        else:
            "invalid user"

def product_list():
    pass

@is_admin_required
def sales_report():
    pass

@is_admin_required
def product_price_history():
    pass