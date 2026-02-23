def count_words(text):
    return len(text.split())

def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

def count_consonants(text):
    count = 0
    for ch in text.lower():
        if ch.isalpha() and ch not in "aeiou":
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    t = text.lower().replace(" ", "")
    return t == t[::-1]

def remove_vowels(text):
    result = ""
    for ch in text:
        if ch.lower() not in "aeiou":
            result += ch
    return result

def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def longest_word(text):
    words = text.split()
    longest = ""
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))
    lw = longest_word(text)
    print("Longest word:", lw, "(" + str(len(lw)) + " letters)")
    freq = word_frequency(text)
    freq_str = ", ".join(k + ": " + str(v) for k, v in freq.items())
    print("Word Frequency:", freq_str)

text = input("Enter text: ")
analyze_text(text)
