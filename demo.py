from kimdb import IMDB

imdb = IMDB(debug=True)

top_movies = imdb.top_movies()
top_movies[0].jsonprint()

top_series = imdb.top_series()
top_series[0].jsonprint()

most_popular_movies = imdb.most_popular_movies()
most_popular_movies[0].jsonprint()

most_popular_series = imdb.most_popular_movies()
most_popular_series[0].jsonprint()

title = imdb.get_title(top_movies[0].id)
title.jsonprint()

list = imdb.get_list(title.lists[0].id)
list.jsonprint()

user = imdb.get_user(list.owner.id)
user.jsonprint()

name = imdb.get_name(title.actors[0].id)
name.jsonprint()
