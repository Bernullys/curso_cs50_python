in_list_of_numbers = input("Type numbers separated by spaces:")

list_numbers = []
for num in in_list_of_numbers:
    if num.isdigit() == True:
        list_numbers.append(int(num))
    continue

list_total = sum(list_numbers)
list_large = len(list_numbers)

average = float(list_total/list_large)

print(average)