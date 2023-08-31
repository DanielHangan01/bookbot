def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_mapping = {}
    text = text.lower()
    for char in text:
        if char == ' ':
            pass
        if not char in letter_mapping:
            letter_mapping[char] = 1
        else:
            letter_mapping[char] += 1
    return letter_mapping


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(count_words(file_contents))
    print(count_letters(file_contents))