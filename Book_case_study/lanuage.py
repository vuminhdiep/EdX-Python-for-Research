text = "This is my test text. We will use this text to test the function."

def count_word(text):
    text = text.lower()
    skips = [",", ".", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

count_word(text)

from collections import Counter

text = "This is my test text. We will use this text to test the function."

def count_word_fast(text):
    text = text.lower()
    skips = [",", ".", ":", ";", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts


count_word_fast(text)

def read_book(title_path):
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

#Read multiple files from different directories;
# import os
# book_dir = "./Book_case_study"
# for language in os.listdir(book_dir):
#     for author in os.listdir(book_dir + "/" + language):
#         for title in os.listdir(book_dir + "/" + language + "/" + author):
#            inputfile = book_dir + "/" + language + "/" + author + "/" + title 
#            print(inputfile)
#            text = read_book(inputfile)
#            (num_unique, counts) = word_stats(count_word(text)) 
                             
import pandas as pd  
table = pd.DataFrame(columns = ("name", "age"))
table.loc[1] = "James", 22
table.loc[2] = "Jess", 32
print(table)
