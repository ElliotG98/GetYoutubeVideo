from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/post_field', methods=['GET', 'POST'])
def form_input():
    artist_name = ''
    song_name = ''

    for key, value in request.form.items():
        if key == 'artist_name':
            artist_name += value
        elif key == 'song_name':
            song_name += value

    return artist_name + " " + song_name


