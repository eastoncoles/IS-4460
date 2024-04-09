import requests
import json

id = 1 #order ID

#define API endpoint for order instance
api_url = f'http://localhost:8000/api/orders/{id}/'

customer_id = 1

order_data = {
        "customer": customer_id,
        "item_code": "12345",
        "quantity": "1"
    }

#Sends DELETE request
response = requests.put(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

#Check status code
if response.status_code == 200:
    print("Order deleted successfully.")
else:
    print("Error deleting the order.")