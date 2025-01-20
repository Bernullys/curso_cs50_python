text_input = input("Enter a string: ").lower()

vowels = ["a", "e", "i", "o", "u"]

# Split the input text
splited_text = list(text_input)

# List any of the characters are vowels
only_vowels = [x for x in splited_text if x in vowels]

# List any consonants characters
only_consonants = [y for y in splited_text if y not in vowels and y != " " and y.isalpha()]


print(f"Number of vowels: {len(only_vowels)}")
print(f"Number of consonants: {len(only_consonants)}")