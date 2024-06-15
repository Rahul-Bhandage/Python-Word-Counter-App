from flask import Flask, render_template, request
import re
from collections import Counter

app = Flask(__name__)

def word_counter(text):
    # Count occurrences of all words, numbers, and symbols
    words = re.findall(r'\b\w+\b', text.lower())
    numbers = re.findall(r'\b\d+\b', text)
    symbols = re.findall(r'[^\w\s]', text)

    word_counts = Counter(words)
    number_counts = Counter(numbers)
    symbol_counts = Counter(symbols)

    # Calculate total counts
    total_words = len(words)
    total_numbers = len(numbers)
    total_symbols = len(symbols)

    return word_counts, number_counts, symbol_counts, total_words, total_numbers, total_symbols

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    word_counts, number_counts, symbol_counts, total_words, total_numbers, total_symbols = word_counter(text)
    return render_template('result.html', word_counts=word_counts, number_counts=number_counts, symbol_counts=symbol_counts, total_words=total_words, total_numbers=total_numbers, total_symbols=total_symbols)

if __name__ == '__main__':
    app.run(debug=True)
