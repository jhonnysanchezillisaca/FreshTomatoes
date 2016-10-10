import json
import media
import fresh_tomatoes
import requests


def getTrailer(tmdb_id):
    print "\n\n\nIn getTrailer()"
    url_rq = urlTMDBTrailer % (tmdb_id)
    rq_trailer = requests.get(url_rq, params_TMDB_trailer)
    dataTMDB = json.loads(rq_trailer.content)
    print rq_trailer.url
    print dataTMDB
    return urlYoutube % dataTMDB['results'][0]['key']


def getTMDBID(imdb_id):
    print "\n\n\nin getTMDBID()"
    url_rq = urlTMDB % ('find', imdb_id)
    rq_movie = requests.get(url_rq, params_TMDB_find)
    data_TMDB = json.loads(rq_movie.content)
    print type(data_TMDB)
    print type(data_TMDB['movie_results'])
    print type(data_TMDB['movie_results'][0])
    print data_TMDB['movie_results']
    print rq_movie.url
    print data_TMDB['movie_results'][0]['id']
    print "\n\n movie_results"
    print data_TMDB['movie_results']
    return data_TMDB['movie_results'][0]['id']


urlOMDB = "https://www.omdbapi.com/?%s"
urlTMDB = "https://api.themoviedb.org/3/%s/%s"
urlTMDBTrailer = "http://api.themoviedb.org/3/movie/%s/videos"
urlYoutube = "https://www.youtube.com/watch?v=%s"
params_TMDB_find = {'api_key': '7f276b4eaa72a85490d81dfb4504a1e6',
                    'external_source': 'imdb_id'}
params_TMDB_trailer = {'api_key': '7f276b4eaa72a85490d81dfb4504a1e6'}

# Creating movies
title_movies = ["Django Unchained", "Toy Story", "Avatar", "School of Rock",
                "Ratatouille", "Midnight in Paris", "Toy Story 2",
                "The Cove", "The Act of Killing"]
movies = []

for i in range(len(title_movies)):
    search_by_title = {'t': title_movies[i]}
    response = requests.get(urlOMDB, search_by_title)
    jData = json.loads(response.content)
    print "\n\n\n in for loop"
    print jData
    imdb_id = jData['imdbID']
    trailer = getTrailer(getTMDBID(imdb_id))
    movies.append(media.Movie(jData['Title'], jData['Plot'],
                              jData['Poster'], trailer))

"""
django = media.Movie(jData['Title'], jData['Plot'], jData['Poster'], "")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")


avatar = media.Movie("Avatar",
                    "A marine on an alien planet",
                    "https://cdn.gotchamovies.com/wp-content/uploads/6676-avatar-avatar-movie-poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock",
                            "Storyline",
                            "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                        "Storyline",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                        "https://youtu.be/niD-jahFURU")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=dtiklALGz20")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
          django]
"""
fresh_tomatoes.open_movies_page(movies)
