# try:
#     num1 = int(input("Enter any number: "))
#     num2 = int(input("Enter another number: "))
# except ValueError:
#     print("input must be number")
# except NameError as err:
#     print(err)
# else:
#     print(f"Sum of {num1} and {num2} is {num1+num2}.")
# finally:
#     print("Completed")

# name = input("Enter name: ")
# print(f"Your name is {name}.")
# print("Program completed.")

# a = [1, 2, 3, 4]

# try:
#     a.pop()
#     print(a[3])
# except IndexError as err:
#     print(err)

a = [
        {"1":
            {
            "name": ["Ram", "Kumar", "Shrestha"]
            },
            "contact":{
                "home": ["01-98752141"],
                "office": ["01-7654563"]
            }
        }
    ]
# print(a[])
# Your name is Ram Kumar Shrestha
# Your home contact is 01-98752141
# Your office contact is 01-7654563

fullname = a[0].get("1").get("name")
print(" ".join(fullname))

# try:
#     pass
# except Exception:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass