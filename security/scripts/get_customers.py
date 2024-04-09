import requests

api_url = 'http://localhost:8000/api/customers/'

token = "4e6882ba2036aeeefae91922ddbd3194b2c96fcb"

headers = {
    'Authorization': f'Token {token}'
}

response = request.get(apit_url,headers=headers)

response=requests.get(api_url,headers=headers)

print(response.status_code)

#check the response sttus and content

if response.status_code ==200:
    print(f"customers retrieval succesful. {response.text}")

else: 
    print(f"Customers retrieval failed. {response.text}")