import flask
import os
import requests
from dotenv import find_dotenv, load_dotenv

app = flask.Flask(__name__)
@app.route('/')

def index():
    load_dotenv(find_dotenv())
    
    TMDB_KEY = os.getenv("TMDB_KEY")
    WIKI_KEY = os.getenv("WIKI_KEY")
    TMDB_URL = #TODO get this
    WIKI_URL = #TODO get this

    #get TMDB
    responseTMDB = requests.get(TMDB_URL)
    responseTMDB_json = responseTMDB.json()

    TMDB_List

    try:
        results = responseTMDB_json["results"]
        TMDB_List = [results['original_title']] #TODO Add tagline, genres, poster image
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

