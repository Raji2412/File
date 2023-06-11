import re
from collections import Counter

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    word_counts = Counter(words)
    top_words = word_counts.most_common(10)
    print("Top 10 most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")


file_path = "sample.txt"
count_words(file_path)
