n = int(input("number: "))

# n_list = list(range(0,n))

# multiples_of_three_and_five = 0

# for each in n_list:
#     if each % 3 == 0 or each % 5 == 0:
#         multiples_of_three_and_five += each

# print(multiples_of_three_and_five)


print(sum(x for x in range(0, n) if x % 3 == 0 or x % 5 == 0))