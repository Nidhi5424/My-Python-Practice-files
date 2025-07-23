def char_frequency(text):
    """Returns the frequency of each character in the string as a dictionary."""
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

string_input = input("Enter a string: ")
print(char_frequency(string_input))
