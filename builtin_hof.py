# map and filter

# lambda x1, x2: x1 + x2
# def a(x1, x2):
#     return x1 + x2
# a = lambda x1, x2: x1 + x2
# print(a(10, 9))

# map(func ,iterable_object)

# def increase_by_one(n):
#     return n+1

# alist = [2, 4, 6, 8, 10, 12, 14, 16, 18]
# res = map(lambda n:n+1, alist)
# print(list(res))

namelist = ["ram", "shyam", "geeta", "meera",
            "monster", "suzan", "sabin"]
# res = ["Ram", "Shyam"]
res = map(lambda name:name.title(), namelist)
# print(list(res))

emaillist = ["1-gmail.com", "2-gmail.com", "3-gmail.com",
            "4-gmail.com", "5-gmail.com"]

res = map(lambda email:email.replace("-", "@"), emaillist)
# print(list(res))

# filter
# filter(func, iterable_object)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
evelist = filter(lambda n:n % 2 == 0, a)
print(list(evelist))

emailist = ["1@gmail.com", "2@gmail.com",
            "3@hotmail.com", "4@yahoo.com",
            "5@gmail.com"]

res = filter(lambda e:e.endswith("gmail.com"), emailist)
print(list(res))