import requests
import json

movie_url = 'http://localhost:8000/hw3/movie-add'

movie_data = {
        'title': "Title",
        'description': "Description",
        'director': "Director",
        'release_year': '1900',
        'budget': '0',
        'runtime': '0:00',
        'rating':'G',
        'genre':'Other'
    }

response = requests.post(movie_url, data=json.dumps(movie_data), headers={'Content-Type':'application/json'})

if response.status_code == 201:
    print("Movie created successfully.")
else:
    print(f"Error creatiing Movie")

