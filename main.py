import random
import flask
import os
import requests
from dotenv import find_dotenv, load_dotenv

app = flask.Flask(__name__)
@app.route('/')

def index():
    #list of tmbd move IDS
    movieIDs = [157336, 15040,37165]
    wikiLinks = ["https://en.wikipedia.org/wiki/Interstellar_(film)/w/api.php", "https://en.wikipedia.org/wiki/Big_Money_Hustlas/w/api.php", "https://en.wikipedia.org/wiki/The_Truman_Show/w/api.php"]

    #get random movie from list
    RandomNum = random.randint(1,3)
    ID = movieIDs[RandomNum]
    link = wikiLinks[RandomNum]

    load_dotenv(find_dotenv())
    TMDB_KEY = os.getenv("TMDB_KEY")
    WIKI_KEY = os.getenv("WIKI_KEY")
    TMDB_URL = "https://api.themoviedb.org/3/movie/" + ID + "?api_key=" + TMDB_KEY + "&language=en-US"
    #WIKI_URL = #TODO get this

    #get TMDB
    responseTMDB = requests.get(TMDB_URL)
    responseTMDB_json = responseTMDB.json()

    try:
        Title = responseTMDB_json["title"]
        Tagline = responseTMDB_json["tagline"]
        Genres = []
        for genre in responseTMDB_json["genres"]:
            Genres.append(genre["name"])        
    except KeyError:
        print('TMDB API fail')
    
    #get WIKI Link

    responseWIKI = requests.get(WIKI_URL)
    responseWIKI_json = responseWIKI.json()

    Wiki_link
    
    try:
        Wiki_link = responseWIKI_json[] #TODO get the link
    except KeyError:
        print('WIKI API fail')
    
    return flask.render_template(
        "index.html",
        len = len(TMDB_List)
        TmdbList = TMDB_List
        link = Wiki_link
    )
app.run()

