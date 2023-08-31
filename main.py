def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_mapping = {}
    lower_text = text.lower()
    for char in lower_text:
        if not char.isalpha():
            continue
        if not char in letter_mapping:
            letter_mapping[char] = 1
        else:
            letter_mapping[char] += 1
    return letter_mapping

def average_sentence_length(text):
    sentences = text.split('.')
    avg = 0
    for sentence in sentences:
        words = sentence.split()
        avg += len(words)
    avg //= len(sentences)
    return avg

def print_report(num_words, letter_mapping, average_length):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print(f"The sentences are on average {average_length} words long\n")
    sorted_mapping = list(letter_mapping.items())
    sorted_mapping.sort()
    for pair in sorted_mapping:
        print(f"The '{pair[0]}' character was found {pair[1]} times")
    print("--- End report ---")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    num_words = count_words(file_contents)
    letter_mapping = count_letters(file_contents)
    average_length = average_sentence_length(file_contents)
    print_report(num_words, letter_mapping, average_length)