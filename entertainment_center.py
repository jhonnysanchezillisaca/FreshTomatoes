import json
import media
import fresh_tomatoes
import requests


def createMovies(title_movies):
    # this function creates the movie objects and returns a list of the movies
    urlOMDB = "https://www.omdbapi.com/?%s"
    movies = []

    for i in range(len(title_movies)):
        if title_movies[i]:
            search_by_title = {'t': title_movies[i]}
            response = requests.get(urlOMDB, search_by_title)
            jData = json.loads(response.content)
            imdb_id = jData['imdbID']
            trailer = getTrailer(getTMDBID(imdb_id))
            movies.append(media.Movie(jData['Title'], jData['Plot'],
                                      jData['Poster'], trailer))
    return movies


def getTrailer(tmdb_id):
    # this function returns the youtube url of the trailer from TMDB API
    # TODO handle no key case
    # TODO test multiple results case

    urlTMDBTrailer = "http://api.themoviedb.org/3/movie/%s/videos"
    params_TMDB_trailer = {'api_key': '7f276b4eaa72a85490d81dfb4504a1e6'}
    urlYoutube = "https://www.youtube.com/watch?v=%s"

    url_rq = urlTMDBTrailer % (tmdb_id)
    rq_trailer = requests.get(url_rq, params_TMDB_trailer)
    dataTMDB = json.loads(rq_trailer.content)
    return urlYoutube % dataTMDB['results'][0]['key']


def getTMDBID(imdb_id):
    # this function return the TMDB id receiving a IMDB id
    # TODO handle no results case

    urlTMDB = "https://api.themoviedb.org/3/%s/%s"
    params_TMDB_find = {'api_key': '7f276b4eaa72a85490d81dfb4504a1e6',
                        'external_source': 'imdb_id'}

    url_rq = urlTMDB % ('find', imdb_id)
    rq_movie = requests.get(url_rq, params_TMDB_find)
    data_TMDB = json.loads(rq_movie.content)
    return data_TMDB['movie_results'][0]['id']


# Creating movies
# To add a movie you need to add the title of the movie to title_movies
title_movies = ["Django Unchained", "Toy Story", "Avatar", "School of Rock",
                "Ratatouille", "Midnight in Paris", "Toy Story 2",
                "The Cove", "The Act of Killing", "Rocky"]
fresh_tomatoes.open_movies_page(createMovies(title_movies))
