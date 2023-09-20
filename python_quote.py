import random

quotes = ("Rebellions are built on hope. -Jyn ",
          "The ability to speak does not make you intelligent. - Qui-Gon Jinn",
          "Try not. Do or do not. There is no try. —Yoda",
          "We’ll always be with you. No one’s ever really gone. A thousand generations live in you now. —Luke Skywalker",
          "Once you start down the dark path, forever will it dominate your destiny. -Yoda"
          )

def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)
