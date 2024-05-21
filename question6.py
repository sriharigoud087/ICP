sentence = "I am a teacher and I love to inspire and teach people"

# Split the sentence into words
words = sentence.split()

# Get the unique words using a set
unique_words = set(words)

# Get the number of unique words
num_unique_words = len(unique_words)

print("Number of unique words:", num_unique_words)
