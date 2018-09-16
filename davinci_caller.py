import requests
from firebase import firebase
import pandas
import datetime


# get all the transactions for a customer and returns in as a pandas dataframe
def get_transaction_df(api_key, customer_key):
    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions", headers={'Authorization': api_key})
    response_data = response.json()
    if response_data["statusCode"] == 200:
        return pandas.DataFrame.from_records(response_data["result"])
    else:
        return None


#returns the account number of a sample customer
def get_account():
    file = open("sample_customer", "r")
    account = file.readline().rstrip("\n")
    file.close()
    return account


def get_masked_account(acc, api_key):
    """ Return the masked account number of the customer """
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc, headers ={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]
    print(data["maskedRelatedBankAccounts"])


def get_income(acc, api_key):
    """ Return the income of the customer """
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc,
                       headers={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]
    return data["totalIncome"]


def get_bank_amounts(acc, api_key):
    """ Return the amounts of the bank accounts for each customer """
    res = requests.get("https://api.td-davinci.com/api/customers/" + acc + "/accounts", headers={'Authorization': api_key})
    res_data = res.json()
    data = res_data["result"]["bankAccounts"]
    for i in data:
        print(i["balance"])


def get_public_transportation(api_key):
    """ Returns how much was spend on public transportation in the last month """
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    total = 0
    last_ar = []
    for i in response_data:
        if i['merchantCategoryCode'] in ['4112', '4131', '4111']:
            if i['currencyAmount'] > 0:
                td = i['originationDateTime']
                cur_date = datetime.date.today()
                last_month = decrement_month(cur_date)

                if td is not None:
                    if td > last_month:
                        last_ar.append(i)

    last_total = 0;
    for i in last_ar:
        last_total += i['currencyAmount']

    return total


# returns total amount and goals spent on groceries over last two months
def get_groceries(api_key):
    """ Returns total amount and goals spent on groceries over the last two months """
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    last_ar = []
    second_last_ar = []
    for i in response_data:
        if i['merchantCategoryCode'] in ['5411', '5422', '5451', '5462', '5499']:
            if i['currencyAmount'] > 0:
                td = i['originationDateTime']
                cur_date = datetime.date.today()
                last_month = decrement_month(cur_date)
                lasty_month = datetime.date(int(last_month[0:4]), int(last_month[5:7]), int(last_month[8:]))
                second_last = decrement_month(lasty_month)

                if td is not None:
                    if td > last_month:
                        last_ar.append(i)
                    elif td > second_last:
                        second_last_ar.append(i)

    last_total = 0
    second_last_total = 0
    for i in last_ar:
        last_total += i['currencyAmount']
    for i in second_last_ar:
        second_last_total += i['currencyAmount']
    print(last_total)
    print(second_last_total)
    res_ar = []
    res_ar.append(round(second_last_total, 2))
    res_ar.append(round(second_last_total * 1.1, 2))
    res_ar.append(round(last_total, 2))
    return res_ar


def get_rest(api_key):
    """ Reutrn amount spent at restaurnats and unhealthy places in the last month """
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    last_ar = []
    second_last_ar = []
    for i in response_data:
        if i['merchantCategoryCode'] in ['5441', '5811', '5812', '5813', '5814', '5921']:
            if i['currencyAmount'] > 0:
                td = i['originationDateTime']
                cur_date = datetime.date.today()
                last_month = decrement_month(cur_date)
                lasty_month = datetime.date(int(last_month[0:4]), int(last_month[5:7]), int(last_month[8:]))
                second_last = decrement_month(lasty_month)

                if td is not None:
                    if td > last_month:
                        last_ar.append(i)
                    elif td > second_last:
                        second_last_ar.append(i)

    last_total = 0;
    second_last_total = 0;
    for i in last_ar:
        last_total += i['currencyAmount']
    for i in second_last_ar:
        second_last_total += i['currencyAmount']

    res_ar = []
    res_ar.append(round(second_last_total, 2))
    res_ar.append(round(second_last_total * .9, 2))
    res_ar.append(round(last_total, 2))
    return res_ar


def get_rec(api_key):
    """ Returns the amount spend on recreation in the last month """
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()

    response = requests.get("https://api.td-davinci.com/api/customers/" + customer_key + "/transactions",
                            headers={'Authorization': api_key})
    response_data = response.json()
    response_data = response_data["result"]
    last_ar = []
    for i in response_data:
        if i['merchantCategoryCode'] in ['5941', '5940', '7032', '7941', '7992', '7999']:
            if i['currencyAmount'] > 0:
                td = i['originationDateTime']
                cur_date = datetime.date.today()
                last_month = decrement_month(cur_date)

                if td is not None:
                    if td > last_month:
                        last_ar.append(i)

    last_total = 0
    res_ar = []
    for i in last_ar:
        last_total += i['currencyAmount']
    res_ar.append(last_total)
    income = get_income(customer_key, api_key)
    percent = income / 12 * .02
    res_ar.append(round(percent, 2))
    return res_ar


