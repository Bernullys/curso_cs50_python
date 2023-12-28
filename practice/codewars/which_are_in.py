a1 = ["arp", "live", "strong", "live"]
a2 = ["livaly", "alive", "harp", "sharp", "armstrong"]

r = list(filter(lambda x: x in a2, a1))

new_a1 = list(set(a1))
print(new_a1)

are_in = []

for a in new_a1:
    for b in a2:
        if a in b:
            are_in.append(a)
            break

print(sorted(are_in))


############### Some codewards solutions ######################################

def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})