from flask import Flask, render_template, request, flash, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = 'sdfh9e34gkggdf'


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

    artist_plus_song = artist_name + " " + song_name
    query = artist_plus_song.replace(" ", "+")

    # GETS MATCH ON YOUTUBE
    url = 'https://www.youtube.com/results?search_query=' + query
    source = requests.get(url, timeout=15)
    plain_text = source.text
    soup = BeautifulSoup(plain_text, "html.parser")

    try:
        # FETCHES THE URL
        songs = soup.findAll('div', {'class': 'yt-lockup-video'})
        song = songs[0].contents[0].contents[0].contents[0]
        link = "https://www.youtube.com" + song['href']

        return link
    except Exception as e:
        print("Can't find that, check your network or try a new song", e)
        flash("Can't find that, check your network or try a new song")
        return redirect(url_for('home'))


