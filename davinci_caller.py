import requests
from firebase import firebase
import pandas


def get_transaction_df(api_key):
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions", headers={'Authorization': api_key})
    response_data = response.json()
    if response_data["statusCode"] == 200:
        return pandas.DataFrame.from_records(response_data["result"])
    else:
        return None


def get_account():
    file = open("sample_customer", "r")
    account = file.readline().rstrip("\n")
    file.close()
    return account


def get_masked_account(acc, api_key):
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc, headers ={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]
    print(data["maskedRelatedBankAccounts"])


def get_income(acc, api_key):
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc,
                       headers={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]
    print(data["totalIncome"])


def get_bank_amounts(acc, api_key):
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc + "/accounts", headers={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]["bankAccounts"]
    num_items = len(data)
    for i in data:
        print(i["balance"])


def read_firebase():
    fb = firebase.FirebaseApplication(
        'https://elixr-37b8a.firebaseio.com')
    result = fb.get('/users', None)
    print(result)


def get_monthly_spending(tdf):
    tdf["ym"], _ = tdf['originationDateTime'].str.rsplit('-', 1).str
    months = tdf["ym"].drop_duplicates().values.tolist()
    monthly_spending = []
    for month in months:
        monthly_spending.append({"month":month, "spending": tdf.loc[(tdf["ym"] == month) & (tdf["currencyAmount"] >= 0)]["currencyAmount"].values.sum()})

    return monthly_spending


if __name__ == "__main__":
    api_file = open("api.key", "r")
    api_key = api_file.readline().rstrip("\n")
    api_file.close()

    # acc = get_account()
    # get_masked_account(acc, api_key)
    tdf = get_transaction_df(api_key)

    print(get_monthly_spending(tdf))
    # print(tdf.columns.values.tolist())

    # read_firebase()

    # acc = get_account()
    # get_bank_amounts(acc, api_key)
    # print(iter_customer_transactions(api_key))
    # read_firebase()
