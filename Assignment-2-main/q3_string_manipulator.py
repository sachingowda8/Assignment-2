sentence = input("Enter a sentence: ")

words = sentence.split()
first_word = words[0]
last_word = words[-1]

# reverse by going backwards through the string
reversed_sentence = sentence[::-1]

# count characters without spaces
no_space = sentence.replace(" ", "")

print("Original:", sentence)
print("Characters (with spaces):", len(sentence))
print("Characters (without spaces):", len(no_space))
print("Words:", len(words))
print("UPPERCASE:", sentence.upper())
print("lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("First word:", first_word)
print("Last word:", last_word)
print("Reversed:", reversed_sentence)
