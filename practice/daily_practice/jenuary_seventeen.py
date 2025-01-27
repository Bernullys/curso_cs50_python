sentence = input("Type a sentence: ")

word_list = list(sentence.split(" "))

each_word_len = list(map(lambda x: len(x), word_list))
longest_word = max(each_word_len)

longest_word_index = each_word_len.index(longest_word)
print(f"The longest word id '{word_list[longest_word_index]}' with {longest_word} characters")