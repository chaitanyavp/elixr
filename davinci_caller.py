import requests

api_file = open("api.key", "r")
api_key = api_file.readline().rstrip("\n")
api_file.close()

customer_file = open("sample_customer", "r")
customer_key = customer_file.readline().rstrip("\n")
customer_file.close()

response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions", headers ={'Authorization': api_key})
response_data = response.json()


#print(response_data["statusCode"])
#print(response_data["result"])


def get_account():
    file = open("sample_customer", "r")
    account = file.readline().rstrip("\n")
    file.close()
    return account


def get_masked_account(acc):
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc, headers ={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]
    print(data["maskedRelatedBankAccounts"])


def get_income(acc):
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc,
                       headers={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]
    print(data["totalIncome"])


def get_bank_amount(acc):
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc + "/accounts", headers={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]
    print(data)
    print(data["bankAccount"]["balance"])


acc = get_account()
get_masked_account(acc)
