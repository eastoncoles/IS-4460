import requests
import json

#Define the API endpoint
api_url = 'http://localhost:8000/api/customers/'

#Customer data as an array of JSON objects
customer_data = {
        "name": "Easton",
        "email": "ERC@example.com",
        "phone_number": "3852807870"
    }


#Create customers using a single POST request
response = requests.post(api_url, data=json.dumps(customer_data), headers={'Content-Type': 'application/json'})

#Check the response status and content
if response.status_code == 201:
    print("Customers created successfully.")
else:
    print(f"Error creating customers.")
