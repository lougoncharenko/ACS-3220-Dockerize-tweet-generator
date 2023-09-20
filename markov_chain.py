import random

class Markov_Chain_Sentence_Generator:
    def __init__(self, corpus_file):
        self.corpus = self._read_corpus(corpus_file)
        self.chain = self._build_chain(self.corpus)
        
    def _read_corpus(self, corpus_file):
        with open(corpus_file, 'r') as file:
            corpus = file.read()
        return corpus.split()
    
    def _build_chain(self, corpus):
        chain = {}
        for i in range(len(corpus)-1):
            word = corpus[i]
            next_word = corpus[i+1]
            if word not in chain:
                chain[word] = []
            chain[word].append(next_word)
        return chain
    
    def generate_sentence(self, length=10):
        start_word = random.choice(list(self.chain.keys()))
        sentence = [start_word]
        
        while len(sentence) < length:
            current_word = sentence[-1]
            if current_word in self.chain:
                next_word = random.choice(self.chain[current_word])
                sentence.append(next_word)
            else:
                break
        
        return ' '.join(sentence)


corpus_file = 'Code/data/story.txt'  # Path to your corpus file
generator = Markov_Chain_Sentence_Generator(corpus_file)
sentence = generator.generate_sentence(length=10)
print(sentence)
