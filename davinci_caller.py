import requests


api_file = open("api.key", "r")
api_key = api_file.readline().rstrip("\n")
api_file.close()

customer_file = open("sample_customer", "r")
customer_key = customer_file.readline().rstrip("\n")
customer_file.close()

response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions", headers ={'Authorization': api_key})
response_data = response.json()

print(response_data["statusCode"])
print(response_data["result"])