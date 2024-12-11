sentence = input("Enter a sentence: ")

def sep_words(texts):
    sentence_list = texts.split()
    return sentence_list

list_of_words = sep_words(sentence)
print(list_of_words)