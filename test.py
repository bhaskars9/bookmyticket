import tmdbsimple as tmdb
import requests

tmdb.API_KEY = '7a8e0acac3a7b83177ac5021a88e11d4'
# tmdb.API_KEY = 'YOUR_API_KEY_HERE'
tmdb.REQUESTS_SESSION = requests.Session()


# movie = tmdb.Movies(603)
# response = movie.info()
# print(movie.title)

search = tmdb.Search()
response = search.movie(query='The Bourne')
for s in search.results:
    print(s['title'], s['id'], s['release_date'], s['popularity'])

