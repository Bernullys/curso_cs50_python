in_list_of_numbers = input("Type numbers separated by spaces:").strip()

# list_numbers = []
# for num in in_list_of_numbers:
#     if num.isdigit() == True:
#         list_numbers.append(int(num))
#     continue

list_numbers = [int(l_n) for l_n in in_list_of_numbers if l_n.isdigit()]

list_total = sum(list_numbers)
list_large = len(list_numbers)
average = round(list_total/list_large, 2)
print(f"{average:,.2f}")

