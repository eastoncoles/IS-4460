import requests
import json

id = 1 #customer ID

#define API endpoint for customer instance
api_url = f'http://localhost:8000/api/customers/{id}/'

customer_data = {
        "name": "Easton",
        "email": "ERC@example.com",
        "phone_number": "3852807870",
    }

#Sends UPDATE request
response = requests.put(api_url, data=json.dumps(customer_data), headers={'Content-Type': 'application/json'})

#Check status code
if response.status_code == 200:
    print("Customer updated successfully.")
else:
    print("Error updating the customer.")