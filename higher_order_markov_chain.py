import random
import re
from listogram import Listogram

class Markov_Chain(dict):
    def __init__(self, word_list=None):
        super().__init__()
        if word_list is not None:
            parsed_word_list = self.corpus_parser(word_list)
            for i, word in enumerate(parsed_word_list):
                if i <= (len(parsed_word_list) - 2):
                    self.build_chains(word, parsed_word_list[i + 1])
                else:
                    if word not in self:
                        self[word] = []
        for word, tokens in self.items():
            self[word] = Listogram(tokens)

    def corpus_parser(self, source_text):
        self.word_list = []
        with open(source_text, 'r') as infile:
            words = infile.read().split()
            for word in words:
                word = re.sub("-", " ", word)
                word = re.sub("[^a-zA-Z!,.?']", "", word)
                self.word_list.append(word)

        return self.word_list

    def build_chains(self, word, next_word):
        if word in self:
            self[word].append(next_word)
        else:
            self[word] = [next_word]

    def generate_sentence(self):
        current_word = random.choice(list(self.keys()))
        random_words = []
        random_words.append(current_word)

        for _ in range(random.randint(5, 30)):
            next_word = self[current_word].sample()
            if next_word != "I":
                random_words.append(next_word.lower())
            else:
                random_words.append(next_word)
            current_word = next_word
    
        sentence = " ".join(random_words)
        new_string = sentence.replace(",", "")
        new_sentence = new_string.replace(".", "")
        sentence = new_sentence.capitalize() + '.'
        return sentence



    