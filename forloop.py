# for <variable> in <iterable_object>:
    # code to repeat
# alist = ["ram", "shyam", "hari", "sita"]
# blist = [1, 2, 3, 4, 5, 6]

# for item in alist:
#     print(item)

# for item in blist:
#     print(item)

# for i in range(100, 1, -2):
#     print(i)

# range(start, stop, step)

# range(100)
    # start->0, stop->99, step->1
# range(1, 100)
    # start->1, stop->99, step->1
# range(1, 100, 2)
    # 1, 3, 5, 7, 9, 11, ...
    # start->1, stop->99, step->2

# alist = []
# total_sum = 0

# for i in range(10):
#     num = int(input("Enter number: "))
#     total_sum = total_sum + num
#     alist.append(num)

# print(alist)
# print(total_sum)

# break, continue

for i in range(1, 25):
    if i % 7 == 0:
        break
    print(i)

for i in range(1, 25):
    if i % 7 == 0:
        continue
    print(i)