def decrement_month(cur_date):
    """ Find the date one month before given date """
    m = cur_date.month
    if m < 10:
        m = '0' + str(m)
    else:
        m = str(m)
    cur_date = str(cur_date.year) + '-' + m + '-' + str(cur_date.day)
    month = int(cur_date[5:7])
    if month == 1:
        prev_month = 12
    else:
        prev_month = month - 1;

    if prev_month < 10:
        prev_month = '0' + str(prev_month)
    else:
        prev_month = str(prev_month)
    cur_date = cur_date[0:5] + prev_month + cur_date[7:]
    return cur_date


def read_firebase(customer_id):
    """ Read firebase """
    fb = firebase.FirebaseApplication(
        'https://elixr-37b8a.firebaseio.com')
    points = int(fb.get('/'+customer_id+"/points", None))
    steps = int(fb.get('/'+customer_id+"/steps", None))
    return points, steps

def add_firebase_goal(text, customer_id):
    fb = firebase.FirebaseApplication(
        'https://elixr-37b8a.firebaseio.com')
    fb.post("/" + customer_id + "/tasks")
    points = int(fb.get('/' + customer_id + "/points", None))
    steps = int(fb.get('/' + customer_id + "/steps", None))
    return points, steps


def get_grocery_list(tdf):
    grocery_store_codes = [5411, 5422, 5451, 5462, 5499]
    grocery_store_categories = {5411:"Supermarket", 5422:"Meats", 5451:"Dairy", 5462:"Bakeries", 5499:"Misc. food"}
    grocery_spending = []
    for code in grocery_store_codes:
        category = grocery_store_categories[code]
        spending = tdf.loc[(tdf["merchantCategoryCode"] == code) & (tdf["currencyAmount"] >= 0)]["currencyAmount"].values.sum()
        grocery_spending.append({"category":category, "spending":spending})
    return sorted(grocery_spending, key=lambda k: k['spending'], reverse=True)


def get_eatingout_list(tdf):
    eatingout_codes = [5441, 5811, 5812, 5813, 5814, 5921]
    eatingout_categories = {5441:"Candy", 5811:"Catering", 5812:"Restaurants", 5813:"Drinking Places", 5814:"Fast food", 5921:"Alcohol"}
    eatingout_spending = []
    for code in eatingout_codes:
        category = eatingout_categories[code]
        spending = tdf.loc[(tdf["merchantCategoryCode"] == code) & (tdf["currencyAmount"] >= 0)]["currencyAmount"].values.sum()
        eatingout_spending.append({"category":category, "spending":spending})
    return sorted(eatingout_spending, key=lambda k: k['spending'], reverse=True)


def get_monthly_spending(tdf):
    """ Return the monthly spending of a customer """
    tdf["ym"], _ = tdf['originationDateTime'].str.rsplit('-', 1).str
    months = tdf["ym"].drop_duplicates().values.tolist()
    monthly_spending = []
    for month in months:
        monthly_spending.append({"month": month, "spending": tdf.loc[(tdf["ym"] == month) & (tdf["currencyAmount"] >= 0)]["currencyAmount"].values.sum()})

    return sorted(monthly_spending, key=lambda k: k['month'])


def get_yearly_spending(tdf):
    """ Return  yearly spending of a customer """
    tdf["y"], _ = tdf['originationDateTime'].str.split('-', 1).str
    years = tdf["y"].drop_duplicates().values.tolist()
    years_spending = []
    for year in years:
        years_spending.append({"year": year, "spending": tdf.loc[(tdf["y"] ==
                                                                 year) & (tdf["currencyAmount"] >= 0)]
        ["currencyAmount"].values.sum()})

    return sorted(years_spending, key=lambda k: k['year'])


def get_company_spending(tdf):
    """ Return  spending at companies by a customer """
    merchants = tdf["merchantName"].drop_duplicates().values.tolist()
    merchant_spending = []
    for merc in merchants:
        spending = tdf.loc[(tdf["merchantName"] == merc) & (tdf["currencyAmount"] >= 0)][
                "currencyAmount"].values.sum()
        if spending > 0:
            merchant_spending.append({"merc": merc, "spending":spending})
    return sorted(merchant_spending, key=lambda k: k['spending'], reverse=True)


def get_branch_spending(tdf):
    """ Return spending at each branch by a customer """
    merchants = tdf["merchantId"].drop_duplicates().values.tolist()
    merchant_spending = []
    for merc in merchants:
        merc_df = tdf.loc[(tdf["merchantId"] == merc) & (tdf["currencyAmount"] >= 0)]
        if len(merc_df) > 0:
            merchant_spending.append({"merc":merc_df["merchantName"].values[0], "spending": merc_df["currencyAmount"].values.sum()})
    return sorted(merchant_spending, key=lambda k: k['spending'], reverse=True)


def get_api_key():
    """ Get the api key from file """
    api_file = open("api.key", "r")
    api_key = api_file.readline().rstrip("\n")
    api_file.close()
    return api_key


def get_customer_key():
    """ Reutrn the key of the sample customer from file """
    customer_file = open("sample_customer", "r")
    customer_key = customer_file.readline().rstrip("\n")
    customer_file.close()
    return customer_key


if __name__ == "__main__":
    ap_key = get_api_key()
    customer_key = get_customer_key()
    print(get_rest(ap_key))

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
