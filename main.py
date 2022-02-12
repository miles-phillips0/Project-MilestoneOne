import flask
import os
import requests
from dotenv import find_dotenv, load_dotenv
from genMovie import GenerateMovie
from tmdbApi import getTMDB
from wikiApi import getWiki

app = flask.Flask(__name__)
@app.route('/')

def index():
    #choose a random movie
    ID, name = GenerateMovie()

    #get movie info from TMDB
    Title, Tagline, Genres, ImagePath = getTMDB(ID)
   
    #get wiki link from mediaWiki
    Wiki_Link = getWiki(name)

    #Big Money Hustlas Doesn't have a tagline
    if name == "Big_Money_Hustlas":
        Tagline = "Magnets, How do they work??"
    
    return flask.render_template(
        "index.html",
        title = Title,
        tagline = Tagline,
        len = len(Genres),
        genres = Genres,
        imagePath = ImagePath,
        wikiLink = Wiki_Link
    )

app.run()

