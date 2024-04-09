import requests
import json

id =1

hw3_url = f'http://localhost:8000/hw3/movie-update/{id}/'

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

response = requests.put(hw3_url, data=json.dumps(movie_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Movie updated successfully.")
else:
    print("Error updating movie.")