"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from higher_order_markov_chain import Markov_Chain

app = Flask(__name__)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    corpus_file = './data/corpus.txt' 
    generator = Markov_Chain(corpus_file)
    sentence = generator.generate_sentence() 
    return render_template("index.html", sentence=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python3 app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
