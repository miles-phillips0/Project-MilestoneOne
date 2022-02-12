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
    movieNames = ["Interstellar_(film)", "Big_Money_Hustlas", "The_Truman_Show"]

    #get random movie from list
    RandomNum = random.randint(1,3)
    ID = movieIDs[RandomNum-1]
    name = movieNames[RandomNum-1]

    load_dotenv(find_dotenv())
    TMDB_KEY = os.getenv("TMDB_KEY")
    TMDB_URL = "https://api.themoviedb.org/3/movie/" + str(ID) + "?api_key=" + str(TMDB_KEY) + "&language=en-US"
   

    #get TMDB
    responseTMDB = requests.get(TMDB_URL)
    responseTMDB_json = responseTMDB.json()

    try:
        Title = responseTMDB_json["title"]
        Tagline = responseTMDB_json["tagline"]
        Genres = []
        ImagePath = "https://www.themoviedb.org/t/p/w500"+ responseTMDB_json["poster_path"]
        for genre in responseTMDB_json["genres"]:
            Genres.append(genre["name"])        
    except KeyError:
        print('TMDB API fail')
    
    #get WIKI Link
    wikiEndPoint = "https://en.wikipedia.org/w/api.php"
    wikiParams = {
    "action" : "query",
    "titles" : name,
    "prop"  :   "info",
    "inprop" : "url",
    "format" : "json",
    "formatversion" : "2",
    "origin" : "*"
    }
    result = requests.get(wikiEndPoint, wikiParams)
    result_json = result.json()
    try:
        Wiki_Link = result_json["query"]["pages"][0]["fullurl"]
    except KeyError:
        print('WIKI API fail')
    
    #Big Money Hustlas Doesn't have a tagline
    if movieNames[RandomNum-1] == "Big_Money_Hustlas":
        Tagline = "Magnets, How do they work??"
    
    return flask.render_template(
        "index.html",
        title = Title,
        tagline = Tagline,
        len = len(Genres),
        genres = Genres,
        imagePath = ImagePath
        wikiLink = Wiki_Link
    )

app.run()

