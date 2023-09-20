import random

def generate_sentence(corpus, order=1, max_length=20):
    # Create a dictionary to store the transition probabilities
    transitions = {}

    # Split the corpus into words
    words = corpus.split()

    # Generate transition probabilities for each word based on the order
    for i in range(len(words) - order):
        prefix = tuple(words[i:i+order])
        suffix = words[i+order]

        if prefix in transitions:
            transitions[prefix].append(suffix)
        else:
            transitions[prefix] = [suffix]

    # Start the sentence with a random prefix
    current_prefix = random.choice(list(transitions.keys()))
    sentence = list(current_prefix)

    # Generate the sentence
    while len(sentence) < max_length:
        if current_prefix in transitions:
            next_word = random.choice(transitions[current_prefix])
            sentence.append(next_word)
            current_prefix = tuple(sentence[-order:])
        else:
            break

    return ' '.join(sentence)



corpus = "A man, a plan, a canal: Panama! A dog, a panic in a pagoda!"
generated_sentence = generate_sentence(corpus, order=2, max_length=10)
print(generated_sentence)