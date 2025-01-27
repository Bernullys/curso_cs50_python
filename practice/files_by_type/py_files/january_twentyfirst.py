sentence = input("Enter a sentence: ")

splited_sentence = sentence.split()

organizator = {}

for word in splited_sentence:
    if word in organizator:
        organizator[word] += 1
    else:
        organizator[word] = 1

values_list = organizator.values()

max_value = max(values_list)
max_value_key = [key for key in organizator if organizator[key] == max_value][0]

print(f"The most frequent word is '{max_value_key}' with {max_value} occurrences.")