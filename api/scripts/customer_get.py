import requests

id = 1 #the customer ID

#Define the API endpoint for a customer instance
api_url = f'http://localhost:8000/api/customers/{id}/'

#GET requests to retrieve the customer
response = requests.get(api_url)

#Check status code
if response.status_code == 200:
    customer_data = response.json()
    print(customer_data)
else:
    print("error retrieving the customer.")
