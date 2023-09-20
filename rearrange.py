# Import Libraries
import random
import sys

# Variables
n = len(sys.argv)-1
words = sys.argv[1:]
random_words = random.sample(words, len(words))

for i in range(0, n):
    print(random_words[i], end = " ")
