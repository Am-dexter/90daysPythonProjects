#this program finds all number divisible by 3 but not a multiple of 7 between 900 and 1000

empty_list = []

for i in range(900, 1000):
    if (i % 3 == 0) and (i % 7 != 0):
        empty_list.append(str(i))

print(','.join(empty_list))