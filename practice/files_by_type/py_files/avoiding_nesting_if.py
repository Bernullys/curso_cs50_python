
def process_number(numbers_array):
    results = []
    for number in numbers_array:
        if number is not None:
            if number > 0:
                if number % 2 == 0:
                    if number < 100:
                        results.append(number)
    return results
# %%                 
def better_way_process_number(number_array):
    results = []
    for number in number_array:
        if number is None: #This skip the iteration and go to the next value.
            continue
        odd_one = number % 2 != 0
        out_of_range = number > 100 or number <= 0
        if odd_one or out_of_range:
            continue
        results.append(number)
    return results
# %%
a = [100000, None, 1, 34, 354, 0, 12]

print(better_way_process_number(a))
print(process_number(a))


