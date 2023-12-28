characters_chain = input("string: ")
# list_from_string = []
# if len(characters_chain) % 2 == 0:
#     print("is pair")
#     for c in range(0, len(characters_chain), 2):
#         list_from_string.append(characters_chain[c:c+2])
# else:
#     print('not a pair')
#     new_cha_cha = f"{characters_chain}_"
#     print(new_cha_cha)
#     for c in range(0, len(new_cha_cha), 2):
#         list_from_string.append(new_cha_cha[c:c+2])


# print(list_from_string)


##########Other solution##################

import re

print(re.findall(".{2}", characters_chain + "_"))