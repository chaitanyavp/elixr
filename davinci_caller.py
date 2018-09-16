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


#get how much a user has spent on transportation
def get_public_transportation(api_key):
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    total = 0;
    for i in response_data:
        if i['merchantCategoryCode'] in ['4112', '4131', '4111']:
            if i['currencyAmount'] > 0:
                total += i['currencyAmount']
    return total


# returns total amount spent on groceries
def get_groceries(api_key):
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    total = 0;
    second_last_month = 0
    last_month = 0;
    for i in response_data:
        if i['merchantCategoryCode'] in ['5411', '5422', '5451', '5462', '5499']:
            if i['currencyAmount'] > 0:
                position = i['originationDatTime'].find('T')
                print(position)
                if i['originationDateTime'][:position]:
                    last_month += i['currencyAmount']
    return total

# returns total amount of uneccessary eating
def get_unnecessary_eating(api_key):
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    total = 0;
    for i in response_data:
        if i['merchantCategoryCode'] in ['5441', '5811', '5812', '5813', '5814', '5921']:
            if i['currencyAmount'] > 0:
                total += i['currencyAmount']
    return total


def get_rec(api_key):
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    total = 0;
    for i in response_data:
        if i['merchantCategoryCode'] in ['5941', '5940', '7032', '7941', '7992', '7999']:
            if i['currencyAmount'] > 0:
                total += i['currencyAmount']
    return total


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


def get_yearly_spending(tdf):
    tdf["y"], _ = tdf['originationDateTime'].str.split('-', 1).str
    years = tdf["y"].drop_duplicates().values.tolist()
    years_spending = []
    for year in years:
        years_spending.append({"year":year, "spending": tdf.loc[(tdf["y"] == year) & (tdf["currencyAmount"] >= 0)]["currencyAmount"].values.sum()})

    return years_spending


def get_company_spending(tdf):
    merchants = tdf["merchantName"].drop_duplicates().values.tolist()
    merchant_spending = []
    for merc in merchants:
        merchant_spending.append({"merc": merc, "spending":
            tdf.loc[(tdf["merchantName"] == merc) & (tdf["currencyAmount"] >= 0)][
                "currencyAmount"].values.sum()})
    return sorted(merchant_spending, key=lambda k: k['spending'],
                      reverse=True)


def get_branch_spending(tdf):
    merchants = tdf["merchantId"].drop_duplicates().values.tolist()
    merchant_spending = []
    for merc in merchants:
        merc_df = tdf.loc[(tdf["merchantId"] == merc) & (tdf["currencyAmount"] >= 0)]
        if len(merc_df)>0:
            merchant_spending.append({"merc":merc_df["merchantName"].values[0], "spending": merc_df["currencyAmount"].values.sum()})

    return sorted(merchant_spending, key=lambda k: k['spending'], reverse=True)


def get_api_key():
    api_file = open("api.key", "r")
    api_key = api_file.readline().rstrip("\n")
    api_file.close()
    return api_key


if __name__ == "__main__":
    api_key = get_api_key()
    print(get_groceries(api_key))
    print(get_unnecessary_eating(api_key))

    # acc = get_account()
    # get_masked_account(acc, api_key)
    # tdf = get_transaction_df(api_key)
    # print(get_company_spending(tdf))

    # print(tdf.columns.values.tolist())

    # read_firebase()

    # acc = get_account()
    # get_bank_amounts(acc, api_key)
    # print(iter_customer_transactions(api_key))
    # read_firebase()
