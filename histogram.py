import random
import string

class Histogram: 
  def __init__(self, source_text):
    self.histogram = self._generate_histogram(source_text)

  def _generate_histogram(self, source_text):
    histogram = {}
    with open(source_text, 'r') as file:

        word_data = file.read()
        translated_text = word_data.translate(str.maketrans('', '', string.punctuation)).lower()
        words = translated_text.split()
        for word in words:
          if word in histogram.keys():
                histogram[word] += 1
          else:
              histogram[word] = 1
    return histogram

  def unique_words(self):
    return len(self.histogram.keys())
  
  def frequency(self, word):
    return self.histogram.get(word, 0)

  def _generate_random_word(self):
    keys = list(self.histogram.keys())
    values = list(self.histogram.values())
    return random.choices(keys, weights=values)[0]
  
  def _generate_random_sentence(self):
    random_words = []
    for i in range(random.randint(3,20)):
      word = self._generate_random_word()
      random_words.append(word)
    sentence = ""
    for word in random_words:
      sentence += word + " "
    return sentence
  
