import os
import re

def count_words(text:str):
    word_count = {}

    # Use regular expressions to find all words in the sentence, ignoring case
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count




# import re
# from collections import Counter

# text = "Mary had a little lamb. Jack and Jill went up the hill. Peter, Paul, and Mary went to the concert."

# # Find words that start with a capital letter and are not behind a stop
# capital_words = re.findall(r"(?<!\.)\b[A-Z]\w+\b", text)

# # Separate all the words in the text
# separated_words = re.findall(r"\b\w+\b", text)

# # Eliminate the words stored in the capital_words variable from separated_words
# remaining_words = [word.lower() for word in separated_words if word not in capital_words]

# # Count the remaining words
# word_counts = Counter(remaining_words)

# print(word_counts)



file_path = 'el_quijote.txt'
# file_path = 'el_quijote.txt'
with open(file_path, encoding="utf-8") as file:
    cosas = file.read()

words = count_words(cosas)