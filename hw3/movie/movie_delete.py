import requests

id =1

hw3_url = f'http://localhost:8000/hw3/movie-delete/{id}/'

response = requests.delete(hw3_url)

if response.status_code == 200:
    print("Movie deleted")
else:
    print("Error deleting movie.")