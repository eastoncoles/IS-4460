import requests

id = 2 #the order ID

#Define the API endpoint for a customer instance
api_url = f'http://localhost:8000/api/orders/{id}/'

#GET requests to retrieve the customer
response = requests.get(api_url)

#Check status code
if response.status_code == 200:
    order_data = response.json()
    print(order_data)
else:
    print("error retrieving the order.")
    