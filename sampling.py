# import packages
import random
import sys

# set command line arguments to a variable
number_of_runs = int(sys.argv[1])

def generate_histogram(source_text):
    """
    function generates a histogram from a source text
    """
    histogram = {}
    with open(source_text, 'r') as file:
        word_data = file.read().split(' ')
        for word in word_data:
            word = word.strip('.,!'). lower() 
            if word in histogram.keys():
                 histogram[word] += 1
            else:
                histogram[word] = 1
    return histogram

def generate_total_word_count(histogram):
    """
    function creates a total word count for the source text
    """
    weights = list(histogram.values())
    word_count = 0
    for weight in weights:
        word_count += weight
    return word_count           

def generate_random_word():
    """
    funtion generates a random word from the histogram
    """
    histogram = generate_histogram('Code/histogram.txt')
    keys = list(histogram.keys())
    weights = list(histogram.values())
    return random.choices(keys, weights=weights)[0]

def unique_words():
    histogram = generate_histogram('Code/histogram.txt')
    return len(histogram.keys())

def frequency_of_all_words(histogram):
    return list(histogram.items())

def print_frequency(histogram):
    for word in histogram:
      print(word , histogram.get(word, 0)) 


def collect_data(number_of_runs, word):
    unique_word_count = 0
    random_words = []
    random_words_histogram = {}
    for x in range(number_of_runs):
        random_words.append(generate_random_word())
    for word in random_words:
        if word in random_words_histogram.keys():
                random_words_histogram[word] += 1
        else:
            random_words_histogram[word] = 1
    return random_words_histogram

def get_probability(histogram):
    total = generate_total_word_count(histogram)
    new_histogram = {}
    for key, value in histogram.items():
        new_histogram[key] = (value/total)
    return new_histogram

def print_probability(histogram):
    new_histogram = get_probability(histogram)
    for key, value in new_histogram.items():
       print(f"{key}: {value}")
    

histogram = collect_data(number_of_runs, "blue")
print_frequency(histogram)
print_probability(histogram)

        


