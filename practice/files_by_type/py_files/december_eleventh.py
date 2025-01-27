sentence = input("Enter a sentence: ").lower()

def sep_words(texts):
    sentence_list = texts.split()
    return sentence_list

list_of_words = sorted(sep_words(sentence))

base_dict = {}

for word in list_of_words:
    if word in base_dict:
        base_dict[word] += 1
    else:
        base_dict[word] = 1

for base in base_dict:
    print(base, base_dict[base])
