numbs = [11, 22, 33, 44, 55]

# multiplay nums by three (using map) and two ways of making a list:

res = map(lambda x: x*3, numbs)

print(res)

numbs_by_three = []
for i in res:
    numbs_by_three.append(i)
print(numbs_by_three)

res_ = list(map(lambda x: x*3, numbs))
print(res_)


# filtering the impairs (using filter):

impairs = list(filter(lambda y: y%2!=0, numbs))

print(impairs)