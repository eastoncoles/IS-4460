import requests
import json

#Define the API endpoint
api_url = 'http://localhost:8000/api/orders/'

#Customer data as an array of JSON objects
order_data = {
        "customer": "1",
        "item_code": "12345",
        "quantity": "1"
    }


#Create customers using a single POST request
response = requests.post(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

#Check the response status and content
if response.status_code == 201:
    print("Orders created successfully.")
else:
    print(f"Error creating order.")