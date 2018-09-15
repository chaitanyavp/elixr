import requests
from firebase import firebase


def iter_customer_transactions():
    api_file = open("api.key", "r")
    api_key = api_file.readline().rstrip("\n")
    api_file.close()

    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions", headers={'Authorization': api_key})
    response_data = response.json()

    if response_data["statusCode"] == 200:
        return response_data["result"]
    else:
        return None


def read_firebase():
    fb = firebase.FirebaseApplication(
        'https://elixr-37b8a.firebaseio.com')
    result = fb.get('/users', None)
    print(result)


if __name__ == "__main__":
    read_firebase()
