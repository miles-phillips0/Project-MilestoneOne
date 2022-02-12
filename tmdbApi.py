import os
import requests
from dotenv import find_dotenv, load_dotenv

def getTMDB(ID):
    load_dotenv(find_dotenv())
    TMDB_KEY = os.getenv("TMDB_KEY")
    TMDB_URL = "https://api.themoviedb.org/3/movie/" + str(ID) + "?api_key=" + str(TMDB_KEY) + "&language=en-US"
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
    return(Title, Tagline, Genres, ImagePath)