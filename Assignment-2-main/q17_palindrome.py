word = input("Enter a word or number: ")

# ignore case for comparison
cleaned = word.lower()
reversed_word = cleaned[::-1]

print("Original:", word)
print("Reversed:", reversed_word)

if cleaned == reversed_word:
    print("Result: PALINDROME")
else:
    print("Result: NOT a Palindrome")

