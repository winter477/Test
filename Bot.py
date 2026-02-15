import requests

# Use Miraheze Meta as the login base
API_URL = "https://corewiki.miraheze.org/w/api.php"

# Start a session
session = requests.Session()

# 1. Get login token
params_1 = {
    "action": "query",
    "meta": "tokens",
    "type": "login",
    "format": "json"
}
res = session.get(API_URL, params=params_1).json()
login_token = res['query']['tokens']['logintoken']

# 2. Log in with your new credentials
params_2 = {
    "action": "login",
    "lgname": "EZYA@UTRS",
    "lgpassword": "mb465ufnj85n9olurorsovnh575i52nu",
    "lgtoken": login_token,
    "format": "json"
}
response = session.post(API_URL, data=params_2).json()

print(response)
