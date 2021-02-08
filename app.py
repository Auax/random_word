from flask import Flask, render_template, redirect, url_for, request, session
import os
import random
from util.requests import get_url, find_all, find, convert_to_str

app = Flask(__name__)


@app.route('/')
def index():
    if not return_all(randomize=True):
        return redirect('/')
    
    else:
        word, translation, definitions = return_all(randomize=True)

    return render_template('index.html', word=word, translation=translation, definitions=definitions)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['search-query']

    return redirect(f'/search/{query}')


@app.route('/search/<string:word>')
def return_word(word):

    if not return_all(word):
        return render_template('error.html')
    
    else:
        word, translation, definitions = return_all(word)

    return render_template('index.html', word=word, translation=translation, definitions=definitions)


i = 0
def return_all(word=None, randomize:bool=None):

    assert type(word) == str if randomize == None else True

    # Get Word
    f = open('words.txt', 'r')
    words = f.readlines()
    f.close()

    if randomize:
        word = random.choice(words).strip('\n')

    URL = f'https://dictionary.cambridge.org/dictionary/english-spanish/{word}'

    # Get translation
    content = get_url(URL)

    try:
        translation = find(content, 'span', 'trans').text

    except AttributeError:
        return False

    translation = translation.replace(' ', '').strip('\n')

    # Get Definitions
    # content = get_url(URL)
    definitions = find_all(content, 'div', 'def')
    definitions = convert_to_str(definitions)

    return [word, translation, definitions]



if __name__ == '__main__':
    app.run(debug=True)
