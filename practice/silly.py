print(True and False)
print({1, False, 'hello',12.2})

dicts = {}
for i in range (1, 11):
    dicts[i] = i *2

print(dicts)

dict2 = {i: i*2 for i in range(1,11)}
print(dict2)

import random

countries = ["ve", "cl", "usa", "ca"]
population = {}
for country in countries:
    population[country] = random.randint(100000, 10000000000)
print(population)

population2 = {country: random.randint(100000, 10000000000) for country in countries}
print(population2)

countries_range = [1, 2, 3, 4]

lived = {country: country_range for(country, country_range) in zip(countries, countries_range)}
print(lived)

print(list(zip(countries, countries_range)))


result = { country: population for (country, population) in population2.items() if population > 500000}
print(result)