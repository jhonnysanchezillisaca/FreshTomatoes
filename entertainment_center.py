import json
import media
import fresh_tomatoes
import requests


urlApi = "https://www.omdbapi.com/?%s"


# Creating movies
title_movies = ["Django", "Toy Story", "Avatar", "School of Rock",
                "Ratatouille", "Midnight in Paris", "Django"]
movies = []

for i in range(len(title_movies)):
    search_by_title = {'t': title_movies[i]}
    response = requests.get(urlApiT, search_by_title)
    jData = json.loads(response.content)
    movies.append(media.Movie(jData['Title'], jData['Plot'],
                              jData['Poster'], ""))

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
