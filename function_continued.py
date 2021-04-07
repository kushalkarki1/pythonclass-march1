# def func(*args):
#     print(args)

# func(1, 2, 3, 4, "python")

# def func(**kwargs):
#     print(kwargs)

# func(name="Ram", contact="932723")

# def func(*args, **kwargs):
#     print(args, kwargs)

# func(1, 2, 3, 4, "python", name="Ram", contact="932723")

# def welcome(name):
#     print(f"Welcome {name}")

# w = welcome # call by reference
# w("Shyam")

# def welcome(name):
#     print(f"Welcome {name}")

# def namaste(name):
#     print(f"Namaste {name}")

# def greet(f, name):
#     # f -> welcome
#     # f() -> welcome()
#     f(name)

# greet(welcome, "Harry")
# greet(namaste, "Ram")

# def main():
#     def inner_func():
#         print("I am inner function.")

#     return inner_func

# f = main()
# f()
# f()

# def main(n):
#     def addition(a, b):
#         return a + b
#     def subtraction(a, b):
#         return a - b
#     if n == 1:
#         return addition
#     elif n == 2:
#         return subtraction

# add = main(1)
# print(add(10, 9))

# sub = main(2)
# print(sub(19, 9))

# num = 10 # Immutable object

# def func():
#     global num
#     num = num + 1
#     print(num)

# func()

# alist = [1, 2, 3, 4]

# def func():
#     alist.append(89)

# print(alist)
# func()
# print(alist)


# def main():
#     num = 10
#     def inner_func():
#         nonlocal num
#         num = num + 1
#         print(num)
#     inner_func()

# main()

